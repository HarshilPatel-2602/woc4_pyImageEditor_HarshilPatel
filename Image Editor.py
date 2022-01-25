
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import ImageTk, Image, ImageOps, ImageChops


root = Tk()
root.geometry("600x600")
root.title("Image Editor")

def open_file():
    global img1
    global img_show
    global img
    global filetypes, filename
    filetypes = (
        ('jpg files', '*.jpg'),
        ('png files', '*.png'),
        ('jpeg file','*.jpeg'),
        ('All files', '.')
    )
    filename = askopenfilename(title = "Select Image", filetypes = filetypes)
    img = Image.open(filename)
    img = img.resize((1722,1074))
    img1= ImageTk.PhotoImage(img)
    img_show = Label(root, image=img1)
    img_show.grid(row=1,column=0)
def save_file():
    new_img.save(filename)
    img=new_img
def SaveAs_file():
    global filename, filetypes, img
    filetypes = (
    ('jpg files', '*.jpg'),
    ('png files', '*.png'),
    ('jpeg file','*.jpeg'),
    ('All files', '.')
    )
    filename=asksaveasfilename(initialfile="Untitled.png",filetypes=filetypes)
    img.save(filename)
    img=Image.open(filename)
def vertical_flip():
    global img, im1, new_img, img_show
    new_img=ImageOps.flip(img)
    new_img.save("sample.png")
    img=Image.open("sample.png")
    im1=ImageTk.PhotoImage(img)
    img_show=Label(root,image=im1).grid(row=1,column=0)
def mirror_flip():
    global img, im1, new_img, img_show
    new_img=ImageOps.mirror(img)
    new_img.save("sample.png")
    img=Image.open("sample.png")
    im1=ImageTk.PhotoImage(img)
    img_show=Label(root,image=im1).grid(row=1,column=0)
def invert_colour():
    global img, im1, new_img, img_show
    new_img=ImageChops.invert(img)
    new_img.save("sample.png")
    img=Image.open("sample.png")
    im1=ImageTk.PhotoImage(img)
    img_show=Label(root,image=im1).grid(row=1,column=0)
def blackandwhite():
    global img, im1, new_img, img_show
    new_img=img.convert('L')
    new_img.save("sample.png")
    img=Image.open("sample.png")
    im1=ImageTk.PhotoImage(img)
    img_show=Label(root,image=im1).grid(row=1,column=0)
def original_image():
    global img, im1, new_img, img_show,filename
    new_img=Image.open(filename)
    new_img.save("sample.png")
    img=Image.open("sample.png")
    im1=ImageTk.PhotoImage(img)
    img_show=Label(root,image=im1).grid(row=1,column=0)
def rotate_left():
    global img, im1, new_img, img_show
    new_img=img.rotate(90)
    new_img.save("sample.png")
    img=Image.open("sample.png")
    im1=ImageTk.PhotoImage(img)
    img_show=Label(root,image=im1).grid(row=1,column=0)
def rotate_right():
    global img, im1, new_img, img_show
    new_img=img.rotate(-90)
    new_img.save("sample.png")
    img=Image.open("sample.png")
    im1=ImageTk.PhotoImage(img)
    img_show=Label(root,image=im1).grid(row=1,column=0)
my_menu=Menu(root) 
m1=Menu(my_menu)
m2=Menu(my_menu)
root.config(menu=my_menu )

m1.add_command(label="Open",command=open_file)
m1.add_command(label="Save",command=save_file)
m1.add_checkbutton(label="Auto Save",onvalue=0,)
m1.add_command(label="Save As",command=SaveAs_file)

my_menu.add_cascade(label="File",menu=m1)


m2.add_command(label="Vertical Flip", command=vertical_flip)
m2.add_command(label="Mirror Flip", command=mirror_flip)
m2.add_separator()
m2.add_command(label="Invert Colour", command=invert_colour)
m2.add_command(label="Black and White", command=blackandwhite)
m2.add_command(label="Original Image", command=original_image)
m2.add_separator()
m21=Menu(m2)
m2.add_cascade(label="Rotate", menu=m21)
m21.add_command(label="Rotate Left", command=rotate_left)
m21.add_command(label="Rotate Right",command=rotate_right)
my_menu.add_cascade(label="Edit",menu=m2)

root.mainloop() 