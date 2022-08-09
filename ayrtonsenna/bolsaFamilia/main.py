import clipboard
from tika import parser  # pip install tika
import textract
import os
import PyPDF2

PATH = r"C:\Users\sbferreira\OneDrive\BKP SECRETARIA\BOLSA FAMÍLIA - AUXILIO BRASIL\2022\pdfs"

ARQS = os.listdir(PATH)
arq1 = LEGENDA = os.path.join(PATH, ARQS[0])
arq2 = os.path.join(PATH, ARQS[1])


def opened_file(f):
    file = open(f, 'rb')
    fileReader = PyPDF2.PdfFileReader(file)
    # print the number of pages in pdf file
    print(fileReader.numPages)
    return fileReader

# arq1 = legenda


def reader(arg, can_print=True):
    r = opened_file(arg)
    # reader = opened_file(arq2)

    text = ""
    for page in r.pages:
        text += page.extract_text() + "\n"
    if can_print:
        print(text)
    return text


# reader(LEGENDA)
alunos = reader(arq2, False)

list_names = []


def word_finder(txt, word):
    TXT = txt
    counter = _mechanics = 0

    while _mechanics <= counter:

        findedindx = TXT.find(word, counter)
        index_final = findedindx + len(word)

        counter = index_final
        if _mechanics < counter:
            _mechanics = counter

        word_final = TXT[findedindx: index_final]
        searched = TXT[index_final:index_final+255]
        print(searched)

        get_nome = searched.split()
        get_nome = " ".join(get_nome[:get_nome.index('Dt.')])
        list_names.append(get_nome)


a = word_finder(alunos, "Nome: ")

input(list_names)


# alunos.find()
