from pathlib import Path
import shutil
import sys
import file_parser as parser
import re

#Normalize-----------------------------------------------------
CYRILLIC = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "jo", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "ju", "ja", "je", "i", "ji", "g")
# Translate cyrillic into latin and changes all special symbols into '_'
TRANS = {}
for c, l in zip(CYRILLIC, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

def normalize(name: str) -> str:
    translate_name = name.translate(TRANS)
    translate_name = re.sub(r'(\W+!.)', '_', translate_name)
    return translate_name

# Making folders for archieves, mediafiles and other files---
def handle_media(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_other(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_archive(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    file_folder = target_folder / normalize(filename.name.replace(filename.suffix, ''))
    file_folder.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()), str(file_folder.resolve()))
    except shutil.ReadError:
        print(f'{filename} is not an archive!')
        file_folder.rmdir()
        return None
    filename.unlink()
# Deleting empty folders---------------------
def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Error deleting {folder}')

def main(folder: Path):
    parser.scan(folder)
    # Replace sorted files into folders-----------
    for file in parser.IMAGES:                                  
        handle_media(file, folder / 'images')         
    for file in parser.VIDEO:                                  
        handle_media(file, folder / 'video')            
    for file in parser.DOCUMENTS:                              
        handle_media(file, folder / 'documents')  
    for file in parser.MODELS:                                  
        handle_media(file, folder / 'models')    
    for file in parser.AUDIO:                              
        handle_media(file, folder / 'audio')            
    for file in parser.UNKNOWN_FILES:                          
        handle_other(file, folder / 'UNKNOWN_FILES') 
    # Replace archives with unzipping---------
    for file in parser.ARCHIVES:                               
        handle_archive(file, folder / 'archives') 
    # видаляємо порожні папки-------------------
    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)
# Start function--------------------------------        
def start_func():
    try:
        folder = sys.argv[1]
    except IndexError:
        print('Enter valid path to the folder')
    else:
        scan_folder = Path(folder)
        print(f'Start in folder {scan_folder.resolve()}')
        main(scan_folder.resolve())

# Entry point ------------------------
if __name__ == '__main__':
    start_func()
