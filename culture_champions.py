import tkinter as tk
from tkinter import messagebox, ttk, CENTER, Canvas
from PIL import Image, ImageTk
import pandas as pd
from datetime import datetime
import webbrowser
import random

# importing functions from the 'helpers' file
from src.helpers import set_background, clear_widgets, set_exit_button


# executing tkinter and creating the main gui frame
root = tk.Tk()
root.title("Culture Champions")

# giving the frame my desired size
screen_width = 550
screen_height = 400

# using geometry here to position where the gui frame launches
root.geometry(f'{screen_width}x{screen_height}+500+150')


# creating a splash screen
splash_root = tk.Tk()
splash_root.title("Culture Champions")

# giving the screen a smaller size than the main one for visual purposes
screen_width = 500
screen_height = 400

# using geometry again to position where the frame launches
splash_root.geometry(f'{screen_width}x{screen_height}+500+150')

# setting a Label to initiate the mvp
splash_label = tk.Label(splash_root,
                        text="C u l t u r e    C h a m p i o n s    i s    l o a d i n g   . . . ",
                        font="Impact 16",
                        fg="#9ACD32"
                        )
splash_label.place(relx=0.09, rely=0.4)


# creating the main window function to make the main window visible
def main():
    # destroying the splash window
    splash_root.destroy()
    # showing the previously hidden main root
    root.deiconify()


# creating a setup function that will clear widgets and place a back-button when creating a new page
def new_page_setup():
    global root  # ensuring that root is accessed globally

    # clearing all the widgets that have been created
    clear_widgets(root)

    # adding a go-back-button that will go back to the account screen
    account = tk.Button(root,
                        text="←",
                        command=lambda: account_screen()
                        )
    account.pack(side=tk.BOTTOM)


# function for checking for an existing user before access to the mvp
def check_user():
    global root

    # reading all the usernames from the user_data.csv file
    user_ids = list(pd.read_csv("user_data/users_data.csv").user_id)

    # checking if the username exists - then proceed
    if username.get() in user_ids:
        tutorial_screen_one()
    # otherwise giving a warning message
    else:
        tk.messagebox.showwarning("WARNING", "User does not exist")


# creating a language selection screen to give the option of choosing preferred language
def language_selection_screen():
    global root

    # clearing all the widgets that have been created
    clear_widgets(root)

    # placing a background image using the set_background definition from the helpers file
    set_background(root, "images/language_selection_image.jpeg", background_colour="white")

    # creating different messages shown when selecting a language
    # listing matching languages with their messages
    language_messages = {
        "German": "Guten Tag und Hallo! Willkommen bei Culture Champions 🌍 "
                  "Wir freuen uns riesig, dass du dabei bist - "
                  "lass uns gemeinsam das Alltagsleben in einer neuen Kultur bewältigen...",
        "Chinese": "您好，欢迎来到文化冠军 🌍 我们很高兴您能加入我们 - 让我们一起了解新文化中的日常生活...",
        "English": "Greetings and Hello! Welcome to Culture Champions 🌍 "
                   "We're delighted that you' are joining us - "
                   "let's get to grips with everyday life in a new culture together...",
        "Arabic": "مرحباً ومرحباً بك في أبطال الثقافة 🌍 يسعدنا انضمامك إلينا"
                  " - دعنا نتعرف على الحياة اليومية في ثقافة جديدة معاً...",
        "Spanish": "Hola y bienvenido a Culture Champions 🌍 Estamos encantados de que te hayas unido a nosotros - "
                   "vamos a enfrentarnos juntos a la vida cotidiana en una nueva cultura...."
    }

    # creating a function to show a message for the selected language
    def show_language_message(selected_language):
        message = language_messages.get(selected_language, "No message available for this language.")
        messagebox.showinfo("Guten Tag - 你好 - Hello - مرحبا - Hola", message)

    # defining a function to handle the language selection
    def handle_language_selection(event):
        # getting the selected language from the combobox
        selected_language = combo.get()
        # showing the message for the selected language
        show_language_message(selected_language)

    # placing a button that will go to the account screen
    language_selection = tk.Button(root,
                                   text="continue",
                                   font="Consolas 14",
                                   command=lambda: account_screen()
                                   )
    language_selection.place(relx=0.4, rely=0.85)

    # creating a dropdown menu with a list of language options for the user - starting with the list
    value_list = ["German", "Chinese", "English",
                  "Arabic", "Spanish"]

    # placing a combobox widget (a dropdown menu) using the values from the value_list as options
    combo = ttk.Combobox(values=value_list)
    combo.set("Select a language")
    combo.pack(padx=5, pady=5)
    combo.place(relx=0.48, rely=0.2, anchor=CENTER)

    # binding the combobox selection event to the handle_language_selection function
    combo.bind("<<ComboboxSelected>>", handle_language_selection)

    # adding the exit button from the src helpers file
    set_exit_button(root)


# this function gives the option to log back in after having created an account previously
def login_user_screen():
    global root
    global username  # ensuring that the variable username is accessed globally

    # calling the setup function that will clear widgets and place a back-button
    new_page_setup()

    # placing a background image using the set_background definition from the helpers file
    set_background(root, "images/login_user_image.jpeg", background_colour="white")

    # creating a 'welcome back' label
    welcome_back_label = tk.Label(root,
                                  text="WELCOME TO CULTURE CHAMPIONS! - we are happy to have you back",
                                  font="Impact 15",
                                  fg="#008080",
                                  bg="#B0E0E6"
                                  )
    welcome_back_label.pack(side=tk.TOP, anchor=tk.CENTER)

    # asking for the username
    userid_label = tk.Label(root,
                            text="enter your username:",
                            font="Consolas 10",
                            fg="#008080",
                            bg="#FFFFE0"
                            )
    userid_label.place(x=50, y=150)

    # placing an entry box to enter the username
    username = tk.StringVar()
    username_box = tk.Entry(root,
                            textvariable=username,
                            fg="black",
                            bg="#FFDEAD"
                            )
    username_box.place(x=200, y=150)

    # adding a button to login
    login_button = tk.Button(root,
                             text="login",
                             font="Consolas 10",
                             command=lambda: check_user()
                             )
    login_button.place(x=225, y=200, anchor=tk.CENTER)

    # adding a go-back-button that will go back to the account screen
    account = tk.Button(root,
                        text="←",
                        command=lambda: account_screen()
                        )
    account.pack(side=tk.BOTTOM)

    set_exit_button(root)


# adding a function to capture & save the new users data in the user_data.csv file
def enter_user_data():

    # this will keep track of when the user registered
    current_timestamp = datetime.now()

    # creating a dictionary that stores the information when the user enters and a timestamp
    user_data = {
        "name_of_user": name.get(),
        "user_id": username.get(),
        "created_at": current_timestamp
    }

    # reading the list of existing user ids
    user_ids = list(pd.read_csv("user_data/users_data.csv").user_id)

    # making sure the user does not leave it empty
    if len(username.get()) == 0 and len(name.get()) == 0:
        messagebox.showerror('Error', 'Please enter a name and username!')
    elif len(name.get()) == 0:
        messagebox.showerror('Error', 'Please enter your name!')
    elif len(username.get()) == 0:
        messagebox.showerror('Error', 'Please enter a user name!')
    else:
        # if the username exists - printing a warning box
        if username.get() in user_ids:
            tk.messagebox.showwarning("WARNING!", "This username already exists")
        # otherwise writing the user_data to the .csv file - then moving onto the next page
        else:
            # converting the dictionary into a user_data frame
            user_data_df = pd.DataFrame([user_data])
            # writing to a csv file - to include future sets of user data, we set the mode to "append"
            # and the header to be "false"
            user_data_df.to_csv("user_data/users_data.csv", index=False, mode='a', header=False)

            # clearing the widgets and placing the homepage button
            new_page_setup()

            # placing a background image
            set_background(root, "images/background_new_user_image.jpeg", background_colour="white")

            # adding a 'thank you' label
            thank_you_label = tk.Label(root,
                                       text=f"Thank you {name.get().capitalize()}!",
                                       font=("Impact", 20),
                                       fg="#7B68EE",
                                       bg="#E6E6FA"
                                       )
            thank_you_label.pack(pady=40, side=tk.TOP, anchor=tk.CENTER)

            # placing a button to proceed to the tutorial
            go_tutorial_button = tk.Button(root,
                                           text="start the tutorial here →",
                                           font="Consolas 12",
                                           command=lambda: tutorial_screen_one()
                                           )
            go_tutorial_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

            set_exit_button(root)


# this function will open a screen for new users to register
def register_user_screen():
    global root
    global username, name  # accessing these variables on a global scale to store them in the user_data.csv file

    new_page_setup()

    # setting the background image
    set_background(root, "images/register_user_image.jpeg", background_colour="white")

    # creating a welcome label
    welcome_label = tk.Label(root,
                             text="WELCOME TO CULTURE CHAMPIONS! - we are happy you made it",
                             font="Impact 16",
                             fg="#B22222",
                             bg="#FFDAB9"
                             )
    welcome_label.pack(side=tk.TOP, anchor=tk.CENTER)

    # creating labels and entry boxes to get the users information
    # asking for the name of the user
    name_label = tk.Label(root,
                          text="enter your name:",
                          font="Consolas 10",
                          fg="#B22222",
                          bg="#FFFFE0"
                          )
    name_label.place(x=50, y=100)

    # placing an entry box for the user to put in their name
    name = tk.StringVar()
    name_box = tk.Entry(root,
                        textvariable=name,
                        font="Consolas 10",
                        fg="black",
                        bg="#FFDAB9"
                        )
    name_box.place(x=200, y=100)

    # asking for a username
    username_label = tk.Label(root,
                              text="create a username:",
                              font="Consolas 10",
                              fg="#B22222",
                              bg="#FFFFE0"
                              )
    username_label.place(x=50, y=150)

    # placing an entry box for the user to put in their username
    username = tk.StringVar()
    username_box = tk.Entry(root,
                            textvariable=username,
                            font="Consolas 10",
                            fg="black",
                            bg="#FFDAB9"
                            )
    username_box.place(x=200, y=150)

    # creating a button to store all the information
    enter_data = tk.Button(root,
                           text="submit info",
                           font="Consolas 10",
                           command=enter_user_data
                           )
    enter_data.place(x=200, y=200)

    set_exit_button(root)


# creating the initial account screen
def account_screen():
    global root

    # clearing the widgets
    clear_widgets(root)

    set_background(root, "images/culture_champions_image.jpeg", background_colour="white")

    # placing a button that will go to the register screen
    new_user = tk.Button(root,
                         text="new user",
                         font="Consolas 14",
                         command=lambda: register_user_screen()
                         )
    new_user.place(relx=0.05, rely=0.8)

    # placing a button that will go to the login screen
    returning_user = tk.Button(root,
                               text="returning user",
                               font="Consolas 14",
                               command=lambda: login_user_screen()
                               )
    returning_user.place(relx=0.33, rely=0.8)

    set_exit_button(root)


# creating the first tutorial screen of four
def tutorial_screen_one():
    global root

    clear_widgets(root)

    # adding an image to the screen
    image1 = Image.open("images/tutorial_one_image.png")

    # resizing the image
    resize_image = image1.resize((400, 300))
    img = ImageTk.PhotoImage(resize_image, Image.LANCZOS)

    # creating label and add resize image
    label1 = tk.Label(root, image=img)
    label1.place(x=275, y=170, anchor=tk.CENTER)
    label1.image = img

    # placing a button that will go back to the account screen
    account_selection = tk.Button(root,
                                  text="←",
                                  font="Consolas 14",
                                  command=lambda: account_screen()
                                  )
    account_selection.place(relx=0.2, rely=0.85)

    # placing a button that will go to the next tutorial screen
    tutorial_selection_2 = tk.Button(root,
                                     text="→",
                                     font="Consolas 14",
                                     command=lambda: tutorial_screen_two()
                                     )
    tutorial_selection_2.place(relx=0.25, rely=0.85)

    # creating four canvas objects - canvas used like a blank sheet where you can draw shapes, text, or images
    canvas1 = Canvas()
    canvas2 = Canvas()
    canvas3 = Canvas()
    canvas4 = Canvas()

    # using create_oval() method to draw an oval shape in black or white to show the tutorial process
    # the circle one is black when at tutorial one e.g. - white are the previous or upcoming
    canvas1.create_oval(12.5, 1.25, 25, 12.5, outline="black", fill="black")
    canvas1.pack(side="bottom", anchor='e')
    canvas1.place(relx=0.4,
                  rely=0.925
                  )
    canvas2.create_oval(12.5, 1.25, 25, 12.5, outline="black", fill="white")
    canvas2.pack(side="bottom", anchor='n')
    canvas2.place(relx=0.45,
                  rely=0.925
                  )
    canvas3.create_oval(12.5, 1.25, 25, 12.5, outline="black", fill="white")
    canvas3.pack(side="bottom", anchor='n')
    canvas3.place(relx=0.5,
                  rely=0.925
                  )
    canvas4.create_oval(12.5, 1.25, 25, 12.5, outline="black", fill="white")
    canvas4.pack(side="bottom", anchor='n')
    canvas4.place(relx=0.55,
                  rely=0.925
                  )

    set_exit_button(root)


def tutorial_screen_two():
    global root

    clear_widgets(root)

    image2 = Image.open("images/tutorial_two_image.png")

    resize_image = image2.resize((400, 300))
    img = ImageTk.PhotoImage(resize_image, Image.LANCZOS)

    label2 = tk.Label(root, image=img)
    label2.place(x=275, y=170, anchor=tk.CENTER)
    label2.image = img

    # placing a button that will go back to the last tutorial screen
    tutorial_selection_1 = tk.Button(root,
                                     text="←",
                                     font="Consolas 14",
                                     command=lambda: tutorial_screen_one()
                                     )
    tutorial_selection_1.place(relx=0.2, rely=0.85)

    # placing a button that will go to the next tutorial screen
    tutorial_selection_3 = tk.Button(root,
                                     text="→",
                                     font="Consolas 14",
                                     command=lambda: tutorial_screen_three()
                                     )
    tutorial_selection_3.place(relx=0.25, rely=0.85)

    canvas1 = Canvas()
    canvas2 = Canvas()
    canvas3 = Canvas()
    canvas4 = Canvas()

    canvas1.create_oval(12.5, 1.25, 25, 12.5, outline="black", fill="white")
    canvas1.pack(side="bottom", anchor='e')
    canvas1.place(relx=0.4,
                  rely=0.925
                  )
    canvas2.create_oval(12.5, 1.25, 25, 12.5, outline="black", fill="black")
    canvas2.pack(side="bottom", anchor='n')
    canvas2.place(relx=0.45,
                  rely=0.925
                  )
    canvas3.create_oval(12.5, 1.25, 25, 12.5, outline="black", fill="white")
    canvas3.pack(side="bottom", anchor='n')
    canvas3.place(relx=0.5,
                  rely=0.925
                  )
    canvas4.create_oval(12.5, 1.25, 25, 12.5, outline="black", fill="white")
    canvas4.pack(side="bottom", anchor='n')
    canvas4.place(relx=0.55,
                  rely=0.925
                  )

    set_exit_button(root)


def tutorial_screen_three():
    global root

    clear_widgets(root)

    image3 = Image.open("images/tutorial_three_image.png")

    resize_image = image3.resize((400, 300))
    img = ImageTk.PhotoImage(resize_image, Image.LANCZOS)

    label3 = tk.Label(root, image=img)
    label3.place(x=275, y=170, anchor=tk.CENTER)
    label3.image = img

    tutorial_selection_2 = tk.Button(root,
                                     text="←",
                                     font="Consolas 14",
                                     command=lambda: tutorial_screen_two()
                                     )
    tutorial_selection_2.place(relx=0.2, rely=0.85)

    tutorial_selection_4 = tk.Button(root,
                                     text="→",
                                     font="Consolas 14",
                                     command=lambda: tutorial_screen_four()
                                     )
    tutorial_selection_4.place(relx=0.25, rely=0.85)

    canvas1 = Canvas()
    canvas2 = Canvas()
    canvas3 = Canvas()
    canvas4 = Canvas()

    canvas1.create_oval(12.5, 1.25, 25, 12.5, outline="black", fill="white")
    canvas1.pack(side="bottom", anchor='e')
    canvas1.place(relx=0.4,
                  rely=0.925
                  )
    canvas2.create_oval(12.5, 1.25, 25, 12.5, outline="black", fill="white")
    canvas2.pack(side="bottom", anchor='n')
    canvas2.place(relx=0.45,
                  rely=0.925
                  )
    canvas3.create_oval(12.5, 1.25, 25, 12.5, outline="black", fill="black")
    canvas3.pack(side="bottom", anchor='n')
    canvas3.place(relx=0.5,
                  rely=0.925
                  )
    canvas4.create_oval(12.5, 1.25, 25, 12.5, outline="black", fill="white")
    canvas4.pack(side="bottom", anchor='n')
    canvas4.place(relx=0.55,
                  rely=0.925
                  )

    set_exit_button(root)


def tutorial_screen_four():
    global root

    clear_widgets(root)

    image4 = Image.open("images/tutorial_four_image.png")

    resize_image = image4.resize((400, 300))
    img = ImageTk.PhotoImage(resize_image, Image.LANCZOS)

    label4 = tk.Label(root, image=img)
    label4.place(x=275, y=170, anchor=tk.CENTER)
    label4.image = img

    tutorial_selection_3 = tk.Button(root,
                                     text="←",
                                     font="Consolas 14",
                                     command=lambda: tutorial_screen_three()
                                     )
    tutorial_selection_3.place(relx=0.2, rely=0.85)

    # adding a button that will go to the home screen
    home_screen_selection = tk.Button(root,
                                      text="→",
                                      font="Consolas 14",
                                      command=lambda: home_screen()
                                      )
    home_screen_selection.place(relx=0.25, rely=0.85)

    canvas1 = Canvas()
    canvas2 = Canvas()
    canvas3 = Canvas()
    canvas4 = Canvas()

    canvas1.create_oval(12.5, 1.25, 25, 12.5, outline="black", fill="white")
    canvas1.pack(side="bottom", anchor='e')
    canvas1.place(relx=0.4,
                  rely=0.925
                  )
    canvas2.create_oval(12.5, 1.25, 25, 12.5, outline="black", fill="white")
    canvas2.pack(side="bottom", anchor='n')
    canvas2.place(relx=0.45,
                  rely=0.925
                  )
    canvas3.create_oval(12.5, 1.25, 25, 12.5, outline="black", fill="white")
    canvas3.pack(side="bottom", anchor='n')
    canvas3.place(relx=0.5,
                  rely=0.925
                  )
    canvas4.create_oval(12.5, 1.25, 25, 12.5, outline="black", fill="black")
    canvas4.pack(side="bottom", anchor='n')
    canvas4.place(relx=0.55,
                  rely=0.925
                  )

    set_exit_button(root)


# this definition creates the home screen
def home_screen():
    global root

    clear_widgets(root)

    # setting a background image
    set_background(root, "images/homepage_background_image.jpeg", background_colour="white")

    # creating a welcoming label
    homepage_label = tk.Label(root,
                              text="Welcome to your homepage!",
                              font="Impact 15",
                              fg="#4f696a",
                              bg="#EEE8AA"
                              )
    homepage_label.pack(side=tk.TOP, anchor=tk.CENTER)

    # placing a button that will go to the first support screen - culture screen
    # loading an image to be placed on the button
    load = Image.open("images/culture_image.png")
    render = ImageTk.PhotoImage(load)

    # displaying the image in using a label
    img1 = tk.Label(image=render)
    img1.image = render  # keeping a reference to avoid it being seen as garbage in the garbage collection
    img1.place(x=450, y=280)

    # creating a button using a separate reference to the image
    # declaring the button_image as global
    global button_image

    # keeping a separate reference for the button image
    button_image = ImageTk.PhotoImage(load)
    # creating a button using the same image
    button1 = tk.Button(root, image=button_image,
                        command=culture_screen
                        )
    # setting a grid for placement
    button1.place(relx=0.05, rely=0.1)

    # repeating previous button creation for three additional buttons to be placed on the homepage
    # this is for the language screen button
    load = Image.open("images/language_image.png")
    render = ImageTk.PhotoImage(load)

    img2 = tk.Label(image=render)
    img2.image = render
    img2.place(x=450, y=280)

    global button_image2

    button_image2 = ImageTk.PhotoImage(load)
    button2 = tk.Button(root, image=button_image2,
                        command=language_screen
                        )
    button2.place(relx=0.45, rely=0.1)

    # repeating steps for the task screen button
    load = Image.open("images/tasks_image.png")
    render = ImageTk.PhotoImage(load)

    img3 = tk.Label(image=render)
    img3.image = render
    img3.place(x=450, y=280)

    global button_image3

    button_image3 = ImageTk.PhotoImage(load)
    button3 = tk.Button(root, image=button_image3,
                        command=task_screen
                        )
    button3.place(relx=0.45, rely=0.55)

    # last repetition for the paperwork screen button
    load = Image.open("images/paperwork_image.png")
    render = ImageTk.PhotoImage(load)

    img4 = tk.Label(image=render)
    img4.image = render
    img4.place(x=450, y=280)

    global button_image4

    button_image4 = ImageTk.PhotoImage(load)
    button4 = tk.Button(root, image=button_image4,
                        command=paperwork_screen
                        )
    button4.place(relx=0.05, rely=0.55)

    # using destroy() to destroy the image labels in order to only have them displayed on the buttons
    img1.destroy()
    img2.destroy()
    img3.destroy()
    img4.destroy()

    # placing a button that will go back to the first tutorial screen
    tutorial_selection = tk.Button(root,
                                   text="see tutorial",
                                   font="Consolas 10",
                                   command=lambda: tutorial_screen_one()
                                   )
    tutorial_selection.place(relx=0.25, rely=0.95, width=200, height=20)

    # placing a button that will go to the profile page
    profile_selection = tk.Button(root,
                                  text="👤",
                                  font="Consolas 14",
                                  command=lambda: profile_screen()
                                  )
    profile_selection.place(relx=0.9)

    # placing a button that will go to the donation page
    tutorial_selection = tk.Button(root,
                                   text="💸",
                                   font="Consolas 14",
                                   command=lambda: donation_screen()
                                   )
    tutorial_selection.place(relx=0.9, rely=0.2, width=25, height=260)

    set_exit_button(root)


# this definition creates the culture screen
def culture_screen():
    global root
    global name

    clear_widgets(root)

    # placing a background image
    set_background(root, "images/background_image_culture.jpeg", background_colour="white")

    # creating image paths to be linked to names that will randomly be picked on the screen
    # dictionary mapping image paths to associated words/ names
    image_word_map = {
        "images/professional_alex_image.jpg": "Alex",
        "images/professional_esra_image.jpg": "Esra",
        "images/professional_matteo_image.jpg": "Matteo"
    }

    # adding a list for the three images
    image_paths = list(image_word_map.keys())

    # selecting one image path randomly
    selected_image_path = random.choice(image_paths)

    # opening the selected image using PIL
    pil_image = Image.open(selected_image_path)

    # converting PIL image to a Tkinter-compatible image
    tk_image = ImageTk.PhotoImage(pil_image)

    # creating a label to display the image
    image_label = tk.Label(root, image=tk_image)
    image_label.image = tk_image
    image_label.place(relx=0.5,
                      rely=0.4,
                      anchor="center"
                      )

    # adding text that is to be displayed underneath the image
    text = f"Hi {name.get().capitalize()}! I am your assigned professional '{image_word_map[selected_image_path]}'. " \
           f"The Support Space Culture meets online on Zoom every Monday at 8:00 AM CET. The in-person meeting is " \
           f"scheduled for every first Wednesday of the month at 1:00 PM CET. Please contact me for the " \
           f"meeting code or further detail on the in-person meeting. We are looking forward to getting to know you!"

    # creating a label to display the text
    text_label = tk.Label(root,
                          text=text,
                          font="Consolas 7",
                          wraplength=150,
                          justify="center",
                          fg="black",
                          bg="white"
                          )
    text_label.place(relx=0.51, rely=0.77, anchor="center")

    # placing a 'welcome' label
    welcome_space_label = tk.Label(root,
                                   text="welcome to your support space:",
                                   font="Impact 15",
                                   fg="#CD5C5C",
                                   bg="#FFE4B5"
                                   )
    welcome_space_label.pack(side=tk.TOP, anchor=tk.CENTER)

    # placing another label for the area
    culture_label = tk.Label(root,
                             text="C U L T U R E",
                             font="Impact 18",
                             fg="#96ff00",
                             bg="white"
                             )
    culture_label.place(relx=0.4, rely=0.12)

    # placing a label for the group 'To-Do's'
    todo_label = tk.Label(root,
                          text="To-Do's",
                          font="Impact 15",
                          fg="#FF6347",
                          bg="#FFE4B5"
                          )
    todo_label.place(relx=0.1)

    # placing a label for the group 'Chat'
    chat_label = tk.Label(root,
                          text="Chat",
                          font="Impact 15",
                          fg="#FF6347",
                          bg="#FFE4B5"
                          )
    chat_label.place(relx=0.75)

    # placing check buttons for the to-do area
    # creating a variable for each check button to keep track of their states (checked or unchecked)
    var1 = tk.IntVar()
    var2 = tk.IntVar()
    var3 = tk.IntVar()
    var4 = tk.IntVar()
    var5 = tk.IntVar()

    # creating check buttons within the frame, each button is associated with a corresponding variable created earlier
    chk_btn = tk.Checkbutton(root,
                             width=15,
                             variable=var1,
                             bg="#FFA07A"
                             )
    chk_btn.place(anchor="w", rely=0.15)

    chk_btn2 = tk.Checkbutton(root,
                              width=15,
                              variable=var2,
                              bg="#FFA07A"
                              )
    chk_btn2.place(anchor="w", rely=0.3)

    chk_btn3 = tk.Checkbutton(root,
                              width=15,
                              variable=var3,
                              bg="#FFA07A"
                              )
    chk_btn3.place(anchor="w", rely=0.45)

    chk_btn4 = tk.Checkbutton(root,
                              width=15,
                              variable=var4,
                              bg="#FFA07A"
                              )
    chk_btn4.place(anchor="w", rely=0.6)

    chk_btn5 = tk.Checkbutton(root,
                              width=15,
                              variable=var5,
                              bg="#FFA07A"
                              )
    chk_btn5.place(anchor="w", rely=0.75)

    # adding chat boxes as text input fields where the user can type their 'to-do's'
    chat_box1 = tk.Entry(root,
                         font='Consolas 10'
                         )
    chat_box1.place(relx=0.15,
                    rely=0.14,
                    relwidth=0.2,
                    relheight=0.1
                    )

    chat_box2 = tk.Entry(root,
                         font='Consolas 10'
                         )
    chat_box2.place(relx=0.15,
                    rely=0.29,
                    relwidth=0.2,
                    relheight=0.1
                    )

    chat_box3 = tk.Entry(root,
                         font='Consolas 10'
                         )
    chat_box3.place(relx=0.15,
                    rely=0.44,
                    relwidth=0.2,
                    relheight=0.1
                    )

    chat_box4 = tk.Entry(root,
                         font='Consolas 10'
                         )
    chat_box4.place(relx=0.15,
                    rely=0.59,
                    relwidth=0.2,
                    relheight=0.1
                    )

    chat_box5 = tk.Entry(root,
                         font='Consolas 10'
                         )
    chat_box5.place(relx=0.15,
                    rely=0.74,
                    relwidth=0.2,
                    relheight=0.1
                    )

    # creating variables to format for the following chat option
    bg_colour = "#CD5C5C"
    text_colour = "#EAECEE"
    font = "Consolas 10"
    font_bold = "Impact 8"

    # creating a definition for a chatbot
    def send():
        # getting the user message and store it as a variable
        user_message = entry_box.get()

        # if the user enters a message
        if user_message:
            text_box.insert(tk.END, f"\nUser: {user_message}")
            # text_box.insert(tk.END, f"\nBot: {user_message}")
            text_box.insert(tk.END, "\n" + "Bot: Thank you for your message. "
                                           "You will receive an answer within approximately 72 hours.")
            # the chatbot self-destructs
            entry_box.destroy()
            send_button.destroy()

        # removing the text from the entry box
        entry_box.delete(0, tk.END)

    # creating the chatbot function
    def chatbot():
        global root
        global entry_box, send_button, text_box

    # adjusting the placement of the scrollbar
    scrollbar_width = 0.03
    scrollbar_spacing = 0.01

    # calculating the adjusted width of the text box
    text_box_width = (1 / 3) - (1 * scrollbar_width) - (1 * scrollbar_spacing)

    # creating the text box
    text_box = tk.Text(root,
                       bg=bg_colour,
                       fg=text_colour,
                       font=font,
                       width=60
                       )
    text_box.place(relx=(2/3),
                   rely=0.15,
                   relheight=0.75,
                   relwidth=text_box_width
                   )

    # adding an introductory message
    text_box.insert(tk.END,
                    "Bot: Please type your message below and your professional will contact you as soon as possible."
                    )

    # creating a scrollbar for the textbox
    scroll_bar = tk.Scrollbar(root)
    scroll_bar.place(relx=(2/3) + (1/3) - scrollbar_width - scrollbar_spacing,
                     rely=0.15,
                     relheight=0.75,
                     relwidth=scrollbar_width
                     )

    # linking the scrollbar to textbox
    scroll_bar.config(command=text_box.yview)
    text_box.config(yscrollcommand=scroll_bar.set)

    # calculating the adjusted width of the text box
    entry_box_width = (1 / 3) - (2.5 * scrollbar_width) - (2.5 * scrollbar_spacing)

    # creating an entry box for the user to enter a message and placing it
    entry_box = tk.Entry(root,
                         bg="#FF6347",
                         fg="white",
                         font=font,
                         width=55
                         )
    entry_box.place(relx=(2/3), rely=0.92, relwidth=entry_box_width)

    # creating a 'send' button
    send_button = tk.Button(root,
                            text="send",
                            font=font_bold,
                            bg="white",
                            command=send,
                            width=8)
    send_button.place(relx=(5.5/6), rely=0.92, relwidth=(0.5/6))

    # running the chatbot
    chatbot()

    # placing a button that will go back to the homepage
    home_screen_selection = tk.Button(root,
                                      text="🏠",
                                      font="Consolas 14",
                                      command=lambda: home_screen()
                                      )
    home_screen_selection.place(relx=0.05, rely=0.85)

    exit_button = tk.Button(text="X",
                            font="Consolas 14",
                            command=root.destroy
                            )
    exit_button.pack(side="top", anchor='e')
    exit_button.place(relx=0.9)


# this definition creates the language screen
def language_screen():
    global root
    global name

    clear_widgets(root)

    set_background(root, "images/background_image_language.jpeg", background_colour="white")

    # the following code section is a replica of the culture screen's - with adjusted content & colour palette
    image_word_map = {
        "images/professional_mei_image.jpg": "Mei",
        "images/professional_putri_image.jpg": "Putri",
        "images/professional_rafael_image.jpg": "Rafael"
    }

    image_paths = list(image_word_map.keys())
    selected_image_path = random.choice(image_paths)
    pil_image = Image.open(selected_image_path)
    tk_image = ImageTk.PhotoImage(pil_image)

    image_label = tk.Label(root, image=tk_image)
    image_label.image = tk_image
    image_label.place(relx=0.5,
                      rely=0.4,
                      anchor="center"
                      )

    text = f"Hi {name.get().capitalize()}! I am your assigned professional '{image_word_map[selected_image_path]}'. " \
           f"The Support Space Language meets online on Zoom every Wednesday at 10:00 AM CET. " \
           f"The in-person meeting is scheduled for every first Friday of the month at 4:00 PM CET. " \
           f"Please contact me for the meeting code or further detail on the in-person meeting. " \
           f"We are looking forward to getting to know you!"

    text_label = tk.Label(root,
                          text=text,
                          font="Consolas 7",
                          wraplength=150,
                          justify="center",
                          fg="black",
                          bg="white"
                          )
    text_label.place(relx=0.51, rely=0.77, anchor="center")

    welcome_space_label = tk.Label(root,
                                   text="welcome to your support space:",
                                   font="Impact 15",
                                   fg="#191970",
                                   bg="#ADD8E6"
                                   )
    welcome_space_label.pack(side=tk.TOP, anchor=tk.CENTER)

    language_label = tk.Label(root,
                              text="L A N G U A G E",
                              font="Impact 16",
                              fg="#00ffd1",
                              bg="white"
                              )
    language_label.place(relx=0.4, rely=0.12)

    todo_label = tk.Label(root,
                          text="To-Do's",
                          font="Impact 15",
                          fg="#4169E1",
                          bg="#ADD8E6"
                          )
    todo_label.place(relx=0.1)

    chat_label = tk.Label(root,
                          text="Chat",
                          font="Impact 15",
                          fg="#4169E1",
                          bg="#ADD8E6"
                          )
    chat_label.place(relx=0.75)

    var1 = tk.IntVar()
    var2 = tk.IntVar()
    var3 = tk.IntVar()
    var4 = tk.IntVar()
    var5 = tk.IntVar()

    chk_btn = tk.Checkbutton(root,
                             width=15,
                             variable=var1,
                             bg="#AFEEEE"
                             )
    chk_btn.place(anchor="w", rely=0.15)

    chk_btn2 = tk.Checkbutton(root,
                              width=15,
                              variable=var2,
                              bg="#AFEEEE"
                              )
    chk_btn2.place(anchor="w", rely=0.3)

    chk_btn3 = tk.Checkbutton(root,
                              width=15,
                              variable=var3,
                              bg="#AFEEEE"
                              )
    chk_btn3.place(anchor="w", rely=0.45)

    chk_btn4 = tk.Checkbutton(root,
                              width=15,
                              variable=var4,
                              bg="#AFEEEE"
                              )
    chk_btn4.place(anchor="w", rely=0.6)

    chk_btn5 = tk.Checkbutton(root,
                              width=15,
                              variable=var5,
                              bg="#AFEEEE"
                              )
    chk_btn5.place(anchor="w", rely=0.75)

    chat_box1 = tk.Entry(root,
                         font='Consolas 10'
                         )
    chat_box1.place(relx=0.15,
                    rely=0.14,
                    relwidth=0.2,
                    relheight=0.1
                    )

    chat_box2 = tk.Entry(root,
                         font='Consolas 10'
                         )
    chat_box2.place(relx=0.15,
                    rely=0.29,
                    relwidth=0.2,
                    relheight=0.1
                    )

    chat_box3 = tk.Entry(root,
                         font='Consolas 10'
                         )
    chat_box3.place(relx=0.15,
                    rely=0.44,
                    relwidth=0.2,
                    relheight=0.1
                    )

    chat_box4 = tk.Entry(root,
                         font='Consolas 10'
                         )
    chat_box4.place(relx=0.15,
                    rely=0.59,
                    relwidth=0.2,
                    relheight=0.1
                    )

    chat_box5 = tk.Entry(root,
                         font='Consolas 10'
                         )
    chat_box5.place(relx=0.15,
                    rely=0.74,
                    relwidth=0.2,
                    relheight=0.1
                    )

    bg_colour = "#4682B4"
    text_colour = "#EAECEE"
    font = "Consolas 10"
    font_bold = "Impact 8"

    def send():

        user_message = entry_box.get()

        if user_message:
            text_box.insert(tk.END, f"\nUser: {user_message}")
            text_box.insert(tk.END, "\n" + "Bot: Thank you for your message. "
                                           "You will receive an answer within approximately 72 hours.")
            entry_box.destroy()
            send_button.destroy()

        entry_box.delete(0, tk.END)

    def chatbot():
        global root
        global entry_box, send_button, text_box

    scrollbar_width = 0.03
    scrollbar_spacing = 0.01
    text_box_width = (1 / 3) - (1 * scrollbar_width) - (1 * scrollbar_spacing)

    text_box = tk.Text(root,
                       bg=bg_colour,
                       fg=text_colour,
                       font=font,
                       width=60
                       )

    text_box.place(relx=(2 / 3),
                   rely=0.15,
                   relheight=0.75,
                   relwidth=text_box_width
                   )

    text_box.insert(tk.END,
                    "Bot: Please type your message below and your professional will contact you as soon as possible."
                    )

    scroll_bar = tk.Scrollbar(root)
    scroll_bar.place(relx=(2 / 3) + (1 / 3) - scrollbar_width - scrollbar_spacing, rely=0.15, relheight=0.75,
                     relwidth=scrollbar_width)

    scroll_bar.config(command=text_box.yview)
    text_box.config(yscrollcommand=scroll_bar.set)

    entry_box_width = (1 / 3) - (2.5 * scrollbar_width) - (2.5 * scrollbar_spacing)

    entry_box = tk.Entry(root,
                         bg="#4169E1",
                         fg="white",
                         font=font,
                         width=55
                         )
    entry_box.place(relx=(2 / 3), rely=0.92, relwidth=entry_box_width)

    send_button = tk.Button(root,
                            text="send",
                            font=font_bold,
                            bg="white",
                            command=send,
                            width=8)
    send_button.place(relx=(5.5 / 6), rely=0.92, relwidth=(0.5 / 6))

    chatbot()

    home_screen_selection = tk.Button(root,
                                      text="🏠",
                                      font="Consolas 14",
                                      command=lambda: home_screen()
                                      )
    home_screen_selection.place(relx=0.05, rely=0.85)

    exit_button = tk.Button(text="X",
                            font="Consolas 14",
                            command=root.destroy
                            )
    exit_button.pack(side="top", anchor='e')
    exit_button.place(relx=0.9)


# this definition creates the paperwork screen
def paperwork_screen():
    global root
    global name

    clear_widgets(root)

    set_background(root, "images/background_image_paperwork.jpeg", background_colour="white")

    image_word_map = {
        "images/professional_sara_image.jpg": "Sara",
        "images/professional_sofia_image.jpg": "Sofia",
        "images/professional_thiago_image.jpg": "Thiago"
    }

    image_paths = list(image_word_map.keys())
    selected_image_path = random.choice(image_paths)
    pil_image = Image.open(selected_image_path)
    tk_image = ImageTk.PhotoImage(pil_image)

    image_label = tk.Label(root, image=tk_image)
    image_label.image = tk_image
    image_label.place(relx=0.5, rely=0.4, anchor="center")

    text = f"Hi {name.get().capitalize()}! I am your assigned professional '{image_word_map[selected_image_path]}'. " \
           f"The Support Space Paperwork meets online on Zoom every Tuesday at 11:00 AM CET. " \
           f"The in-person meeting is scheduled for every first Thursday of the month at 5:00 PM CET. " \
           f"Please contact me for the meeting code or further detail on the in-person meeting. " \
           f"We are looking forward to getting to know you!"

    text_label = tk.Label(root, text=text,
                          font="Consolas 7",
                          wraplength=150,
                          justify="center",
                          fg="black",
                          bg="white"
                          )
    text_label.place(relx=0.51, rely=0.77, anchor="center")

    welcome_space_label = tk.Label(root,
                                   text="welcome to your support space:",
                                   font="Impact 15",
                                   fg="#556B2F",
                                   bg="#EEE8AA"
                                   )
    welcome_space_label.pack(side=tk.TOP, anchor=tk.CENTER)

    paperwork_label = tk.Label(root,
                               text="P A P E R W O R K",
                               font="Impact 16",
                               fg="#d4ff00",
                               bg="white"
                               )
    paperwork_label.place(relx=0.38, rely=0.12)

    todo_label = tk.Label(root,
                          text="To-Do's",
                          font="Impact 15",
                          fg="#6B8E23",
                          bg="#EEE8AA"
                          )
    todo_label.place(relx=0.1)

    chat_label = tk.Label(root,
                          text="Chat",
                          font="Impact 15",
                          fg="#6B8E23",
                          bg="#EEE8AA"
                          )
    chat_label.place(relx=0.75)

    var1 = tk.IntVar()
    var2 = tk.IntVar()
    var3 = tk.IntVar()
    var4 = tk.IntVar()
    var5 = tk.IntVar()

    chk_btn = tk.Checkbutton(root,
                             width=15,
                             variable=var1,
                             bg="#8FBC8B"
                             )
    chk_btn.place(anchor="w", rely=0.15)

    chk_btn2 = tk.Checkbutton(root,
                              width=15,
                              variable=var2,
                              bg="#8FBC8B"
                              )
    chk_btn2.place(anchor="w", rely=0.3)

    chk_btn3 = tk.Checkbutton(root,
                              width=15,
                              variable=var3,
                              bg="#8FBC8B"
                              )
    chk_btn3.place(anchor="w", rely=0.45)

    chk_btn4 = tk.Checkbutton(root,
                              width=15,
                              variable=var4,
                              bg="#8FBC8B"
                              )
    chk_btn4.place(anchor="w", rely=0.6)

    chk_btn5 = tk.Checkbutton(root,
                              width=15,
                              variable=var5,
                              bg="#8FBC8B"
                              )
    chk_btn5.place(anchor="w", rely=0.75)

    chat_box1 = tk.Entry(root,
                         font='Consolas 10'
                         )
    chat_box1.place(relx=0.15,
                    rely=0.14,
                    relwidth=0.2,
                    relheight=0.1
                    )

    chat_box2 = tk.Entry(root,
                         font='Consolas 10'
                         )
    chat_box2.place(relx=0.15,
                    rely=0.29,
                    relwidth=0.2,
                    relheight=0.1
                    )

    chat_box3 = tk.Entry(root,
                         font='Consolas 10'
                         )
    chat_box3.place(relx=0.15,
                    rely=0.44,
                    relwidth=0.2,
                    relheight=0.1
                    )

    chat_box4 = tk.Entry(root,
                         font='Consolas 10'
                         )
    chat_box4.place(relx=0.15,
                    rely=0.59,
                    relwidth=0.2,
                    relheight=0.1
                    )

    chat_box5 = tk.Entry(root,
                         font='Consolas 10'
                         )
    chat_box5.place(relx=0.15,
                    rely=0.74,
                    relwidth=0.2,
                    relheight=0.1
                    )

    bg_colour = "#556B2F"
    text_colour = "#EAECEE"
    font = "Consolas 10"
    font_bold = "Impact 8"

    def send():
        user_message = entry_box.get()

        if user_message:
            text_box.insert(tk.END, f"\nUser: {user_message}")
            text_box.insert(tk.END, "\n" + "Bot: Thank you for your message. "
                                           "You will receive an answer within approximately 72 hours.")
            entry_box.destroy()
            send_button.destroy()

        entry_box.delete(0, tk.END)

    def chatbot():
        global root
        global entry_box, send_button, text_box

    scrollbar_width = 0.03
    scrollbar_spacing = 0.01
    text_box_width = (1 / 3) - (1 * scrollbar_width) - (1 * scrollbar_spacing)

    text_box = tk.Text(root,
                       bg=bg_colour,
                       fg=text_colour,
                       font=font,
                       width=60
                       )
    text_box.place(relx=(2 / 3),
                   rely=0.15,
                   relheight=0.75,
                   relwidth=text_box_width
                   )

    text_box.insert(tk.END,
                    "Bot: Please type your message below and your professional will contact you as soon as possible."
                    )

    scroll_bar = tk.Scrollbar(root)
    scroll_bar.place(relx=(2 / 3) + (1 / 3) - scrollbar_width - scrollbar_spacing,
                     rely=0.15,
                     relheight=0.75,
                     relwidth=scrollbar_width
                     )

    scroll_bar.config(command=text_box.yview)
    text_box.config(yscrollcommand=scroll_bar.set)

    entry_box_width = (1 / 3) - (2.5 * scrollbar_width) - (2.5 * scrollbar_spacing)

    entry_box = tk.Entry(root,
                         bg="#6B8E23",
                         fg="white",
                         font=font,
                         width=55
                         )
    entry_box.place(relx=(2 / 3),
                    rely=0.92,
                    relwidth=entry_box_width
                    )

    send_button = tk.Button(root,
                            text="send",
                            font=font_bold,
                            bg="white",
                            command=send,
                            width=8
                            )
    send_button.place(relx=(5.5 / 6), rely=0.92, relwidth=(0.5 / 6))

    chatbot()

    home_screen_selection = tk.Button(root,
                                      text="🏠",
                                      font="Consolas 14",
                                      command=lambda: home_screen()
                                      )
    home_screen_selection.place(relx=0.05, rely=0.85)

    exit_button = tk.Button(text="X",
                            font="Consolas 14",
                            command=root.destroy
                            )
    exit_button.pack(side="top", anchor='e')
    exit_button.place(relx=0.9)


# defining open doc to open a web browser with a specific URL
def open_doc():

    # the variable 'url' is assigned the value of the hyperlink
    url = "https://docs.google.com"
    # the variable 'new' is assigned to the value 1 - the web browser will open the URL in a new window
    new = 1
    # opening the assigned website link
    webbrowser.open(url, new=new)


# this definition creates the task screen
def task_screen():
    global root

    clear_widgets(root)

    set_background(root, "images/homepage_background_image.jpeg", background_colour="white")

    # create a welcome label
    welcome_space_label = tk.Label(root,
                                   text="Welcome to your Taskpage!",
                                   font="Impact 15",
                                   fg="#fa00ff",
                                   bg="white"
                                   )
    welcome_space_label.pack(side=tk.TOP, anchor=tk.CENTER, pady=60)

    # adding an informational text
    text = "These are your tasks for each learning area.        " \
           "Consult with your professional for advice."
    # creating a label to display the text
    text_label = tk.Label(root,
                          text=text,
                          font="Consolas 9",
                          wraplength=400,
                          justify="center",
                          fg="#A52A2A",
                          bg="#FFEFD5"
                          )
    text_label.place(relx=0.5, rely=0.6, anchor="center")

    # loading an image to connect to a button
    load = Image.open("images/culture_task_image.png")
    # resizing the image to a smaller size
    resized_image1 = load.resize((70, 70))
    # converting the resized image to PhotoImage
    render = ImageTk.PhotoImage(resized_image1)

    # creating a button using the resized image
    button1 = tk.Button(root,
                        text='Culture',
                        image=render,
                        font="Consolas 14",
                        command=open_doc
                        )
    # referencing the image to prevent garbage collection
    button1.image = render
    # placing the button on the screen
    button1.place(relx=0.23, rely=0.3)

    # loading another image to be managed the same way as the previous with adjusted image & placement
    load = Image.open("images/language_task_image.png")
    resized_image2 = load.resize((70, 70))
    render = ImageTk.PhotoImage(resized_image2)

    button2 = tk.Button(root,
                        text='Culture',
                        image=render,
                        font="Consolas 14",
                        command=open_doc
                        )
    button2.image = render
    button2.place(relx=0.43, rely=0.3)

    # loading another image to be managed the same way as the previous two with adjusted image & placement again
    load = Image.open("images/paperwork_task_image.png")
    resized_image3 = load.resize((70, 70))
    render = ImageTk.PhotoImage(resized_image3)

    button3 = tk.Button(root,
                        text='Culture',
                        image=render,
                        font="Consolas 14",
                        command=open_doc
                        )
    button3.image = render
    button3.place(relx=0.63, rely=0.3)

    home_screen_selection = tk.Button(root,
                                      text="🏠",
                                      font="Consolas 14",
                                      command=lambda: home_screen()
                                      )
    home_screen_selection.place(relx=0.12, rely=0.85)

    set_exit_button(root)


# cresting a function for the profile screen
def profile_screen():
    global root
    global username

    clear_widgets(root)

    set_background(root, "images/homepage_background_image.jpeg", background_colour="white")

    # adding an image for visual purposes
    profile_image = Image.open("images/profile_image.jpeg")
    # resizing the image
    resize_image = profile_image.resize((100, 100))
    img = ImageTk.PhotoImage(resize_image, Image.LANCZOS)

    # creating a label and adding the resized image
    profile_image_label = tk.Label(root, image=img)
    profile_image_label.place(x=25, y=70)
    profile_image_label.image = img

    # placing a label to welcome the user to the profile page
    welcome_profile_label = tk.Label(text=f"Welcome your Profile Page, {username.get()}!",
                                     font="Impact 15",
                                     fg="#008B8B",
                                     bg="#EEE8AA"
                                     )
    welcome_profile_label.place(relx=0.05)

    # adding an informational text
    text = f"You can add personal data below. All information is only visible to you and you assigned professional."
    # creating a label to display the text
    text_label = tk.Label(root, text=text,
                          font="Consolas 8",
                          wraplength=400,
                          justify="left",
                          fg="#F0FFFF",
                          bg="#008B8B"
                          )
    text_label.place(relx=0.05, rely=0.08, anchor="nw")

    # adding a labels for profile biography
    name_label = tk.Label(text="Name:",
                          font="Consolas 10",
                          bg="White",
                          fg="#008B8B"
                          )
    name_label.place(relx=0.05, rely=0.45)

    contact_label = tk.Label(text="Contact:",
                             font="Consolas 10",
                             bg="White",
                             fg="#008B8B"
                             )
    contact_label.place(relx=0.05, rely=0.55)

    about_label = tk.Label(text="About me:",
                           font="Consolas 10",
                           bg="White",
                           fg="#008B8B"
                           )
    about_label.place(relx=0.05, rely=0.65)

    languages_label = tk.Label(text="Languages I speak:",
                               font="Consolas 10",
                               bg="White",
                               fg="#008B8B"
                               )
    languages_label.place(relx=0.05, rely=0.75)

    # creating entry boxes for the answers entry
    chat_box1 = tk.Entry(root, font="Consolas 10", width=50)
    chat_box1.place(relx=0.15, rely=0.45)

    chat_box2 = tk.Entry(root, font="Consolas 10", width=48)
    chat_box2.place(relx=0.18, rely=0.55)

    chat_box3 = tk.Entry(root, font="Consolas 10", width=47)
    chat_box3.place(relx=0.195, rely=0.65)

    # adding the languages dropdown menus for selecting languages
    # creating a list with optional language values
    languages_list1 = ["English", "Mandarin", "Hindi",
                       "Spanish", "French", "Arabic", "Bengali", "Russian",
                       "Portuguese", "Urdu", "Indonesian", "German", "Japanese",
                       "Punjabi", "Wu"
                       ]

    # creating combo boxes - configured with the list and its height to accommodate the languages
    combo1 = ttk.Combobox(root, values=languages_list1, height=15)
    # setting the prompt
    combo1.set("1st Language")
    # placing the boxes within the screen
    combo1.pack(padx=4, pady=4)
    combo1.place(relx=0.3, rely=0.75)

    languages_list2 = ["English", "Mandarin", "Hindi",
                       "Spanish", "French", "Arabic", "Bengali", "Russian",
                       "Portuguese", "Urdu", "Indonesian", "German", "Japanese",
                       "Punjabi", "Wu"
                       ]

    combo2 = ttk.Combobox(root, values=languages_list2, height=15)
    combo2.set("2nd Language")
    combo2.pack(padx=4, pady=4)
    combo2.place(relx=0.3, rely=0.8)

    languages_list3 = ["English", "Mandarin", "Hindi",
                       "Spanish", "French", "Arabic", "Bengali", "Russian",
                       "Portuguese", "Urdu", "Indonesian", "German", "Japanese",
                       "Punjabi", "Wu"
                       ]

    combo3 = ttk.Combobox(root, values=languages_list3, height=15)
    combo3.set("3rd Language")
    combo3.pack(padx=4, pady=4)
    combo3.place(relx=0.3, rely=0.85)

    home_screen_selection = tk.Button(root,
                                      text="🏠",
                                      font="Consolas 14",
                                      command=lambda: home_screen()
                                      )
    home_screen_selection.place(relx=0.05, rely=0.85)

    set_exit_button(root)


# defining open web to open a web browser with a specific URL
def open_web():
    url = "https://www.paypal.com/home"
    new = 1
    webbrowser.open(url, new=new)


# creating the donation screen function
def donation_screen():
    global root
    global name

    clear_widgets(root)

    set_background(root, "images/homepage_background_image.jpeg", background_colour="white")

    # adding and placing an apprechiative label
    appreciation_label = tk.Label(root,
                                  text=f"Thank you for considering a donation {username.get()}!",
                                  font="Impact 15",
                                  fg="#20B2AA",
                                  bg="#EEE8AA"
                                  )
    appreciation_label.place(relx=0.15)

    # adding and placing an explanatory label
    explanation_label = tk.Label(root,
                                 text="We are a non-profit organisation, entirely based on donations.",
                                 font="Consolas 8",
                                 fg="white",
                                 bg="#F4A460"
                                 )
    explanation_label.place(relx=0.15, rely=0.1)

    # adding and placing a disclaimer label
    disclaimer_label = tk.Label(root,
                                text="See our disclaimer below for further information → ",
                                font="Consolas 8",
                                fg="white",
                                bg="#F4A460"
                                )
    disclaimer_label.place(relx=0.15, rely=0.15)

    # adding a friendly image
    donation_image = Image.open("images/donation_image.jpeg")
    # resizing the image
    resize_image = donation_image.resize((200, 200))
    img = ImageTk.PhotoImage(resize_image, Image.LANCZOS)

    # creating label and add resize image
    donation_label = tk.Label(root, image=img)
    donation_label.place(x=275, y=200, anchor=tk.CENTER)
    donation_label.image = img

    # placing a 'donate' button that opens the donation website
    donation_button = tk.Button(text="Donate",
                                font="Impact 14",
                                command=open_web
                                )
    donation_button.pack(side="bottom", anchor=tk.CENTER)
    donation_button.place(relx=0.43,
                          rely=0.8)

    # placing a file button that opens the disclaimers website
    disclaimer_button = tk.Button(root,
                                  text="📁",
                                  font="Consolas 12",
                                  command=open_doc
                                  )
    disclaimer_button.place(relx=0.75, rely=0.16)

    home_screen_selection = tk.Button(root,
                                      text="🏠",
                                      font="Consolas 14",
                                      command=lambda: home_screen()
                                      )
    home_screen_selection.place(relx=0.05, rely=0.85)

    set_exit_button(root)


# setting an interval to open first the splash screen and then the main root
splash_root.after(3000, main)
root.after(4000, language_selection_screen)

# hiding the main window until the splash screen is closed
root.withdraw()

# launching and running the gui
root.mainloop()
