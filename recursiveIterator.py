import time
import glob
import os
import excelRead

path = os.getcwd()
fileList = glob.glob(path + '/**/*.xlsx', recursive = True)
completedList = []

for file in fileList:
    if file in fileList and file not in completedList:
        time.sleep(10)
        excelRead.excelReader(file)
        print("File completed: " + path)
        completedList.append(file)
        fileList = glob.glob(path + '/**/*.xlsx', recursive = True)
