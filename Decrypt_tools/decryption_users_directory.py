#!/usr/bin/python
#coding:utf-8

from cryptography.fernet import Fernet
import os

file = open(input("Enter your key file location : "),"rb")
key = file.read()
file.close()

def filelist():
    mylist = []
    spec = "c:/users/"
    for root, dirs, files in os.walk(spec):
        for file in files:
            if file.endswith(".covid-19"):
                mylist.append(os.path.join(root, file))
    return mylist
print(filelist())

def file_decrypt(key, files):

    for name in files:
        if (name!="Ransom_decrypt.py"):
            with open(name, 'rb') as f:
                data = f.read()

            fernet = Fernet(key)
            decrypted = fernet.decrypt(data)
            decrypted_file = name.replace('.covid-19', '')
            try:
                with open(decrypted_file, 'wb') as f:
                    f.write(decrypted)
                    os.remove(name)
            except:
                continue

file_decrypt(key, filelist())
