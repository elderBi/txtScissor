#This program was revised on May, 19th, 2019, being planned to launch on May, 21st, 2019.
#Version: 1.0
#Copyright: Luo Ziqian
'''README
	This program is for people who need to extract a certain part of a file in a regular way and only available to .txt 
	For instance: Using this program to process novels
'''
import re
import os
import winreg
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import tkinter.font
import cn2an


def textCopy(file, start, end, sourceEncoding, resultEncoding, window=lambda: generateWindow()):
    # try:
    with open(file, 'r', encoding=sourceEncoding) as f:
        string = f.read()
        try:
            result = re.search(pattern(string, start, end), string, re.DOTALL).group()
            outputFile = outputFileName(file, start, end)
            with open(outputFile, 'wb') as f:
                f.write(result.encode(resultEncoding))
            temp = tkinter.messagebox.askyesno(title="Success", message='File size: ' + str(getFileSize(outputFile)) + 'MB (:\n' + 'Open file?')
            if temp:
                os.system('notepad '+outputFile)
            else:
                window.quit()
        except AttributeError:
            temp = tkinter.messagebox.askretrycancel(title="Fail", message='The Clip does not exist! ):')
            if temp == False:
                window.quit()
    # except Exception as e:
    #     tkinter.messagebox.showerror(message='Error: ' + str(e))


def outputFileName(file, start, end):
    parts = file.split('/')
    parts[-1] = start + '-' + end + '_' + parts[-1]
    return '/'.join(parts)


def pattern(string, start, end):
    if end == '-1':  
        start, _start = combine(start), combine(cn2an.an2cn(int(start)))
        return '(({start})|({_start}))(.+)'.format(start = start, _start = _start)
    else:
        start, _start = combine(start), combine(cn2an.an2cn(int(start)))
        end, _end = combine(str(int(end)+1)), combine(cn2an.an2cn(int(end)+1))
        return '(({start})|({_start}))(.+?)(({end})|({_end}))'.format(start = start, _start = _start, end = end, _end = _end)
        

def combine(string):
    return '第' + string + '章'


def getFileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize / float(1024 * 1024)
    return round(fsize, 2)


def getDesktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return winreg.QueryValueEx(key, "Desktop")[0]


def selectFile(file):
    f = tkinter.filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(getDesktop())),
                                                   filetypes=[('text files', '.txt')])
    return file.set(f)


def generateWindow(title="", geometry="600x150"):
    window = tkinter.Tk()
    window.title(title)
    window.geometry(geometry)
    return window


def main():
    mainWindow = generateWindow(title="TXT Scissor", geometry="300x150")
    inputFile = tkinter.StringVar(mainWindow)
    startKey = tkinter.StringVar(mainWindow, value='1')
    endKey = tkinter.StringVar(mainWindow, value='-1')
    sourceEncoding = tkinter.StringVar(mainWindow, 'utf-8')
    resultEncoding = tkinter.StringVar(mainWindow, 'gbk')
    font = tkinter.font.Font(family='Arial', size=12, weight=tkinter.font.NORMAL)

    label1 = tkinter.Label(mainWindow, text='Initial Value: ', width=15, font=font)
    label2 = tkinter.Label(mainWindow, text='End Value: ', width=15, font=font)
    label3 = tkinter.Label(mainWindow, text='Source Encoding', width=15, font=font)
    label4 = tkinter.Label(mainWindow, text='Result Encoding', width=15, font=font)

    entry1 = tkinter.Entry(mainWindow, textvariable=startKey, width=15, font=font)
    entry2 = tkinter.Entry(mainWindow, textvariable=endKey, width=15, font=font)
    entry3 = tkinter.Entry(mainWindow, textvariable=sourceEncoding, width=15, font=font)
    entry4 = tkinter.Entry(mainWindow, textvariable=resultEncoding, width=15, font=font)

    selectButton = tkinter.Button(mainWindow, text=' Select ', command=lambda: selectFile(inputFile), width=10, font=font)
    startButton = tkinter.Button(mainWindow, text=' Start ', command=lambda: textCopy(inputFile.get(), startKey.get(),
                                                    endKey.get(), sourceEncoding.get(), resultEncoding.get(), mainWindow), width=10, font=font)

    label1.grid(row=0, column=0)
    entry1.grid(row=0, column=1)
    label2.grid(row=1, column=0)
    entry2.grid(row=1, column=1)
    label3.grid(row=2, column=0)
    entry3.grid(row=2, column=1)
    label4.grid(row=3, column=0)
    entry4.grid(row=3, column=1)
    selectButton.grid(row=4, column=0)
    startButton.grid(row=4, column=1)

    mainWindow.mainloop()
    
	
def test():
    textCopy('D:/Documents/Books/电子书/修真高手在校园.txt', '341', '442', 'utf-8', 'gbk')
    textCopy('D:/Documents/Books/电子书/三界淘宝店.txt', '1', '-1', 'utf-8', 'gbk')


if __name__ == '__main__':
    # test()
    main()
    








