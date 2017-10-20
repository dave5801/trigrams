import sys
import os.path



def open_file(file_path):
    new_content = {}

    if os.path.exists(file_path):
        return True
    else:
        return False
        
    

#open_file("sherlock_small.txt")
