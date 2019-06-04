import docx
from . import kindle


def write(file, content, form): #assign different forms of files to different functions
    if form == '.txt':
        return writeInTxt(file, content)
    elif form == '.docx':
        return writeInDocx(file, content)
    elif form == '.epud':
        return writeInEpud(file, content)
    elif form == '.mobi':
        return writeInMobi(file, content)
    else:
        return None
        

def writeInTxt(file, content):
    decodeList = ['gbk', 'gb18030', 'gb2312', 'utf-8', 'ISO-8859-2', 'Error'] #predicted encoding list 
    for decode in decodeList: #try them one by one
        try:
            with open(file, 'wb') as f:
                f.write(content.encode(decode))
                break
        except:
            if decode == 'Error':
                raise Exception('Decoding Failed')
            continue


def writeInDocx(file, content):
    doc = docx.Document()
    doc.add_paragraph(content)
    doc.save(file)


def writeInEpud(file, content):
    pass


def writeInMobi(file, content):
    pass
