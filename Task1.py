import json
import yaml
import xmltodict
import os
import dicttoxml from dicttoxml

file_path = input("Proszę o podanie ścieżki pliku: ")
data = input("Proszę o podanie ścieżki pliku w jakim ma być zapisany wcześniej podany plik: ")
file_name, file_extension = os.path.splitext(file_path)
file_name_new, file_extension_new = os.path.splitext(data)

def checkfile():
    file = os.path.isfile(file_path)
    if file == False:
        print("Podana ścieżka pliku jest zła.")
        quit()
    else:
        print("Podana ścieżka pliku jest poprawna...")
    return file_path, data
