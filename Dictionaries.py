thatlist = []
bca = open('bca_questions.txt', 'r')
meme = open('meme_questions.txt', 'r')
number = open('number_questions.txt', 'r')
python = open('python_questions.txt', 'r')
random = open('random_questions.txt', 'r')
filelist= [bca, meme, number, python, random]
dbca = {}
dmeme = {}
dnumber = {}
dpython = {}
drandom = {}
thatlist = [dbca, dmeme, dnumber,dpython, drandom]
for file in filelist:
    for line in file:
        line = line.split(';')
        if file == bca:
            dbca[line[0]] = line[1]
        elif file == meme:
            dmeme[line[0]] = line[1]
        elif file == number:
            dnumber[line[0]] = line[1]
        elif file == python:
            dpython[line[0]] = line[1]
        else:
            drandom[line[0]] = line[1]

