from FileModificationHandler import FileModified
import json

def file_modified():
    print("FileModified")
    return False

fileModifiedHandler = FileModified(r"test.json",file_modified)
fileModifiedHandler.Start()


