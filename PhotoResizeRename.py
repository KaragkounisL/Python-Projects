from cryptography.fernet import Fernet
import base64


msg = b"""
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
from PIL import Image
gui = Tk()
gui.geometry("450x150")
gui.title("Image Resizer by Leonidas Karagkounis")


def getFolderPath():
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)


def resize(img, new_width):
    width, height = img.size
    ratio = height / width
    new_height = int(ratio*new_width)
    resized_image = img.resize((new_width, new_height))
    return resized_image


def resizeImages():
    message.set("Resizing Images...")
    folder = folderPath.get()
    # JPG
    images_jpg = [file for file in os.listdir(
        folder) if file.endswith(('jpg'))]
    for image in images_jpg:
        img = Image.open(folder+"/"+image)
        f, e = os.path.splitext(folder+"/"+image)
        img_resize = resize(img, 1400)
        img_resize.save(f+".jpg", 'JPEG', quality=100)
    # JPEG
    images_jpeg = [file for file in os.listdir(
        folder) if file.endswith(('jpeg'))]
    for image in images_jpeg:
        img = Image.open(folder+"/"+image)
        f, e = os.path.splitext(folder+"/"+image)
        img_resize = resize(img, 1400)
        img_resize.save(f+".jpeg", 'JPEG', quality=100)
    # PNG
    images_png = [file for file in os.listdir(
        folder) if file.endswith(('png'))]
    for image in images_png:
        img = Image.open(folder+"/"+image)
        f, e = os.path.splitext(folder+"/"+image)
        img_resize = resize(img, 1400)
        img_resize.save(f+".png", 'PNG', quality=100)
    message.set("Resizing Complete! Close the Program")


def renameImages():
    message.set("Renaming Images...")
    folder = folderPath.get()
    counter = 1
    images = [file for file in os.listdir(
        folder) if file.endswith(('jpeg', 'png', 'jpg'))]
    for image in images:
        new = str(counter).zfill(2)
        if image.endswith('jpg'):
            new = new + ".jpg"
        elif image.endswith('png'):
            new = new + ".png"
        elif image.endswith('jpeg'):
            new = new + ".jpeg"
        print(folder, new)
        src = os.path.join(folder, image)
        dst = os.path.join(folder, new)
        os.rename(src, dst)
        counter += 1
    message.set("Renaming Complete!")


folderPath = StringVar()
message = StringVar()
a = Label(gui, text="Select a folder")
a.grid(row=0, column=0)
E = Entry(gui, textvariable=folderPath, width=50)
E.grid(row=1, column=0, ipady=5)
btnFind = ttk.Button(gui, text="Browse Folder", command=getFolderPath)
btnFind.grid(row=1, column=1)
k = Label(gui, text="Resize to 1400px width maintaining aspect ratio")
k.grid(row=3, column=0)
b = Entry(gui, state='disabled', textvariable=message, width=50)
b.grid(row=4, column=0, ipady=10)
c = ttk.Button(gui, text="Resize", command=resizeImages)
c.grid(row=5, column=1)
d = ttk.Button(gui, text="Rename", command=renameImages)
d.grid(row=5, column=0)

gui.mainloop()
"""

key = Fernet.generate_key()
encryption_type = Fernet(key)
encrypted_message = encryption_type.encrypt(msg)

decrypted_message = encryption_type.decrypt(encrypted_message)
exec(decrypted_message)
