 #!/usr/bin/python3
 
import os, os.path
from sys import argv


# returns the list of files and directories of the path
def get_dirlist(path="/home"):
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist


# It reads the font file and makes a copy of it in given location
def make_copy_font(old_filename, new_filename):
    font = open(old_filename, "br")
    new_font = open(new_filename, "bw")
    data = font.readlines()

    for row in data:
        new_font.write(row)

    font.close()
    new_font.close()


# returns the each and every list of files with fullpath of the current path
def return_all_file_path(path="/home"):
    fullpath_list = []
    if os.path.exists(path):
        dirlist = get_dirlist(path)
        for fd in dirlist:
            fullpath = os.path.join(path, fd)
            if os.path.isdir(fullpath):
                fullpath_list.extend(return_all_file_path(fullpath))
            else:
                fullpath_list.append(fullpath)
        return fullpath_list


# It searches for the files of given extension in given path
def search_files(file_name, path="/home"):
    print("Searching for any file with", file_name, "extension in", path, "directory.\n")
    files = []
    path_list = return_all_file_path(path)

    if path_list != None and len(path_list) != 0:
        path_list = sorted(path_list)
        for element in path_list:
            if element.endswith(file_name):
                print(element)
                files.append(element)

    print(f"Total:{len(files)}", file_name, "in", path)
    return files


# It removes all the files found by search files
def remove_files(file_name, path="/home", remove=False):
    files = search_files(file_name, path)
    if len(files) > 0 and remove:
        ask = input("\nDo you want to delete these files? [y/n] ")
        if ask.lower() == "y" or ask.lower() == "yes":
            print() # newline
            for element in files:
                print("removing", element)
                os.remove(element)
            print("Completed")


# It makes a copy of all the files found by search files into new directory
def copy_font(file_name, path="/home", copy=False):
    files = search_files(file_name, path)
    if len(files) > 0 and copy:
        new_directory = input("New directory: ")
        if not os.path.exists(new_directory):
            os.mkdir(new_directory)
        ask = input(f"\nDo you want to copy these files into {new_directory} ? [y/n] ")
        if ask.lower() == "yes" or ask.lower() == "y":
            print()
            for fontfile in files:
                old_filename = fontfile.split("/")[-1]
                new_filename = os.path.join(new_directory, old_filename)
                print("Copying", old_filename, "in", new_directory)
                make_copy_font(fontfile, new_filename)
            print("Completed")


if len(argv) == 3:
    search_files(argv[1], argv[2])
elif len(argv) == 4 and argv[3] == "rm":
    remove_files(argv[1], argv[2], True)
elif len(argv) == 4 and argv[3] == "cp":
    copy_font(argv[1], argv[2], True)
else:
    print("Usage: python files_finder.py file-extension filepath/directory [rm]")
    print("""
Search your file in the crowd of files in directory using your file extension.
Enter your file extension and your folder name and you can also use optional rm command to remove any unusual files.
    """)


# Search files using extension

