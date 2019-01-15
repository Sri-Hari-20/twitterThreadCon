import openpyxl
import tweetThread as tt

def writeMode(url):
    id = ""
    wb = openpyxl.Workbook()
    tweetReplyListItems, tweetReplyContentItems = tt.replyRet(url)
    for i in range(len(url)):
        if url[len(url) - i - 1] != '/':
            id = id + url[len(url) - i - 1]
        else:
            break
    id = id[::-1]
    id = id + ".xlsx"
    writeRow = ["URL", "Date Time", "Content"]
    writeSheet = wb.active
    writeSheet.append(writeRow)
    for i in range(1, len(tweetReplyListItems)):
        writeRow = []
        writeRow.append("https://www.twitter.com" + tweetReplyListItems[i]['href'])
        writeRow.append(tweetReplyListItems[i]['title'])
        writeRow.append(tweetReplyContentItems[i-1])
        writeSheet.append(writeRow)

    wb.save(id)

if __name__ == "__main__":
    url = input("Enter an URL to generate the XLSX file of replies: ")
    writeMode(url)