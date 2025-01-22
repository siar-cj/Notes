import tkinter as tk
from PIL import ImageTk, Image
from tkinter import PhotoImage
import os
import logger as l

@l.log_decorator
def loading_screen(root):
    splash_screen = tk.Toplevel(root)
    splash_screen.title("Loading...")
    splash_screen.wm_attributes('-topmost', True)  # Ensures splash screen appears on top
    splash_screen.overrideredirect(True)  # Removes window decorations

    # Get screen width and height
    screen_width = splash_screen.winfo_screenwidth()
    screen_height = splash_screen.winfo_screenheight()

    # Set splash screen width and height
    splash_width = 1112
    splash_height = 625

    # Calculate center position
    x = (screen_width // 2) - (splash_width // 2)
    y = (screen_height // 2) - (splash_height // 2)

    splash_screen.geometry(f"{splash_width}x{splash_height}+{x}+{y}")

    bg_image = ImageTk.PhotoImage(Image.open("loading screen bg.jpg"))
    bg_label = tk.Label(splash_screen, image=bg_image)
    bg_label.image = bg_image  # Keep a reference to the image
    bg_label.place(x=0, y=0, width=1112, height=625)

    button_image = ImageTk.PhotoImage(Image.open("launch button.jpg"))
    button = tk.Button(splash_screen, image=button_image, bd=0, relief=tk.FLAT, highlightthickness=0,
                       command=lambda: show_main_screen(root,splash_screen))  # adding the button in the center of screen and giving it a image
    button.image = button_image  # Keep a reference to the image
    button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

@l.log_decorator
def show_main_screen(root, splash_screen):
    global delete_photo
    splash_screen.destroy()

    mroot = tk.Toplevel(root)
    mroot.title('BYDPP Notes')
    screen_width = mroot.winfo_screenwidth()
    screen_height = mroot.winfo_screenheight()

    # Set main screen width and height
    mroot.geometry(f"{screen_width}x{screen_height}")

    # Function to toggle full-screen
    def toggle_fullscreen(event=None):
        mroot.attributes("-fullscreen", not mroot.attributes("-fullscreen"))
        mroot.state("zoomed")

    # Bind the F11 key to toggle fullscreen
    mroot.bind("<F11>", toggle_fullscreen)

    # Set the background color to peach
    mroot.configure(bg="#FBFDAD")

    # Add your main screen widgets and functionality here
    img = Image.open("delete.png")
    img_resized = img.resize((150, 150), Image.LANCZOS)
    delete_image = ImageTk.PhotoImage(img_resized)

    delete_button = tk.Label(mroot, image=delete_image, bd=0,
                             width=delete_image.width(),
                             height=delete_image.height(),
                             highlightthickness=0, command=None)
    delete_button.image = delete_image
    delete_button.place(relx=0.05, rely=0.9, anchor=tk.SW)
    delete_button.config(borderwidth=0, relief=tk.FLAT, highlightthickness=0, bg="#FBFDAD",
                         highlightbackground="#FBFDAD", highlightcolor="#FBFDAD", bd=0)

    img = Image.open("add.png")
    img_resized = img.resize((150, 150), Image.LANCZOS)
    add_image = ImageTk.PhotoImage(img_resized)

    add_button = tk.Label(mroot, image=add_image, bd=0,
                          width=add_image.width(),
                          height=add_image.height(),
                          highlightthickness=0, command=None)
    add_button.image = add_image
    add_button.place(relx=0.05, rely=0.75, anchor=tk.SW)
    add_button.config(borderwidth=0, relief=tk.FLAT, highlightthickness=0, bg="#FBFDAD",
                      highlightbackground="#FBFDAD", highlightcolor="#FBFDAD", bd=0)

    img = Image.open("edit.png")
    img_resized = img.resize((150, 150), Image.LANCZOS)
    edit_image = ImageTk.PhotoImage(img_resized)

    edit_button = tk.Label(mroot, image=edit_image, bd=0,
                           width=edit_image.width(),
                           height=edit_image.height(),
                           highlightthickness=0, command=None)
    edit_button.image = edit_image
    edit_button.place(relx=0.05, rely=0.6, anchor=tk.SW)
    edit_button.config(borderwidth=0, relief=tk.FLAT, highlightthickness=0, bg="#FBFDAD",
                       highlightbackground="#FBFDAD", highlightcolor="#FBFDAD", bd=0)

    img = Image.open("read.png")  # Change the image file name to "read.png"
    img_resized = img.resize((150, 150), Image.LANCZOS)
    read_image = ImageTk.PhotoImage(img_resized)  # Rename edit_image to read_image

    read_button = tk.Label(mroot, image=read_image, bd=0,
                           width=read_image.width(),
                           height=read_image.height(),
                           highlightthickness=0, command=None)  # Rename edit_button to read_button
    read_button.image = read_image
    read_button.place(relx=0.05, rely=0.45, anchor=tk.SW)
    read_button.config(borderwidth=0, relief=tk.FLAT, highlightthickness=0, bg="#FBFDAD",
                       highlightbackground="#FBFDAD", highlightcolor="#FBFDAD", bd=0)

@l.log_decorator
def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main root window

    loading_screen(root)

    root.mainloop()

if __name__ == "__main__":
    main()
