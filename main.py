import os
from util.Util import Util
from mutagen.id3 import ID3, APIC, TIT2, TPE1

import tkinter
from tkinter import filedialog

def main(music_path):
    # Main function
    os.chdir(music_path)
    # get file names in the directory
    files_list = Util.get_files_list(path = music_path)
    # for each: get author and title 
    for filename in files_list:
        id3 = ID3(filename)
        
        author = Util.get_author_from_filename(filename = filename)
        title = Util.get_title_from_filename(filename = filename)
        
        # if author or title not found ask the user for manual input
        if(author is None):
            print('Author cannot be read from filename <<{filename}>>. Please input the author manually: '.format(filename=filename))
            if(author is None):
                author = Util.input_with_prefill('Author: ', '')
            
            title = Util.input_with_prefill('Title: ', Util.replace_all(filename))

        # if title in uppercase is needed
        # title = title.upper()
        if(Util.cover_exists(filepath=filename) is False):
            prompt_cover_needed = Util.input_with_prefill('Do you need a cover for <<{filename}>>? '.format(filename=filename),'yes')

            if(prompt_cover_needed.lower() == 'yes'):
                    
                tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
                cover_path = filedialog.askopenfilename()
                print('You have selected: {cover_path}'.format(cover_path=cover_path))
                imagedata = open(cover_path, 'rb').read()

                id3.add(APIC(3, 'image/png', 3, 'Front cover', imagedata))
                
        # use the library to populate mp3 tags   
        id3.add(TIT2(encoding=3, text=title))
        id3.add(TPE1(encoding=3, text=author))

        # done ... saving ...
        id3.save(v2_version=3)

        # rename the file to normalize file names
        new_filename = '{author} - {title}.mp3'.format(author=author, title=title)
        os.rename(filename, new_filename)
    pass

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Tool for automatic setting of artist and song title from file name. File names must be in the following format: {artist} - {title}.mp3 The tool will ask you for cover art path if none is present.')
    parser.add_argument('--path', metavar='path', required=True,
                        help='the workspace path where .mp3 files are stored')
    args = parser.parse_args()
    main(music_path = args.path)