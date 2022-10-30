import sys
from pathlib import Path

IMAGES = []              #список
VIDEO = []               #список
DOCUMENTS = []           #список
MODELS = []              #список
AUDIO = []               #список
ARCHIVES = []            #список
UNKNOWN_FILES = []       #список

FOLDERS = []             #список
EXTENSIONS = set()       #множина
UNKNOWN = set()          #множина

REGISTER_EXTENSIONS = {
    'JPEG': IMAGES,
    'PNG': IMAGES,
    'JPG': IMAGES,
    'SVG': IMAGES,
    'AVI': VIDEO,
    'MP4': VIDEO,
    'MOV': VIDEO,
    'MKV': VIDEO,
    'DOC': DOCUMENTS,    
    'DOCX': DOCUMENTS,
    'TXT': DOCUMENTS,
    'PDF': DOCUMENTS,
    'XLS': DOCUMENTS,
    'XLSX': DOCUMENTS,
    'PPTX': DOCUMENTS,
    'SLDASM': MODELS,
    'SLDPRT': MODELS,
    'CATPART': MODELS,
    'CATPRODUCT': MODELS,
    'MP3': AUDIO,
    'OGG': AUDIO,
    'WAV': AUDIO,
    'AMR': AUDIO,
    'ZIP': ARCHIVES,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES
}

def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()

def scan(folder: Path) -> None:
    for item in folder.iterdir():
        # Робота з папкою-----------------------
        if item.is_dir():
            if item.name not in ('images', 'video', 'documents', 'models', 'audio', 'archives', 'unknown_files'):
                FOLDERS.append(item)
                scan(item)
            continue
        # Робота з файлом------------------------
        ext = get_extension(item.name) 
        fullname = folder / item.name
        if not ext: 
            UNKNOWN_FILES.append(fullname)
        else:
            try:
                box = REGISTER_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                box.append(fullname)
            except KeyError:
                UNKNOWN.add(ext)
                UNKNOWN_FILES.append(fullname)

if __name__ == '__main__':

    scan_folder = sys.argv[1]
    print(f'Start in folder {scan_folder}')

    scan(Path(scan_folder))
    print(f'Images jpeg, jpg, png, svg: {IMAGES}')      
    print(f'Videos avi, mp4, mov, mkv: {VIDEO}')         
    print(f'Documents doc, docx, txt, pdf, xls, xlsx, pptx: {DOCUMENTS}')       
    print(f'Models sldasm, sldprt, catpart, catproduct: {MODELS}')        
    print(f'Audio mp3, ogg, wav, amr: {AUDIO}')                          
    print(f'Archives: {ARCHIVES}')            
    print(f'Types of files in folder: {EXTENSIONS}')
    print(f'Unknown files of types: {UNKNOWN}')
    print(FOLDERS[::-1])
