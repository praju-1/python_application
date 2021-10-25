#!usr/bin/env python3
# Python program to build Image viewer app using GUI tkinter

from tkinter import *
from PIL import ImageTk, Image

# Create functions to display previous and next images
def back(image_number):
    global mylabel
    global button_forward
    global button_back

    # disappear the last image from window
    mylabel.grid_forget()

    mylabel = Label(image=image_list[image_number - 1])
    button_forward = Button(window, text=" Next ", width=8, bg='black', fg='gold', font=('ariel 15 bold'),relief=GROOVE,command= lambda: forward(image_number+1))
    button_back = Button(window, text=" Previous ", width=8, bg='black', fg='gold', font=('ariel 15 bold'),relief=GROOVE,command= lambda : back(image_number -1))

    # disabled previous button 
    if image_number == 1:
        button_back = Button(window, text=" Previous ",  width=8, bg='black', fg='gold', font=('ariel 15 bold'),relief=GROOVE, state=DISABLED)

    # showing button on screen
    mylabel.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # update status bar
    status = Label(window, text="Image " + str(image_number) + " of " + str(len(image_list)),font=('ariel 12 bold'), bg="grey",  bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def forward(image_number):
    global mylabel
    global button_forward
    global button_back

    mylabel.grid_forget()
    mylabel = Label(image=image_list[image_number - 1])
    button_forward = Button(window, text= " Next ", width=8, bg='black', fg='gold', font=('ariel 15 bold'),relief=GROOVE, command= lambda: forward(image_number+1))
    button_back = Button(window, text=" Previous ",  width=8, bg='black', fg='gold', font=('ariel 15 bold'),relief=GROOVE,command= lambda : back(image_number-1))

    # disabled next button
    if image_number == 5:
        button_forward = Button(window, text=" Next ", width=8, bg='black', fg='gold', font=('ariel 15 bold'),relief=GROOVE, state=DISABLED)

    mylabel.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0, padx=60, pady=5)
    button_forward.grid(row=1, column=2, padx=60, pady=5)

    # update status bar
    status = Label(window, text="Image " + str(image_number) + " of " + str(len(image_list)), font=('ariel 12 bold'), bg="grey", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

# driver Code

if __name__ == "__main__":

    # creating GUI window
    window = Tk()

    # set Title for window
    window.title(" Image Viewer ")

    # keep window size fixed
    window.resizable(0, 0)

    # set background of window
    window.configure(bg="black")


# create thumbnails of all Images
my_img1 = Image.open("images/flower1.jpg")
my_img1.thumbnail((550, 500))

my_img2 = Image.open("images/flower2.jpg")
my_img2.thumbnail((550, 500))

my_img3 = Image.open("images/flower3.jpg")
my_img3.thumbnail((550, 500))

my_img4 = Image.open("images/flower4.jpg")
my_img4.thumbnail((550, 500))

my_img5 = Image.open("images/flower5.jpg")
my_img5.thumbnail((550, 500))


# open images to use with labels
image1 = ImageTk.PhotoImage(my_img1)
image2 = ImageTk.PhotoImage(my_img2)
image3 = ImageTk.PhotoImage(my_img3)
image4 = ImageTk.PhotoImage(my_img4)
image5 = ImageTk.PhotoImage(my_img5)

# create list of images
image_list = [image1, image2, image3, image4, image5]

# creating status bar
status = Label(window, text="Image 1 of " + str(len(image_list)),font=('ariel 12 bold'), bg="grey", bd=1, relief=SUNKEN, anchor=E)

# configure the image to the Label in frame
mylabel = Label(image=image1)
mylabel.grid(row=0, column=0, columnspan=3)

# create Buttons

button_back = Button(window, text="Previous", bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=back, state=DISABLED)
button_exit = Button(window, text="EXIT PROGRAM", width=12, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=window.quit)
button_forward = Button(window, text="Next", width=8, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=lambda:forward(2))

# show buttons on window

button_back.grid(row=1,column=0, padx=60, pady=5)
button_exit.grid(row=1, column=1, padx=60, pady=5)
button_forward.grid(row=1, column=2, padx=60, pady=5)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)


# keep window starting
window.mainloop()
