from tkinter import *

# LEO'S GOOD FILE
#

bca = open('bca_questions.txt', 'r')
meme = open('meme_questions.txt', 'r')
number = open('number_questions.txt', 'r')
python = open('python_questions.txt', 'r')
random = open('random_questions.txt', 'r')
filelist = [bca, meme, number, python, random]
dbca = {}
dmeme = {}
dnumber = {}
dpython = {}
drandom = {}
thatlist = [dbca, dmeme, dnumber, dpython, drandom]
for file in filelist:
    for line in file:
        line = line.split(';')
        if file == bca:
            dbca[line[0].strip()] = line[1].strip()
        elif file == meme:
            dmeme[line[0].strip()] = line[1].strip()
        elif file == number:
            dnumber[line[0].strip()] = line[1].strip()
        elif file == python:
            dpython[line[0].strip()] = line[1].strip()
        else:
            drandom[line[0].strip()] = line[1].strip()
keybca = list(dbca.keys())
keymeme = list(dmeme.keys())
keynumber = list(dnumber.keys())
keypython = list(dpython.keys())
keyrandom = list(drandom.keys())
keyslist = [keybca, keymeme, keynumber, keypython, keyrandom]


class Application (Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.currAns = ""
        self.create_widgets()

    def create_widgets(self):
        # Question box
        Label(self, text="Question:", font=("Comic Sans", 15)).grid(row=7, column=2, columnspan=2, sticky=N + S + E + W)
        self.question = Text(self, height=2, wrap=WORD, relief="solid")
        self.question.grid(row=8, column=0, columnspan=5)

        # Header
        Label(self, text="Jeopardy", relief="solid", font=("Comic Sans", 30), bg="blue").grid(row=0, column=0, columnspan=5, sticky=N+S+E+W)

        # Category labels
        Label(self, text="BCA", relief="solid", font=("Comic Sans", 30), bg="blue").grid(row=1, column=0, columnspan=1, sticky=N+S+E+W)
        Label(self, text="Memes", relief="solid", font=("Comic Sans", 30), bg="blue").grid(row=1, column=1, columnspan=1, sticky=N+S+E+W)
        Label(self, text="Numbers", relief="solid", font=("Comic Sans", 30), bg="blue").grid(row=1, column=2, columnspan=1, sticky=N+S+E+W)
        Label(self, text="Python", relief="solid", font=("Comic Sans", 30), bg="blue").grid(row=1, column=3, columnspan=1, sticky=N+S+E+W)
        Label(self, text="Miscellaneous", relief="solid", font=("Comic Sans", 30), bg="blue").grid(row=1, column=4, columnspan=1, sticky=N+S+E+W)

        # 100 Point row
        self.cat1_100 = Button(self, text="100", font=("Comic Sans", 30), relief="solid", bg="red", command=lambda: self.question_bttn(0, 0)) #command
        self.cat1_100.grid(row=2, column=0, sticky=N+S+E+W)
        self.cat2_100 = Button(self, text="100", font=("Comic Sans", 30), relief="solid", bg="red", command=lambda: self.question_bttn(1, 0)) #command
        self.cat2_100.grid(row=2, column=1, sticky=N+S+E+W)
        self.cat3_100 = Button(self, text="100", font=("Comic Sans", 30), relief="solid", bg="red", command=lambda: self.question_bttn(2, 0)) #command
        self.cat3_100.grid(row=2, column=2, sticky=N+S+E+W)
        self.cat4_100 = Button(self, text="100", font=("Comic Sans", 30), relief="solid", bg="red", command=lambda: self.question_bttn(3, 0)) #command
        self.cat4_100.grid(row=2, column=3, sticky=N+S+E+W)
        self.cat5_100 = Button(self, text="100", font=("Comic Sans", 30), relief="solid", bg="red", command=lambda: self.question_bttn(4, 0)) #command
        self.cat5_100.grid(row=2, column=4, sticky=N+S+E+W)

        # 200 Point row
        self.cat1_200 = Button(self, text="200", font=("Comic Sans", 30), relief="solid", bg="orange", command=lambda: self.question_bttn(0, 1))  # command
        self.cat1_200.grid(row=3, column=0, sticky=N+S+E+W)
        self.cat2_200 = Button(self, text="200", font=("Comic Sans", 30), relief="solid", bg="orange", command=lambda: self.question_bttn(1, 1))  # command
        self.cat2_200.grid(row=3, column=1, sticky=N+S+E+W)
        self.cat3_200 = Button(self, text="200", font=("Comic Sans", 30), relief="solid", bg="orange", command=lambda: self.question_bttn(2, 1))  # command
        self.cat3_200.grid(row=3, column=2, sticky=N+S+E+W)
        self.cat4_200 = Button(self, text="200", font=("Comic Sans", 30), relief="solid", bg="orange", command=lambda: self.question_bttn(3, 1))  # command
        self.cat4_200.grid(row=3, column=3, sticky=N+S+E+W)
        self.cat5_200 = Button(self, text="200", font=("Comic Sans", 30), relief="solid", bg="orange", command=lambda: self.question_bttn(4, 1))  # command
        self.cat5_200.grid(row=3, column=4, sticky=N+S+E+W)

        # 300 Point row
        self.cat1_300 = Button(self, text="300", font=("Comic Sans", 30), relief="solid", bg="yellow", command=lambda: self.question_bttn(0, 2))  # command
        self.cat1_300.grid(row=4, column=0, sticky=N+S+E+W)
        self.cat2_300 = Button(self, text="300", font=("Comic Sans", 30), relief="solid", bg="yellow", command=lambda: self.question_bttn(1, 2))  # command
        self.cat2_300.grid(row=4, column=1, sticky=N+S+E+W)
        self.cat3_300 = Button(self, text="300", font=("Comic Sans", 30), relief="solid", bg="yellow", command=lambda: self.question_bttn(2, 2))  # command
        self.cat3_300.grid(row=4, column=2, sticky=N+S+E+W)
        self.cat4_300 = Button(self, text="300", font=("Comic Sans", 30), relief="solid", bg="yellow", command=lambda: self.question_bttn(3, 2))  # command
        self.cat4_300.grid(row=4, column=3, sticky=N+S+E+W)
        self.cat5_300 = Button(self, text="300", font=("Comic Sans", 30), relief="solid", bg="yellow", command=lambda: self.question_bttn(4, 2))  # command
        self.cat5_300.grid(row=4, column=4, sticky=N+S+E+W)

        # 400 Point row
        self.cat1_400 = Button(self, text="400", font=("Comic Sans", 30), relief="solid", bg="green", command=lambda: self.question_bttn(0, 3))  # command
        self.cat1_400.grid(row=5, column=0, sticky=N+S+E+W)
        self.cat2_400 = Button(self, text="400", font=("Comic Sans", 30), relief="solid", bg="green", command=lambda: self.question_bttn(1, 3))  # command
        self.cat2_400.grid(row=5, column=1, sticky=N+S+E+W)
        self.cat3_400 = Button(self, text="400", font=("Comic Sans", 30), relief="solid", bg="green", command=lambda: self.question_bttn(2, 3))  # command
        self.cat3_400.grid(row=5, column=2, sticky=N+S+E+W)
        self.cat4_400 = Button(self, text="400", font=("Comic Sans", 30), relief="solid", bg="green", command=lambda: self.question_bttn(3, 3))  # command
        self.cat4_400.grid(row=5, column=3, sticky=N+S+E+W)
        self.cat5_400 = Button(self, text="400", font=("Comic Sans", 30), relief="solid", bg="green", command=lambda: self.question_bttn(4, 3))  # command
        self.cat5_400.grid(row=5, column=4, sticky=N+S+E+W)

        # 500 Point row
        self.cat1_500 = Button(self, text="500", font=("Comic Sans", 30), relief="solid", bg="purple", command=lambda: self.question_bttn(0, 4))  # command
        self.cat1_500.grid(row=6, column=0, sticky=N+S+E+W)
        self.cat2_500 = Button(self, text="500", font=("Comic Sans", 30), relief="solid", bg="purple", command=lambda: self.question_bttn(1, 4))  # command
        self.cat2_500.grid(row=6, column=1, sticky=N+S+E+W)
        self.cat3_500 = Button(self, text="500", font=("Comic Sans", 30), relief="solid", bg="purple", command=lambda: self.question_bttn(2, 4))  # command
        self.cat3_500.grid(row=6, column=2, sticky=N+S+E+W)
        self.cat4_500 = Button(self, text="500", font=("Comic Sans", 30), relief="solid", bg="purple", command=lambda: self.question_bttn(3, 4))  # command
        self.cat4_500.grid(row=6, column=3, sticky=N+S+E+W)
        self.cat5_500 = Button(self, text="500", font=("Comic Sans", 30), relief="solid", bg="purple", command=lambda: self.question_bttn(4, 4))  # command
        self.cat5_500.grid(row=6, column=4, sticky=N+S+E+W)



        # Answer box
        Label(self, text="Answer:", font=("Comic Sans", 15)).grid(row=9, column=2, columnspan=2, sticky=N + S + E + W)
        self.answer = Entry(self, relief="solid")
        self.answer.grid(row=10, column=0, columnspan=5)
        #Enter button
        self.enter = Button(self, text="Enter", font=("Comic Sans", 15), relief="solid", bg="blue", command=self.correct)  # command
        self.enter.grid(row=11, column=2, columnspan=2, sticky=N + S + E + W)
        self.correctbox = Text(self, height=2, wrap=WORD, relief="solid")
        self.correctbox.grid(row=12, column=0, columnspan=5)

        # Footer
        Label(self, text=" ", relief="solid", font=("Comic Sans", 30), bg="blue").grid(row=13, column=0, columnspan=5, sticky=N + S + E + W)

    def question_bttn(self, row, col):
        questDict = keyslist[row]
        ansDict = thatlist[row]
        self.question.delete(0.0, END)
        self.question.insert(0.0, questDict[col])
        self.currAns = ansDict[questDict[col]]
        print ("Hello")

    def correct(self):
        q = self.question.get(0.0, END).strip()
        ans = self.answer.get()
        self.correctbox.delete(0.0, END)

        if ans.lower() == self.currAns:
            self.correctbox.insert(0.0, 'CORRECT!!!!!')
        else:
            self.correctbox.insert(0.0, "INCORRECT :(")

root = Tk()
root.title("Jeopardy")
app = Application(root)
root.mainloop()
