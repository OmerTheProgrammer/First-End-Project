import tkinter as tk
from tkinter import messagebox
from tkinter import *
score = 0
def true():
    def scoref():
        Atrue.destroy()
        global score
        score += 20
    Atrue = tk.Tk()
    lTrue = tk.Label(master = Atrue,text="True!").pack()
    Button = tk.Button(master = Atrue,command = scoref,text = "אישור").pack()
    Atrue.mainloop()
def worng():
    Afalse = tk.Tk()
    lFalse = tk.Label(master = Afalse,text="fulse!,try again").pack()
    Button = tk.Button(master = Afalse,command = Afalse.destroy, text = "אישור").pack()
    Afalse.mainloop()
def maybe():
    Amaybe = tk.Tk()
    l = tk.Label(master = Amaybe,text="it's a quiz of True or False, no maybe!").pack()
    Button = tk.Button(master = Amaybe,command = Amaybe.destroy, text = "!!!").pack()
#כניסה
logIn = tk.Tk()
#ביקורת
Review = tk.Tk()
def newPage1():
#סוגר את הכניסה
    logIn.destroy()
#שאלות כתיבה
    def newPage2():
        global Review
        Review.destroy()
        WriteQuestions = tk.Tk()
        WriteQuestions.geometry("2500x800")
        WriteQuestions.title("Writing questions&True or False?")
        def Answer6():
            answer = str(e1.get())
            if answer == "מילון":
                true()
            else:
                worng()
        def Answer7():
            answer = str(e1.get())
            if answer == "אוצר מילים":
                true()
            else:
                worng()
        def Answer8():
            answer = str(e1.get())
            if answer == "דקדוק":
                true()
            else:
                worng()
        def Answer9():
            answer = str(e1.get())
            if answer == "way":
                true()
            else:
                worng()
        def Answer10():
            answer = str(e1.get())
            if answer == "space":
                true()
            else:
                worng()
        def Answer11():
            answer = str(e1.get())
            if answer == "100":
                true()
            else:
                worng()
        def Answer12():
            answer = str(e1.get())
            if answer == "gold":
                true()
            else:
                worng()
        e1 = Entry(WriteQuestions)
        e1.pack()
#שאלה 6
        l = tk.Label(master = WriteQuestions ,text = 'what the translation of "dicenary" in Hebrew?').pack()
        btn = tk.Button(master = WriteQuestions, text = "cheack",command = Answer6,bg = "blue").pack()
#שאלה 7
        l = tk.Label(master = WriteQuestions ,text = 'What is translation of "vocabulary" in Hebrew?').pack()
        btn = tk.Button(master = WriteQuestions, text = "cheack",command = Answer7,bg = "blue").pack()
#שאלה 8
        l = tk.Label(master = WriteQuestions ,text = 'what the translation of "grammer" for Hebrew?').pack()
        btn = tk.Button(master = WriteQuestions, text = "cheack",command = Answer8,bg = "blue").pack()
#שאלה 9
        l = tk.Label(master = WriteQuestions ,text = "Speed X Time = ?").pack()
        btn = tk.Button(master = WriteQuestions, text = "cheack",command = Answer9,bg = "blue").pack()
#שאלה 10
        l = tk.Label(master = WriteQuestions ,text = "where can we find fling rock?").pack()
        btn = tk.Button(master = WriteQuestions, text = "cheack",command = Answer10,bg = "blue").pack()
#שאלה 11
        l = tk.Label(master = WriteQuestions ,text = "What boiling water temperature (in C°)?").pack()
        btn = tk.Button(master = WriteQuestions, text = "cheack",command = Answer11,bg = "blue").pack()
#שאלה 12
        l = tk.Label(master = WriteQuestions ,text = "What is the most expensive metal for making rings?").pack()
        btn = tk.Button(master = WriteQuestions, text = "cheack",command = Answer12,bg = "blue").pack()
#שאלה 13
        l = tk.Label(master = WriteQuestions,text="Dogs see better at night than humans.").pack()
        R1 = tk.Radiobutton(master = WriteQuestions, text = "False" ,value = 1,command = worng).pack()
        R2 = tk.Radiobutton(master = WriteQuestions, text = "True" ,value = 2,command = true).pack()
#שאלה 14
        l = tk.Label(master = WriteQuestions,text="Birds can only communicate their voices.").pack()
        R1 = tk.Radiobutton(master = WriteQuestions, text = "False" ,value = 1,command = true).pack()
        R2 = tk.Radiobutton(master = WriteQuestions, text = "True" ,value = 2,command = worng).pack()
#שאלה 15
        l = tk.Label(master = WriteQuestions,text="fish didn't need oxygen to live.").pack()
        R1 = tk.Radiobutton(master = WriteQuestions, text = "False" ,value = 1,command = true).pack()
        R2 = tk.Radiobutton(master = WriteQuestions, text = "True" ,value = 2,command = worng).pack()
        R3 = tk.Radiobutton(master = WriteQuestions, text = "maybe" ,value = 2,command = maybe).pack()
        global score
        btn = Button(master = WriteQuestions, text="Go",command = lambda: image(score),bg = "red").pack()
#תמונה
        def image(score):
            WriteQuestions.destroy()
            image = tk.Tk()
            image.geometry("2500x800")
            image.title("surprise")
#חישוב אחוז שאלות נכונות
# דרך אחרת: cScore = int(((score/20)*100)/15)
            prasent = int(score/3)
            if prasent > 100:
                btn = tk.Button(command = image.destroy,text = "Error!").pack()
            else:
                l = tk.Label(master = image, text = "your score: " + str(score) + " points" ,font = ("Arial",15)).pack()
                l = tk.Label(master = image, text = "your prasent: %" + str(prasent) ,font = ("Arial",15)).pack()
            l = tk.Label(master = image, text = "Thank you for playing the science-math quiz!",font = ("Arial",20)).pack()
            l = tk.Label(master = image, text = ": )", bg = "white",font = ("Arial",400)).pack()
            btn = tk.Button(master = image, text = "by!", bg = "red",command = image.destroy).pack()
            image.mainloop()
        WriteQuestions.mainloop()
#ביקורת
    def opeNreview():
        RdQuestions.destroy()
        Review.lift()
        Review.geometry("250x1000")
        Review.title("Review")
#פונקציה לביקורת
        def yes():
            lab1 = tk.Label(master = Review,text="thank you!",bg = "light blue", width = 200, height = 5).pack()
        def no():
            lab1 = tk.Label(master = Review,text="Oops, I'll try to get better",bg = "blue",fg = "light blue", width = 200, height = 5).pack()
        def cheak1():
            get1 = e1.get()
            if get1 == "yes":
                yes()
            elif get1 == "no":
                no()
            else:
                lab1 = tk.Label(master = Review,text="???",bg = "orange",fg = "blue", width = 200, height = 5).pack()
        lab1 = tk.Label(master = Review,text="Hello, again player",bg = "green",fg = "white", width = 1000, height = 5).pack()
        lab1 = tk.Label(master = Review,text="did you enjoy?",bg = "dark green",fg = "white", width = 1000, height = 5).pack()
        e1 = Entry(Review)
        e1.pack()
        btn = Button(Review, text="cheack",command = cheak1,bg = "blue").pack()
        R1 = tk.Radiobutton(master = Review, text = "yes" ,value = 1,command = yes).pack()
        R2 = tk.Radiobutton(master = Review, text = "no" ,value = 2,command = no).pack()
        btn = Button(master = Review, text = "Go",command = newPage2,bg = "red").pack()
        Review.mainloop()
#פותח את חלון שאלות אמריקאיות
    RdQuestions = tk.Tk()
    RdQuestions.geometry("2500x800")
    RdQuestions.title("Multiple choice questions")
#שאלות אמרקאיות
    lab1 = tk.Label(master = RdQuestions, text = "Welcome to science-math quiz",bg = "light green", width = 1000, font = ("Arial",20)).pack()
#שאלה 1   
    l = tk.Label(master = RdQuestions,text="Question 1:").pack()
    l = tk.Label(master = RdQuestions,text="what is the smallest number here:").pack()
    R1 = tk.Radiobutton(master = RdQuestions, text = "0.1" ,value = 1,command = worng).pack()
    R2 = tk.Radiobutton(master = RdQuestions, text = "-8" ,value = 2,command = true).pack()
    R3 = tk.Radiobutton(master = RdQuestions, text = "-0.33" ,value = 3,command = worng).pack()
#שאלה 2
    l = tk.Label(master = RdQuestions,text="Question 2:").pack()
    l = tk.Label(master = RdQuestions,text="what is the biggest number here:").pack()
    R1 = tk.Radiobutton(master = RdQuestions, text="3591992" ,value = 1,command = worng).pack()
    R2 = tk.Radiobutton(master = RdQuestions, text="3594289" ,value = 2,command = true).pack()
    R3 = tk.Radiobutton(master = RdQuestions, text="3593622" ,value = 3,command = worng).pack()
#שאלה 3
    l = tk.Label(master = RdQuestions,text="Question 3:").pack()
    l = tk.Label(master = RdQuestions,text="what the answer for 3x+1=4:").pack()
    R1 = tk.Radiobutton(master = RdQuestions, text="x = 3" ,value = 1,command = worng).pack()
    R2 = tk.Radiobutton(master = RdQuestions, text="x = 1" ,value = 2,command = true).pack()
    R3 = tk.Radiobutton(master = RdQuestions, text="x = 4" ,value = 3,command = worng).pack()
#שאלה 4
    l = tk.Label(master = RdQuestions,text="Question 4:").pack()
    l = tk.Label(master = RdQuestions,text="what the answer for 3x+1=2x:").pack()
    R1 = tk.Radiobutton(master = RdQuestions, text="-x = 1" ,value = 1,command = worng).pack()
    R2 = tk.Radiobutton(master = RdQuestions, text="x = -1" ,value = 2,command = true).pack()
    R3 = tk.Radiobutton(master = RdQuestions, text="x = 5" ,value = 3,command = worng).pack()
    R3 = tk.Radiobutton(master = RdQuestions, text="x = 8" ,value = 4,command = worng).pack()
#שאלה 5
    l = tk.Label(master = RdQuestions,text="Question 5:").pack()
    l = tk.Label(master = RdQuestions,text="what the answer for:2y = 2x + 20").pack()
    l = tk.Label(master = RdQuestions,text="y = 10 + 4x").pack()
    R1 = tk.Radiobutton(master = RdQuestions, text="-4x = 0" ,value = 1,command = true).pack()
    R2 = tk.Radiobutton(master = RdQuestions, text="x = 3" ,value = 4,command = worng).pack()
    R3 = tk.Radiobutton(master = RdQuestions, text="x = 0" ,value = 2,command = true).pack()
    R4 = tk.Radiobutton(master = RdQuestions, text="x = 9" ,value = 3,command = worng).pack()
#כפתור פתיחת ביקורת
    btn = Button(master = RdQuestions, text = "Go",command = opeNreview,bg = "red").pack()
    RdQuestions.mainloop()
#הגדרת כניסה
logIn.geometry("2500x800")
logIn.title("log in")
#טקסט ושאלות אישיות
l = tk.Label(master = logIn,text="your E-mail:").pack()
e1 = Entry(logIn)
e1.pack()
l = tk.Label(master = logIn,text="where are you from?").pack()
e2 = Entry(logIn)
e2.pack()
lab2 = tk.Label(master = logIn, text="your name:").pack()
e3 = Entry(logIn)
e3.pack()
btn = Button(logIn, text = "Go",command = newPage1,bg = "red").pack()
#בדיקה
def cheak2():
    get = str(e3.get())
    l = tk.Label(master = logIn, text = "Hello "+ get,bg = "green",fg = "white",font= ("arial", 100)).pack()
btn = Button(logIn, text = "cheack",command = cheak2,bg = "blue").pack()
logIn.mainloop()