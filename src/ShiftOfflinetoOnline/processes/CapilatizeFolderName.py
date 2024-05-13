import os

def rename_folders(folder_path):
    folders = os.listdir(folder_path)

    for folder_name in folders:
        old_path = os.path.join(folder_path, folder_name)
        if os.path.isdir(old_path):
            new_folder_name = folder_name.replace('_', '').capitalize()
            new_folder_name = new_folder_name[:2].lower() + new_folder_name[2:].upper()
            new_path = os.path.join(folder_path, new_folder_name)
            os.rename(old_path, new_path)
            print(f'Renamed "{folder_name}" to "{new_folder_name}"')

if __name__ == "__main__":
    folder_path = input("Enter the path of the directory containing folders to rename: ")
    rename_folders(folder_path)
