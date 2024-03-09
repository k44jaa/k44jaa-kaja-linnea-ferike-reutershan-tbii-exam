from PIL import Image, ImageTk
import tkinter as tk


# this function sets the background image
def set_background(root, images_file_path, background_colour):

    # opening and resizing image
    img = Image.open(images_file_path)
    img = img.resize((550, 400), Image.LANCZOS)
    # converting to 'PhotoImage'
    photo = ImageTk.PhotoImage(img)
    # creating a label with the image set as its background + a background colour
    label = tk.Label(root, image=photo, bg=background_colour)
    label.image = photo
    # placing the image
    label.place(x=0, y=0, relwidth=1, relheight=1)


# this function will destroy any widgets previously created
def clear_widgets(root):

    for i in root.winfo_children():
        i.destroy()


# this function will add an exit button
def set_exit_button(root):

    # setting an exit button to exit the mvp at all times when needed
    exit_button = tk.Button(text="X",
                            font="Consolas 14",
                            command=root.destroy
                            )
    exit_button.pack(side="bottom", anchor='e')
    exit_button.place(relx=0.9,
                      rely=0.85)
