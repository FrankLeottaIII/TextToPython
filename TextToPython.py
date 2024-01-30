#Author: Frank R. Leotta III

#Discription: This program will take all the Text files ().txt) in your folder and folders in your folders and turn each one into a python file (.py).
            #This will help you work on python files in a text editor on a computer that does not have python installed.

##Inports:
import glob #you need to install this modual before importing it.  Use pip install glob in the terminal.
import os


#psuedo code:
"""
make a list of all the text files in the folder
read 1 file in that list of files
create and write the contents of the text file into the python file
move on to the next file in the list
print a message when all files have been converted

"""
#code:

def ask_user_for_folder()->str:  
    """Summery:
    This funtion asks the user for the folder that they want to convert the python files into text files.
    
    Args:   
        none
        
    Returns:
        str: The folder that the user wants to convert the python files into text files.
    """
    folder = input("What folder do you want to convert the python files into text files? ")
    return folder


def search_every_folder_dirty(search_folder: str)->list:
    """Summary:
    This function makes a list of every folder in the search_folder directory (see arguments).
    It includes the search_folder itself and does not list the files, only the folders.  It is a dirty list, and must be cleaned before it can be used.
    Part 1 of 2 funtions, since the list has elements without a proper path, and must be filtered in the next funtion.
    
    Args:   
        search_folder (str): The folder to search in.
        
    Returns:
        list: A list of all the folders in the search_folder directory.
    """
    folders = []
    for folder_name, subfolders, _ in os.walk(search_folder):
        folders.append(folder_name)
        for subfolder in subfolders:
            folders.append(subfolder)
    return folders


def path_list_cleaner(unclean_list: list)->list:
    """Summary:
        A data cleaning funtion for lists that contain paths.  The funtion  filters out any elements in the list that do not contain "Users".  This filters out any elements that do not have a proper path.
        Part 2 of 2 funtions, the list filtration is done here.

    Warning: This funtion intended for computers running on Windows.  It may not work on other operating systems.

    Args:
        unclean_list (list): A list of all the folders in the search_folder directory.  

    Returns:
        list: A list that only contains proper paths for windows users.
    """
    filtered_folders = []
    for element in unclean_list:
        if "Users" in element:
            filtered_folders.append(element)
    return filtered_folders

def search_every_folder() -> list:
    """Summary:
    This function makes a list of every folder in the search_folder directory using 3 funtions:

    1.) ask_user_for_folder() to get the folder to search in.
    2.) search_every_folder_dirty() to make a list of every folder in the search_folder directory.
    3.) path_list_cleaner() to filter out any elements that do not have a proper path.

    Warning: This funtion intended for computers running on Windows.  It may not work on other operating systems.

    Args:
        none

    Returns:
        list: A list of all the folders in the folder the user is interested in.  The list is filtered to only contain proper paths for windows users

"""
    A_FOLDER = ask_user_for_folder()
    EVERY_FOLDER = search_every_folder_dirty(A_FOLDER)
    EVERY_FOLDER = path_list_cleaner(EVERY_FOLDER)
    return EVERY_FOLDER


#Note: will not work for a list of folders, only a single folder.  Basic code none the less for future use.

# def look_for_text_files_list(folder: str)->list:   
#     """Summery:
#     This funtion makes a list of all the python files in the folder.
    
#     Args:   
#         folder (str): The folder that the user wants to convert the text files into python files.
        
#     Returns:
#         list: A list of all the text files in the folder.
#     """
#     # import glob
#     text_files = glob.glob(folder + '/*.txt')
#     return text_files

def find_text_in_list(file_list: list) -> list:
    """Summary:
    This function sorts through the list of folders and makes a list of all the text (.txt) files in one combined list.

    Args:
        file_list (list): A list of all the different folders to find .txt files.

    Returns:
        list: A list of all the .txt files in the folder.
    """
    text_files = []
    for element in file_list:
        element = str(element)
        text_files.extend(glob.glob(element + '/*.txt'))
    return text_files


def next_file_to_convert(list_of_files: list)->str:
    """Summery:
    This funtion takes the next file to convert from the list of files.
    
    Args:   
        list_of_files (list): A list of all the python files in the folder.
        
    Returns:
        str: The name of the next file to convert.
    """
    next_file = list_of_files[0]
    return next_file


def remove_first(a_list: list)->list:
    """summery: removes the first element of a list.
    
    Args:
        a_list (list): a list of elements

    Returns:
        list: a list of elements with the first element removed
    
    """
    a_list.pop(0)
    return a_list


def py_to_txt_copy(file_name: str) -> str:
    """Summary:
    This function creates a copy of the python file into a text file.

    Args:
        file_name (str): The name of the python file that you want to convert into a text file.

    Returns:
        str: The name of the text file that was created.
    """
    with open(file_name, 'r') as text_file:
        text_code = text_file.read()
    python_file_name = file_name.replace('.txt', '.py')
    with open(python_file_name, 'w') as python_file:
        python_file.write(text_code)
    return python_file_name


def name_converted(the_list: list) -> str:
    """Summary:
    This function prints out the python file name without the file path attached to it. This function is used to let the user know what file has been converted.

    Args:
        the_list (list): A list of file paths.

    Returns:
        str: The name of the next Python file to convert.
    """
    file_path = the_list[0]
    file_name = file_path.split("/")[-1].split("\\")[-1]  # Extract file name
    return file_name 


def main():
    folders = search_every_folder()
    what_files_to_convert = find_text_in_list(folders)
    print("glob modual error, check your folder path and try again")
    what_files_to_convert = find_text_in_list(folders)
    while what_files_to_convert != []:
        next_file = next_file_to_convert(what_files_to_convert)
        py_to_txt_copy(next_file)
        text_file_name = name_converted(what_files_to_convert)
        print(f'{text_file_name} has been converted')
        remove_first(what_files_to_convert)
        if what_files_to_convert == []:
            print("All files have been converted")
    print("end of program")


if __name__ == "__main__":
    main()