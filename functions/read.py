import docx
from . import kindle


#read&write
def read(file, form): #assign different forms of files to different functions. Now .epud and .mobi are not available
    if form == '.txt':
        return readInTxt(file)
    elif form == '.docx':
        return readInDocx(file)
    elif form == '.epud':
        return readInEpud(file)
    elif form == '.mobi':
        return readInMobi(file)
    else:
        return None


def readInTxt(file): 
    decodeList = ['utf-8', 'gb18030', 'gbk', 'gb2312', 'ISO-8859-2', 'Error'] #predicted encoding list 
    for decode in decodeList: #try them one by one
        try:
            with open(file, 'r', encoding=decode) as f:
                return f.read()
        except:
            if decode == 'Error':
                raise Exception('Decoding Failed')
            continue


def readInDocx(file):
    doc = docx.Document(file)
    text = []
    paras = doc.paragraphs
    for element in paras:
        text.append(element.text)
    return '\n'.join(text)
    

def readInEpud(file):
    pass


def readInMobi(file):
    pass