import time
import glob
import os
import excelRead

path = os.getcwd()
fileList = glob.glob(path + '/**/*.xlsx', recursive = True)
completedList = []

for file in fileList:
    if file in fileList and file not in completedList:
        print("Sending file: " + file)
        excelRead.excelReader(file)
        print("File completed: " + file)
        completedList.append(file)
        fileList = glob.glob(path + '/**/*.xlsx', recursive = True)
