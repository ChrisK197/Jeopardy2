from tkinter import *

# LEO'S GOOD FILE
# Leo's bad variable names


class Application (Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        master.bind("<Return>", self.correct)
        self.grid()
        self.currAns = ""
        self.score = 0
        self.buttons = {}

        fileNames = ['bca_questions.txt', 'meme_questions.txt', 'number_questions.txt', 'python_questions.txt',
                     'random_questions.txt']
        self.questDict = {}
        self.categories = []
        for fileName in fileNames:
            file = open(fileName, 'r')
            category = file.readline().strip()
            self.categories.append(category)
            val = 100
            for line in file:
                line = line.split(';')
                d = {}
                d["Q"] = line[0]
                d["A"] = line[1]  # Add button parameter
                d['button'] = line[2]  # column,row
                d['point'] = val
                self.questDict[category + "_" + str(val)] = d
                val += 100

        self.create_widgets()

    def create_widgets(self):
        # Question box
        Label(self, text="Question:", font=("Comic Sans", 15)).grid(row=7, column=2, columnspan=2, sticky=N + S + E + W)
        self.question = Text(self, height=2, wrap=WORD, relief="solid")
        self.question.grid(row=8, column=0, columnspan=5)

        # Header
        Label(self, text="Jeopardy", relief="solid", font=("Comic Sans", 30), bg="blue").grid(row=0, column=0, columnspan=5, sticky=N+S+E+W)

        # Category labels
        c = 0
        for term in self.categories:
            Label(self, text=term, relief='solid', font=('Comic Sans', 30), bg='blue').grid(row=1, column=c, columnspan=1, sticky=N+S+E+W)
            c += 1
        # 100 Point row
        self.BCA_100 = Button(self, text="100", font=("Comic Sans", 30), relief="solid", bg="red", state=NORMAL, command=lambda: self.question_bttn("BCA_100")) #command
        self.buttons["BCA_100"] = self.BCA_100
        self.BCA_100.grid(row=2, column=0, sticky=N + S + E + W)
        self.Memes_100 = Button(self, text="100", font=("Comic Sans", 30), relief="solid", bg="red", state=NORMAL, command=lambda: self.question_bttn("Memes_100")) #command
        self.buttons["Memes_100"] = self.Memes_100
        self.Memes_100.grid(row=2, column=1, sticky=N + S + E + W)
        self.Numbers_100 = Button(self, text="100", font=("Comic Sans", 30), relief="solid", bg="red", state=NORMAL, command=lambda: self.question_bttn("Numbers_100")) #command
        self.buttons["Numbers_100"] = self.Numbers_100
        self.Numbers_100.grid(row=2, column=2, sticky=N + S + E + W)
        self.Python_100 = Button(self, text="100", font=("Comic Sans", 30), relief="solid", bg="red", state=NORMAL, command=lambda: self.question_bttn("Python_100")) #command
        self.buttons["Python_100"] = self.Python_100
        self.Python_100.grid(row=2, column=3, sticky=N + S + E + W)
        self.Miscellaneous_100 = Button(self, text="100", font=("Comic Sans", 30), relief="solid", bg="red", state=NORMAL, command=lambda: self.question_bttn("Miscellaneous_100")) #command
        self.buttons["Miscellaneous_100"] = self.Miscellaneous_100
        self.Miscellaneous_100.grid(row=2, column=4, sticky=N + S + E + W)

        # 200 Point row
        self.BCA_200 = Button(self, text="200", font=("Comic Sans", 30), relief="solid", bg="orange", state=NORMAL, command=lambda: self.question_bttn("BCA_200"))  # command
        self.buttons["BCA_200"] = self.BCA_200
        self.BCA_200.grid(row=3, column=0, sticky=N + S + E + W)
        self.Memes_200 = Button(self, text="200", font=("Comic Sans", 30), relief="solid", bg="orange", state=NORMAL, command=lambda: self.question_bttn("Memes_200"))  # command
        self.buttons["Memes_200"] = self.Memes_200
        self.Memes_200.grid(row=3, column=1, sticky=N + S + E + W)
        self.Numbers_200 = Button(self, text="200", font=("Comic Sans", 30), relief="solid", bg="orange", state=NORMAL, command=lambda: self.question_bttn("Numbers_200"))  # command
        self.buttons["Numbers_200"] = self.Numbers_200
        self.Numbers_200.grid(row=3, column=2, sticky=N + S + E + W)
        self.Python_200 = Button(self, text="200", font=("Comic Sans", 30), relief="solid", bg="orange", state=NORMAL, command=lambda: self.question_bttn("Python_200"))  # command
        self.buttons["Python_200"] = self.Python_200
        self.Python_200.grid(row=3, column=3, sticky=N + S + E + W)
        self.Miscellaneous_200 = Button(self, text="200", font=("Comic Sans", 30), relief="solid", bg="orange", state=NORMAL, command=lambda: self.question_bttn("Miscellaneous_200"))  # command
        self.buttons["Miscellaneous_200"] = self.Miscellaneous_200
        self.Miscellaneous_200.grid(row=3, column=4, sticky=N + S + E + W)

        # 300 Point row
        self.BCA_300 = Button(self, text="300", font=("Comic Sans", 30), relief="solid", bg="yellow", state=NORMAL, command=lambda: self.question_bttn("BCA_300"))  # command
        self.buttons["BCA_300"] = self.BCA_300
        self.BCA_300.grid(row=4, column=0, sticky=N + S + E + W)
        self.Memes_300 = Button(self, text="300", font=("Comic Sans", 30), relief="solid", bg="yellow", state=NORMAL, command=lambda: self.question_bttn("Memes_300"))  # command
        self.buttons["Memes_300"] = self.Memes_300
        self.Memes_300.grid(row=4, column=1, sticky=N + S + E + W)
        self.Numbers_300 = Button(self, text="300", font=("Comic Sans", 30), relief="solid", bg="yellow", state=NORMAL, command=lambda: self.question_bttn("Numbers_300"))  # command
        self.buttons["Numbers_300"] = self.Numbers_300
        self.Numbers_300.grid(row=4, column=2, sticky=N + S + E + W)
        self.Python_300 = Button(self, text="300", font=("Comic Sans", 30), relief="solid", bg="yellow", state=NORMAL, command=lambda: self.question_bttn("Python_300"))  # command
        self.buttons["Python_300"] = self.Python_300
        self.Python_300.grid(row=4, column=3, sticky=N + S + E + W)
        self.Miscellaneous_300 = Button(self, text="300", font=("Comic Sans", 30), relief="solid", bg="yellow", state=NORMAL, command=lambda: self.question_bttn("Miscellaneous_300"))  # command
        self.buttons["Miscellaneous_300"] = self.Miscellaneous_300
        self.Miscellaneous_300.grid(row=4, column=4, sticky=N + S + E + W)

        # 400 Point row
        self.BCA_400 = Button(self, text="400", font=("Comic Sans", 30), relief="solid", bg="green", state=NORMAL, command=lambda: self.question_bttn("BCA_400"))  # command
        self.buttons["BCA_400"] = self.BCA_400
        self.BCA_400.grid(row=5, column=0, sticky=N + S + E + W)
        self.Memes_400 = Button(self, text="400", font=("Comic Sans", 30), relief="solid", bg="green", state=NORMAL, command=lambda: self.question_bttn("Memes_400"))  # command
        self.buttons["Memes_400"] = self.Memes_400
        self.Memes_400.grid(row=5, column=1, sticky=N + S + E + W)
        self.Numbers_400 = Button(self, text="400", font=("Comic Sans", 30), relief="solid", bg="green", state=NORMAL, command=lambda: self.question_bttn("Numbers_400"))  # command
        self.buttons["Numbers_400"] = self.Numbers_400
        self.Numbers_400.grid(row=5, column=2, sticky=N + S + E + W)
        self.Python_400 = Button(self, text="400", font=("Comic Sans", 30), relief="solid", bg="green", state=NORMAL, command=lambda: self.question_bttn("Python_400"))  # command
        self.buttons["Python_400"] = self.Python_400
        self.Python_400.grid(row=5, column=3, sticky=N + S + E + W)
        self.Miscellaneous_400 = Button(self, text="400", font=("Comic Sans", 30), relief="solid", bg="green", state=NORMAL, command=lambda: self.question_bttn("Miscellaneous_400"))  # command
        self.buttons["Miscellaneous_400"] = self.Miscellaneous_400
        self.Miscellaneous_400.grid(row=5, column=4, sticky=N + S + E + W)

        # 500 Point row
        self.BCA_500 = Button(self, text="500", font=("Comic Sans", 30), relief="solid", bg="purple", state=NORMAL, command=lambda: self.question_bttn("BCA_500"))  # command
        self.buttons["BCA_500"] = self.BCA_500
        self.BCA_500.grid(row=6, column=0, sticky=N + S + E + W)
        self.Memes_500 = Button(self, text="500", font=("Comic Sans", 30), relief="solid", bg="purple", state=NORMAL, command=lambda: self.question_bttn("Memes_500"))  # command
        self.buttons["Memes_500"] = self.Memes_500
        self.Memes_500.grid(row=6, column=1, sticky=N + S + E + W)
        self.Numbers_500 = Button(self, text="500", font=("Comic Sans", 30), relief="solid", bg="purple", state=NORMAL, command=lambda: self.question_bttn("Numbers_500"))  # command
        self.buttons["Numbers_500"] = self.Numbers_500
        self.Numbers_500.grid(row=6, column=2, sticky=N + S + E + W)
        self.Python_500 = Button(self, text="500", font=("Comic Sans", 30), relief="solid", bg="purple", state=NORMAL, command=lambda: self.question_bttn("Python_500"))  # command
        self.buttons["Python_500"] = self.Python_500
        self.Python_500.grid(row=6, column=3, sticky=N + S + E + W)
        self.Miscellaneous_500 = Button(self, text="500", font=("Comic Sans", 30), relief="solid", bg="purple", state=NORMAL, command=lambda: self.question_bttn("Miscellaneous_500"))  # command
        self.buttons["Miscellaneous_500"] = self.Miscellaneous_500
        self.Miscellaneous_500.grid(row=6, column=4, sticky=N + S + E + W)



        # Answer box
        Label(self, text="Answer:", font=("Comic Sans", 15)).grid(row=9, column=2, columnspan=2, sticky=N + S + E + W)
        self.answer = Entry(self, relief="solid")
        self.answer.grid(row=10, column=0, columnspan=5)
        #Enter button
        self.enter = Button(self, text="Enter", font=("Comic Sans", 15), relief="solid", bg="blue", command=self.correct)  # command
        self.enter.grid(row=11, column=2, columnspan=2, sticky=N + S + E + W)
        self.enter.bind("<w>")
        self.correctbox = Text(self, height=2, wrap=WORD, relief="solid")
        self.correctbox.grid(row=12, column=0, columnspan=5)

        # Footer
        Label(self, text=" ", relief="solid", font=("Comic Sans", 30), bg="blue").grid(row=13, column=0, columnspan=5, sticky=N + S + E + W)

    def question_bttn(self, name):
        self.question.delete(0.0, END)
        currentdict = self.questDict[name]
        self.question.insert(0.0, currentdict["Q"])
        self.currAns = currentdict["A"]
        self.name = name

    def correct(self, event=0):
        q = self.question.get(0.0, END).strip()
        ans = self.answer.get()
        self.correctbox.delete(0.0, END)
        self.answer.delete(0, "end")
        h = self.questDict[self.name]
        p = h['point']
        self.buttons[self.name].config(state=DISABLED, bg="blue")
        if ans.lower() == self.currAns:
            self.score += p
            self.correctbox.insert(0.0, 'CORRECT!!!!!\nScore = %d' % self.score)
        else:
            self.score -= p
            self.correctbox.insert(0.0, "INCORRECT :(\nScore = %d" % self.score)

root = Tk()
root.title("Jeopardy")
app = Application(root)
root.mainloop()
