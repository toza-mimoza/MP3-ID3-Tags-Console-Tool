from dataclasses import replace
import os
from .exceptions import IllegalArgumentError
from mutagen import File
import readline


class Util:
    # correction list for info in file names
    replace_list = [
        '.mp3', 
        '(Audio)',
        '(TEKST)',
        '(HD)',
        '(Official Audio)', 
        '(Official Video)', 
        '[Official Video]',  
        '(Music Video)',
        '[Music Video]',
        '(Official Music Video)', 
        '[Official Music Video]', 
        '[Official Music video]',
        '[Remastered in 4K]', 
        '(Lyrics)',
        '(Lyrics Video)',
        '[Lyrics]',
        '(2010 Mix)',
        '(2011 Mix)',
        '(2012 Mix)',
        '(2013 Mix)',
        '(2014 Mix)',
        '(2015 Mix)',
        '(2016 Mix)',
        '(2017 Mix)',
        '(2018 Mix)',
        '(2019 Mix)',
        '(2020 Mix)',
        '(2021 Mix)',
        '(2022 Mix)',
        'Lyrics'
        ]

    @staticmethod
    def input_with_prefill(prompt, prefill):
        def hook():
            readline.insert_text(prefill)
            readline.redisplay()
        readline.set_pre_input_hook(hook)
        result = input(prompt)
        readline.set_pre_input_hook()
        return result
    @staticmethod
    def replace_all(string):
        result = string
        for r in Util.replace_list:
            result = result.replace(r,'').strip()
        return result
    @staticmethod
    def get_files_list(path):
        file_list = [f for f in os.listdir(path) if f.endswith('.mp3')]
        return file_list
    
    @staticmethod
    def _get_item_from_filename(filename, item_name):
        result = filename.split(' - ')

        # replace unneeded info with '' 
        for idx, item in enumerate(result):
            item = Util.replace_all(item)
            result[idx] = item

        if (item_name.lower() == 'author'):
            if (len(result) == 1):
                return None
            if (len(result) == 2):
                return result[0].strip()
        elif (item_name.lower() == 'title'):
            if (len(result) == 1):
                return result[0].strip()
            if (len(result) == 2):
                return result[1].strip()
        else: 
            raise IllegalArgumentError('Argument {arg} not compatible with this method'.format(arg = item_name))

    @staticmethod
    def get_author_from_filename(filename):
        return Util._get_item_from_filename(filename=filename, item_name='author')

    @staticmethod
    def get_title_from_filename(filename):
        return Util._get_item_from_filename(filename=filename, item_name='title')
    @staticmethod
    def cover_exists(filepath):
        audio = File(filepath)
        for k in audio.keys():
            if u'covr' in k or u'APIC' in k:
                return True

        return False