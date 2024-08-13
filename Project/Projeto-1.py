import os

def folderfiles(folder_path):
    try:
        # List all files in the directory
        files = os.listdir(folder_path)
        
        # Print each file in the directory
        print(f"Files in folder '{folder_path}':")
        for file in files:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                print(file)
    except OSError as e:
        print(f"Error: {e}")

def main():
    # Ask the user for the folder path
    folder_path = input("Enter the folder path: ")
    
    # Call the function to show files in the folder
    folderfiles(folder_path)

if __name__ == "__main__":
    main()