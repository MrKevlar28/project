import os 
import shutil
import time

def main():
    path = "C:/Users/radhi/Desktop/Python Projects/folder1"
    days = 30
    deletedFoldersCount = 0
    deletedFilesCount = 0
    seconds = time.time() - (days*24*60*60)
    if os.path.exists(path):
        for root_folder,folders,files in os.walk(path):
            if seconds > get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deletedFoldersCount = deletedFoldersCount + 1
            else:
                for folder in folders :
                    folder_path = os.path.join(root_folder,folder)
                    if seconds > get_file_or_folder_age(folder_path) :
                        remove_folder(folder_path)
                        deletedFoldersCount = deletedFoldersCount + 1
                for file in files :
                    file_path = os.path.join(root_folder,file)
                    if seconds > get_file_or_folder_age(file_path) :
                        remove_file(file_path)
                        deletedFilesCount = deletedFilesCount + 1
    
        else :
            if seconds > get_file_or_folder_age(path) :
                remove_file(path)
                deletedFilesCount = deletedFilesCount + 1
    
    else :
        print("Path not found")

    print(f"Total number of folders deleted : {deletedFoldersCount}")
    print(f"Total number of folders deleted : {deletedFilesCount}")


def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime

def remove_file(path):
    if not os.remove(path):
        print("Path is removed successfully")

    else:
        print("Unable to delete the path")

def remove_folder(path):
    if not shutil.rmtree(path):
        print("Path is removed successfully")

    else:
        print("Unable to delete the path")

if __name__ == '__main__':
    main()
    
    
