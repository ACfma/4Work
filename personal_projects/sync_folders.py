import os
import shutil
import logging

# Create a logger object
logger = logging.getLogger(__name__)

# Set the log level to INFO
logger.setLevel(logging.INFO)

# Create a file handler in the output folder
handler = logging.FileHandler('C:\\Users\\Andrea\\Downloads\\Prova_out\\file_update.log')

# Create a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger if not there
if not logger.hasHandlers():
    logger.addHandler(handler)

def update_files(source_folders, target_folder):
    # Dictionary to store the files being updated
    updating_files = {'Conflicts':[]}

    # First pass: Check for conflicts
    for source_folder in source_folders:
        # Walk through all files in the current source folder and its subfolders
        for dirpath, dirnames, filenames in os.walk(source_folder):
            for filename in filenames:
                source_file = os.path.join(dirpath, filename)
                target_file = os.path.join(target_folder, os.path.relpath(source_file, source_folder))
                
                # Get the modification time of the source file
                mtime = os.path.getmtime(source_file)
                
                # Check if the file is being updated in a different source folder
                if target_file in updating_files and updating_files[target_file] != mtime :
                    # Raise an error and log it
                    error = f'Conflict: {target_file} is being updated in multiple source folders with different modification times'
                    logger.error(error)
                    updating_files['Conflicts'].append(target_file)
                    
                
                # Store the modification time of the source file
                updating_files[target_file] = mtime

    # Second pass: Update the target folder
    for source_folder in source_folders:
        # Walk through all files in the current source folder and its subfolders
        for dirpath, dirnames, filenames in os.walk(source_folder):
            for filename in filenames:
                source_file = os.path.join(dirpath, filename)
                target_file = os.path.join(target_folder, os.path.relpath(source_file, source_folder))
                
                # Ensure the target directory exists
                os.makedirs(os.path.dirname(target_file), exist_ok=True)
                
                # Get the modification time of the source file
                mtime = os.path.getmtime(source_file)
                
                # Check if the file exists in the target folder
                if os.path.exists(target_file):
                    # Compare the modification times of the files
                    if mtime > os.path.getmtime(target_file) and target_file not in  updating_files['Conflicts']:
                        # If the source file is newer, replace the target file
                        shutil.copy2(source_file, target_file)
                        # Log the replacement
                        logger.info(f'Replaced {target_file} with {source_file}')
                else:
                    ##if you want to copy new files uncomment this, otherwise use pass
                    # If the file doesn't exist in the target folder, copy it
                    #shutil.copy2(source_file, target_file)
                    # Log the copy operation
                    #logger.info(f'Copied {source_file} to {target_file}')
                    ##
                    pass
    return

# Call the function with the source and target folders
if __name__ == "__main__":
    update_files(["C:\\Users\\Andrea\\Downloads\\Prova_in\\","C:\\Users\\Andrea\\Downloads\\Prova_in2\\"], "C:\\Users\\Andrea\\Downloads\\Prova_out\\")
