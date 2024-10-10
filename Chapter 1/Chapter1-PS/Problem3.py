import os

def print_directory_contents(directory_path):
    try:
        # List all files and directories in the specified path
        with os.scandir(directory_path) as entries:
            for entry in entries:
                if entry.is_file():
                    print(f"File: {entry.name}")
                elif entry.is_dir():
                    print(f"Directory: {entry.name}")
    except FileNotFoundError:
        print(f"The directory {directory_path} does not exist.")
    except PermissionError:
        print(f"Permission denied to access {directory_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory_path = "/home/shtlp_0108/Documents/Python_Practice/Chapter 1"  # Change this to the path you want to inspect
print_directory_contents(directory_path)
