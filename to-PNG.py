import os
import glob
from os.path import exists
from heic2png import HEIC2PNG

files = os.listdir()

length = glob.glob(os.path.join('*.HEIC'))

if not os.path.exists(r'Output'):
    os.makedirs(r'Output')
    
def checkduplicate(filename: str) -> bool:
    decide = input('A file with the name ' + filename[:-5] + '.png already exists in the output directory, would you like to overwrite it [Y/N]?')
    if decide.lower() in {'yes', 'y'}: 
        decide = input('Are you sure? The file ' + filename[:-5] + '.png will be permanently deleted [Y/N]?')
        if decide.lower() in {'yes', 'y'}: return True
    return False

for i, file in enumerate(files):

    print(str(i) + str('/') + str(len(length)))

    if __name__ == '__main__' and file.endswith('.HEIC'):
        if exists('Output/' + file[:-5] + '.png'):
            Check = checkduplicate(file)
            if Check is True:
                os.remove('Output/' + file[:-5] + '.png')
            else: continue
        
        IMG = HEIC2PNG(file)
        IMG.save('Output/' + file[:-5] + '.png')