import os
from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk
#initalize main window
root = Tk()
root.title("Photogallery")

#Variables to hold images and current index
images = []
current_index = 0
 #select folder containing images
folder_path = filedialog.askdirectory(title="Select Folder with images")
if not folder_path:
    print("No folder selected.exiting...")
    root.destroy()
    exit()
for file_name in os.listdir(folder_path):
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        images.append(os.path.join(folder_path, file_name))
if not images:
    print("No images found in the selected folder:")
    root.destroy()
    exit()
img_label = Label(root)
img_label.pack()

#disolay first image
def update_image():
    global current_index, img_label
    img = Image.open(images[current_index])
    img.thumbnail((800, 600)) #resize to fit the window
    photo = ImageTk.PhotoImage(img)
    img_label.config(image=photo)
    img_label.image = photo
    root.title(f"photo gallery - {os.path.basename(images[current_index])}")

#Navigaton to previous image
def prev_image():
    global current_index
    if current_index > 0:
        current_index -= 1
        update_image()
def next_image():
    global current_index
    if current_index < len(images) - 1:
        current_index += 1
        update_image()
#add navigation buttons
prev_button = Button(root, text = "Previous", command = prev_image)
prev_button.pack(side="left", padx=35)

next_button = Button(root, text="Next", command=next_image)
next_button.pack(side="right", padx = 123)

#show the first image
update_image()

#Run the application
root.mainloop()