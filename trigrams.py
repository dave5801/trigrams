import sys
import os.path



def open_file(file_path):


    if os.path.exists(file_path):
        file = open(file_path, 'r')
        return file.read().lower().split()
    
        
    

print open_file("sherlock_small.txt")
