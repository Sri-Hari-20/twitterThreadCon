import openpyxl
import os
import tweetThread as tt

def writeMode(path, url):
    fullPath = path
    for i in range(len(path) - 1, 0, -1):
        if(path[i]!='/'):
            path = path[:-1]
        else:
            break
    id = ""
    os.chdir(path)
    wb = openpyxl.Workbook()
    tweetReplyListItems, tweetReplyContentItems = tt.replyRet(url)
    if tweetReplyListItems is not None and tweetReplyContentItems is not None:
        for i in range(len(url)):
            if url[len(url) - i - 1] != '/':
                id = id + url[len(url) - i - 1]
            else:
                break
        id = id[::-1]
        if not os.path.exists(id):
            os.makedirs(id)
        idFile = id + ".xlsx"
        writeRow = ["URL", "Date Time", "Content"]
        writeSheet = wb.active
        writeSheet.append(writeRow)
        for i in range(1, len(tweetReplyListItems)):
            writeRow = []
            writeRow.append("https://www.twitter.com" + tweetReplyListItems[i]['href'])
            writeRow.append(tweetReplyListItems[i]['title'])
            writeRow.append(tweetReplyContentItems[i-1])
            writeSheet.append(writeRow)
        os.chdir(id)
        wb.save(idFile)
        os.chdir('..')
        print("Finished File: " + idFile)

if __name__ == "__main__":
    url = input("Enter an URL to generate the XLSX file of replies: ")
    path = os.getcwd()
    print(path)
    writeMode(path, url)
