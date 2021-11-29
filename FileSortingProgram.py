import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import *


# Create the program window
window = tk.Tk()
# Set the title of the window
window.title("File Sorting")
# Set the size of the window
window.geometry("300x100")
# Create a browse button
browse_button = Button(window, text="Browse", height=2, bg="cyan",
                       width=10, command=lambda: browse(window))
# Create a sort button
sort_button = Button(window, text="Sort", height=2, bg="orange",
                     width=10, command=lambda: sort(window))
# Create a label
label = Label(window, text="Directory:")
# Place Butonns on the bottom of the window and label on the top
sort_button.pack(side=BOTTOM)
browse_button.pack(side=BOTTOM)
label.pack(side=TOP)


# Pack the browse button
browse_button.pack()
# Pack the sort button
sort_button.pack()
# Pack the label
label.pack()
# Pack the text box


def browse(window):
    # Create a file dialog
    directory = os.path.dirname(os.path.realpath(filedialog.askopenfilename()))
    # Set the text of the label to the path of the file
    label.config(text=directory)


def sort(window):
    # Get the path from the label
    path = label.cget("text")
    # Sort the files
    sort_files(path)
    # Close the window
    window.destroy()


def sort_files(path):
    # Create a text file to write to on the directory
    text_file = open(path + "/Sorted_Files.txt", "w")
    # Create a dict to store files and their extensions
    extension_dict = {}
    # Iterate through the files in the folder
    for filename in os.listdir(path):
        # Extract the extension of the file
        extension = os.path.splitext(filename)[1]
        # Store the file in the dict
        if extension in extension_dict:
            extension_dict[extension].append(filename)
        else:
            extension_dict[extension] = [filename]
    # Create the folders
    for extension in extension_dict:
        try:
            os.mkdir(path + "/" + extension[1:])
        except FileExistsError:
            pass
    # Move the files to their respective folders
    for extension in extension_dict:
        for filename in extension_dict[extension]:
            # Skip the text file
            if filename == "Sorted_Files.txt":
                continue
            shutil.move(path + "/" + filename, path + "/" +
                        extension[1:] + "/" + filename)
            # Add the file and the directory it was moved to the text file
            text_file.write("Filename: " + filename + "\n" +
                            "Original Directory: " + path + "\n" +
                            "Moved Directory: " + path + "/" + extension[1:] + "\n\n")
    # Close the text file
    text_file.close()
    # Delete the empty folders
    for extension in extension_dict:
        if not os.listdir(path + "/" + extension[1:]):
            os.rmdir(path + "/" + extension[1:])
    # Delete the empty parent folder
    if not os.listdir(path):
        os.rmdir(path)
    # Open the text file
    os.startfile(path + "/Sorted_Files.txt")


# Start the main loop
window.mainloop()
