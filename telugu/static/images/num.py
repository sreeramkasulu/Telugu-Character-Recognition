from tkinter import *
from PIL import Image, ImageTk  # Importing from Pillow
import random

ws = Tk()
ws.title('PythonGuides')

# Set fullscreen mode
ws.attributes('-fullscreen', True)

# Get screen dimensions
screen_width = ws.winfo_screenwidth()
screen_height = ws.winfo_screenheight()

# Load and resize the background image using Pillow
bg_image = Image.open('background.png')  # Load the image
bg_image = bg_image.resize((screen_width, screen_height), Image.ANTIALIAS)  # Resize to match screen
bg_image_tk = ImageTk.PhotoImage(bg_image)  # Convert back to Tkinter-compatible image

# Adjust the canvas to match the full screen
canvas = Canvas(ws, width=screen_width, height=screen_height)
canvas.pack(fill='both', expand=True)

# Set the background image on the canvas
canvas.create_image(0, 0, image=bg_image_tk, anchor='nw')

ranNum = random.randint(1, 50)
chance = 5
var = IntVar()
msg = StringVar()

def check_guess():
    global ranNum
    global chance
    usr_ip = var.get()
    if chance > 0:
        if usr_ip == ranNum:
            msg.set(f'You won! The correct answer is {ranNum}.')
        elif usr_ip > ranNum:
            chance -= 1
            msg.set(f'{usr_ip} is greater. You have {chance} attempt left.')
        elif usr_ip < ranNum:
            chance -= 1
            msg.set(f'{usr_ip} is smaller. You have {chance} attempt left.')
        else:
            msg.set('Something went wrong!')
    else:
        msg.set(f'You Lost! The correct answer is {ranNum}. You have {chance} attempt left.')

# Create and place widgets on the canvas
label1 = Label(ws, text='Number Guessing Game', font=('sans-serif', 20), relief=SOLID, padx=10, pady=10, bg='#F27D16')
canvas.create_window(screen_width//2, 50, window=label1)  # Adjust the coordinates as needed

entry = Entry(ws, textvariable=var, font=('sans-serif', 18))
canvas.create_window(screen_width//2, screen_height//3, window=entry)

submit_button = Button(ws, text='Submit Guess', font=('sans-serif', 18), command=check_guess)
canvas.create_window(screen_width//2, screen_height//2, window=submit_button)

label2 = Label(ws, textvariable=msg, bg='#567146', font=('sans-serif', 14))
canvas.create_window(screen_width//2, screen_height//1.5, window=label2)

ws.mainloop()
