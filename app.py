import os
import json
import logging
import functools
import inspect
import traceback
import sys
from datetime import datetime
from fastapi import FastAPI, HTTPException

# Logger setup
def log_decorator(fn):
    logger = logging.getLogger(fn.__module__)
    line_number = inspect.getsourcelines(fn)[1]
    module_name = inspect.getmodule(fn).__name__

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        now = datetime.now()
        logger.info(" " * 3 + f"{now} - Going to run the '{fn.__name__}' method (Module: {module_name}, Line: {line_number})")

        try:
            out = fn(*args, **kwargs)
            logger.info(" " * 3 + f"{now} - Done successfully running the '{fn.__name__}' method (Module: {module_name}, Line: {line_number})")
            return out

        except Exception as err:
            logger.error(f"\nError occurred in method '{fn.__name__}' (Module: {module_name}, Line: {line_number}):")
            logger.error(f"Error Type: {type(err).__name__}")
            logger.error(f"Error Message: {str(err)}")
            logger.error(f"Traceback:\n{traceback.format_exc()}")
            sys.exit(1)

    return wrapper

# In-memory storage for notes
notes_db = {}

# FastAPI app
app = FastAPI()

# Timestamped note format
def create_timestamped_note(filename, subject, other_info, content):
    timestamp = datetime.now().isoformat()
    return {
        "filename": filename,
        "subject": subject,
        "other_info": other_info,
        "content": content,
        "timestamp": timestamp
    }

@app.post("/create_note")
@log_decorator
def create_note_api(data: dict):
    filename, subject, other_info, content = (
        data['filename'],
        data['subject'],
        data['other_info'],
        data['content'],
    )

    if filename in notes_db:
        raise HTTPException(status_code=400, detail="Note with this filename already exists.")

    # Create a timestamped note
    note = create_timestamped_note(filename, subject, other_info, content)
    notes_db[filename] = note

    return {"message": "Note created successfully", "note": note}

@app.get("/read_notes")
@log_decorator
def read_notes_api():
    # Return all notes
    return {"notes": list(notes_db.values())}

@app.put("/update_note")
@log_decorator
def update_note_api(data: dict):
    filename, content = data['filename'], data['content']

    if filename not in notes_db:
        raise HTTPException(status_code=404, detail="Note not found.")

    # Update note content and update timestamp
    note = notes_db[filename]
    note["content"] = content
    note["timestamp"] = datetime.now().isoformat()

    return {"message": "Note updated successfully", "note": note}

@app.delete("/delete_note")
@log_decorator
def delete_note_api(data: dict):
    filename = data['filename']

    if filename not in notes_db:
        raise HTTPException(status_code=404, detail="Note not found.")

    # Delete the note
    deleted_note = notes_db.pop(filename)

    return {"message": "Note deleted successfully", "deleted_note": deleted_note}

# Run the app
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
