import re, os
import tkinter, tkinter.filedialog, tkinter.messagebox, tkinter.font
import cn2an
from functions import fileOperations, read, write


def getOutputFile(file, start, end):
    parts = file.split('/') #split apart 
    parts[-1] = start + '-' + end + '_' + parts[-1] #change the last part of a file path
    return '/'.join(parts) #rejoin them


def selectFile(file):
    f = tkinter.filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(fileOperations.getDesktop())))
    return file.set(f)


#copy file
def combine(string):
    return '第' + string + '章'


def duplicate(string): #convert to different expressions
    return combine(string), combine(cn2an.an2cn(int(string)))


def pattern(string, start, end): #assign a proper pattern
    if end == '-1':  
        start, _start = duplicate(start)
        return '(({start})|({_start}))(.+)'.format(start = start, _start = _start)
    else:
        start, _start = duplicate(start)
        end, _end = duplicate(str(int(end) + 1))
        return '(({start})|({_start}))(.+?)(({end})|({_end}))'.format(start = start, _start = _start, end = end, _end = _end)


def textCopy(file, start, end, window):
    try:
        form = fileOperations.getForm(file) #get the form of the document
        content = read.read(file, form) #get content
        try:
            reExp = pattern(content, start, end) #get regular expression
            result = re.search(reExp, content, re.DOTALL).group() #get the processed content
            outputFile = getOutputFile(file, start, end)
            write.write(outputFile, result, form) #write processed content into the output file
            temp = tkinter.messagebox.askyesno(title="Success", message='File size: ' + str(fileOperations.getFileSize(outputFile)) + 'MB (:\nContinue?') #try to ask a further question
            if not temp:
                window.quit() #quit the program
        except AttributeError: #if the content is None, a messagebox will be poped
            temp = tkinter.messagebox.askretrycancel(title="Fail", message='The Clip does not exist! ):') 
            if not temp:
                window.quit()
    except Exception as e: #show the errors
        tkinter.messagebox.showerror(message='Error: ' + str(e))


#GUI
def generateWindow(title="", geometry="600x150"): #produce a window
    window = tkinter.Tk()
    window.title(title)
    window.geometry(geometry)
    return window


def main():
    mainWindow = generateWindow(title="TXT Scissor", geometry="300x90")
    #some variables
    file = tkinter.StringVar(mainWindow)
    start = tkinter.StringVar(mainWindow, value='1')
    end = tkinter.StringVar(mainWindow, value='-1')
    font = tkinter.font.Font(family='Arial', size=12, weight=tkinter.font.NORMAL)

    #define components
    label1 = tkinter.Label(mainWindow, text='Initial Value: ', width=15, font=font)
    label2 = tkinter.Label(mainWindow, text='End Value: ', width=15, font=font)

    entry1 = tkinter.Entry(mainWindow, textvariable=start, width=15, font=font)
    entry2 = tkinter.Entry(mainWindow, textvariable=end, width=15, font=font)

    selectButton = tkinter.Button(mainWindow, text=' Select ', command=lambda: selectFile(file), width=10, font=font)
    startButton = tkinter.Button(mainWindow, text=' Start ', command=lambda: textCopy(file.get(), start.get(),
                                                    end.get(), mainWindow), width=10, font=font)

    #grid the components
    label1.grid(row=0, column=0)
    entry1.grid(row=0, column=1)
    label2.grid(row=1, column=0)
    entry2.grid(row=1, column=1)
    selectButton.grid(row=2, column=0)
    startButton.grid(row=2, column=1)

    mainWindow.mainloop()


if __name__ == '__main__':
    main()
    








