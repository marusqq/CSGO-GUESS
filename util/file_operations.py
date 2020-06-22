#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
'''random file operations'''

import json
import util.pretty_json as json_beautify
import os
import sys

def get_script_location():
    return os.getcwd()

def construct_full_path(path, filename):
    '''constructs full path'''
    try:
        if path is not None:
            fullpath = path + '/' + filename
        else:
            fullpath = filename
        return fullpath
    except:
        e = sys.exc_info()
        print('Unknown exception at [construct_full_path]:', e)
        quit()
    
def load_json(path, filename):
    '''loads json in designated path/filename
    and returns data in dict'''

    fullpath = construct_full_path(path=path, filename=filename)
    try:
        with open(fullpath) as f:
            data = json.load(f)
        return data
    except:
        e = sys.exc_info()
        print('Unknown exception at [load_json]:', e)
        quit()

def add_to_json(json, add, name):
    '''adds a new element to json
    @json - json to add to
    @add - string / int to add to json
    @name - id of @add in @json'''
    try:
        json[name] = add
        return json
    except:
        e = sys.exc_info()
        print('Unknown exception at [add_to_json]:', e)
        quit()

def delete_file(path, filename):
    '''deletes file at designated path and filename
        returns True'''

    fullpath = construct_full_path(path=path, filename=filename)
    if os.path.exists(fullpath):
        try:
            os.remove(fullpath)
            print('File:', fullpath, 'deleted!')
            return True

        except:
            e = sys.exc_info()
            print('Unknown exception at [delete_file]:', e)
            quit()

    else:
        print("delete_file didn't find any file at", fullpath) 
        return False

def output_json_to_file(json_data, path, filename):
    '''outputs json to a file'''
    fullpath = construct_full_path(path=path, filename=filename)
    try:
        with open(fullpath, "w") as write_file:
            json_output = json_beautify.prettyjson(json_data, indent=2, maxlinelength=50)
            write_file.write(json_output)
    except:
        e = sys.exc_info()
        print('Unknown exception at [output_json_to_file]:', e)
        quit()

def check_if_file_exists(path, filename):
    '''basic file existance check'''
    fullpath = construct_full_path(path=path, filename=filename)
    if os.path.exists(fullpath):
        return True
    else:
        return False
