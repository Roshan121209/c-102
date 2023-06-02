import os
import shutil

from_dir = "Downloads"
to_dir = "C:/Users/rosha/OneDrive/Desktop/downloded images"

list_of_files = os.listdir(from_dir)
for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    if (extension == ""):
        continue
    if (extension in[".gif", ".png", ".jpg", ".jpeg"]):
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "image files"
        path3 = to_dir + "/" + "image files" + "/" + file_name
        if (os.path.exists(path2)):
            print("moving")
            shutil.move(path1, path3)

        else:
            os.mkdir(path2)
            print("moving")
            shutil.move(path1, path2)