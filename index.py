from tkinter import *
import webbrowser
from tkinter import messagebox
#from database import *
main = Tk()  # creating window
main.title("pedagogy")  # title giving to the app
main.geometry("400x670")  # created size of the window
main.resizable(False, False)
def f2():
    f2 = Frame(bg="light cyan")
    f2.place(x=1, y=1, width=400, height=670)
    l2 = Label(f2, bg="light cyan",fg="red",text="PROBABILITY AND STATISTICS ", font=("bold", 15)).place(x=50, y=5)
    sea=Button(f2,width=8,height=1,font=('bold',12),bg="gray65",text="search").place(x=315, y=38)
    e2 = Entry(f2,font=("italic",16)).place(x=12, y=40, width=300)
    t1="If a trial results in n-exhaustive mutually exclusive,and\n equally likely cases and m of them are favorable to\n the happening of an event E then the probability of an \nevent E is denoted by P(E) and is defined as \nP(E) = no of favourable events/total no of events"
    #t3=""
    t2=" probability density function defines the probability function\n representing the density of a continuous random variable\n lying between a specific range of values. In other words,"
    Label(f2,bg="light cyan",text=t1,font=("italic",12)).place(x=0,y=100)
    Label(f2,text=t2,bg="light cyan",font=("italic",12)).place(x=0,y=210)
    Label(f2,text="what is probability(mathematical definition)?",bg="light cyan", fg="blue",font=("bold",14)).place(x=5,y=75)
    Label(f2, bg="light cyan",text="what is probability density function?", fg="blue", font=("bold", 14)).place(x=5, y=190)
    b1 = Button(f2, width=10, height=2, text="back", command=f1, cursor="hand2").place(x=10, y=550)
    bb1 = Button(f2,text="CLICK FOR MORE", width=15, height=2, command=pspage, cursor="hand2").place(x=270, y=550)

def f3():
    f3 = Frame(bg="light cyan")
    f3.place(x=1, y=1, width=400, height=670)
    # scroll1=Scrollbar(f3).pack(side=RIGHT,fill=Y)
    l3 = Label(f3, bg="light cyan",text="PYTHON PROGRAMMING",fg="red", font=("bold", 15)).place(x=80, y=5)
    sea=Button(f3,width=8,height=1,font=('bold',12),bg="gray65",text="search").place(x=315, y=38)
    e2 = Entry(f3,font=("italic",16)).place(x=12, y=40, width=300)
    Label(f3,text="LIST",fg="blue",bg="light cyan",font=("bold",18)).place(x=170,y=75)
    t1="A list in Python is used to store the sequence of various \ntypes of data. Python lists are mutable type its mean we\n can modify its elements after it created"
    t2="Python Tuple is a collection of objects separated by \ncommas.In some ways, a tuple is similar to a list in \nterms of indexing, nested objects, and repetition but a\n tuple is immutable, unlike lists which are mutable"
    t3="Dictionary in Python is a collection of keys values, \nused to store data values like a map, which, unlike other\n data types which hold only a single value as an element"
    Label(f3, text="TUPLE", fg="blue", bg="light cyan", font=("bold", 18)).place(x=160, y=170)
    Label(f3, text="DICTIONARY", fg="blue", bg="light cyan", font=("bold", 18)).place(x=120, y=290)
    Label(f3,text=t1,bg="light cyan",font=("italic",12)).place(x=5,y=100)
    Label(f3, text=t2, bg="light cyan", font=("italic", 12)).place(x=5, y=200)
    Label(f3, text=t3, bg="light cyan", font=("italic", 12)).place(x=5, y=320)
    b2 = Button(f3, width=10, height=2, text="back", command=f1).place(x=10, y=550)
    bb1 = Button(f3, text="CLICK FOR MORE", width=15, height=2, command=pythonpage, cursor="hand2").place(x=270, y=550)
def f4():
    f4 = Frame(bg="skyblue")
    f4.place(x=1, y=1, width=400, height=670)
    l4 = Label(f4, text="DIGITAL LOGIC DESIGN", font=("bold", 15)).place(x=80, y=5)
    sea = Button(f4, width=8, height=1, font=('bold', 12), bg="skyblue", text="search").place(x=315, y=38)
    e2 = Entry(f4, font=("italic", 16)).place(x=12, y=40, width=300)
    b3 = Button(f4, width=10, height=2, text="back", command=f1).place(x=10, y=550)
    bb1 = Button(f4, text="CLICK FOR MORE", width=15, height=2, command=dldpage, cursor="hand2").place(x=270, y=550)
def f5():
    f5 = Frame(bg="skyblue")
    f5.place(x=1, y=1, width=400, height=670)
    l5 = Label(f5, text="DATABASE MANAGEMENT SYSTEM", font=("bold", 15)).place(x=30, y=5)
    search = Label(f5, text="search", font=("bold", 12)).place(x=5, y=40)
    e2 = Entry(f5).place(x=60, y=40, width=300)
    b4 = Button(f5, width=10, height=2, text="back", command=f1).place(x=10, y=550)
    bb1 = Button(f5, text="CLICK FOR MORE", width=15, height=2, command=dbmspage, cursor="hand2").place(x=270, y=550)
def f6():
    f6 = Frame(bg="skyblue")
    f6.place(x=1, y=1, width=400, height=670)
    l6 = Label(f6, text="COMPUTER NETWORKS", font=("bold", 15)).pack()
    search = Label(f6, text="search", font=("bold", 12)).place(x=5, y=40)
    e2 = Entry(f6).place(x=60, y=40, width=300)
    b5 = Button(f6, width=10, height=2, text="back", command=f1).place(x=10, y=550)
    bb1 = Button(f6, text="CLICK FOR MORE", width=15, height=2, command=cnpage, cursor="hand2").place(x=270, y=550)
def f7():
    f7 = Frame(bg="#363636")
    f7.place(x=0, y=0, width=400, height=670)
    l1 = Label(f7, text="PEDAGOGY", bg="#363636", fg="white", font=("italic", 20)).pack(padx=10, pady=15)
    ps = Button(f7, text="PROBABILITY \n AND \nSTATISTICS",bg="#7A7AC5", activebackground="yellow", width=20, height=8, fg="blue",
                font=("italic", 12), command=f2).place(x=10, y=70)
    pp = Button(f7, text="PYTHON \n PROGRAMMING",bg="#A5A52A", width=20, activebackground="yellow", height=8, fg="blue",
                font=("italic", 12), command=f3).place(x=200, y=70)
    dld = Button(f7, text="DIGITAL LOGIC DESIGN \n AND \n COMPUTER ORGANISATION",bg="#CDCD33", width=20, height=8, fg="blue",
                 font=("italic", 12), command=f4).place(x=10, y=240)
    dbms = Button(f7, text="DATABASE \n MANAGEMENT \n SYSTEM",bg="#8E8EE5", width=20, height=8, fg="blue", font=("italic", 12),
                  command=f5).place(x=200, y=240)
    cn = Button(f7, text="COMPUTER NETWORKS", width=41, height=8,bg="yellow green", command=f6, fg="blue", font=("italic", 12)).place(
        x=10, y=410)
    onof = Button(f7, text="light mode", width=9, command=f1, height=1, fg="black", font=("italic", 12)).place(x=300,
                                                                                                              y=25)
    btnb = Button(f7, cursor="hand2",bg="#777788", text="any queries?", width=14, height=1, fg="blue", font=("italic", 12)).place(x=250, y=590)
    btna = Button(f7, cursor="hand2", text="logout",bg="#777788", width=14,command=login, height=1, fg="blue", font=("italic", 12)).place(x=20,y=590)
def f1():
    f1 = Frame(bg="burlywood1")
    f1.place(x=0, y=0, width=400, height=670)
    l1 = Label(f1, text="PEDAGOGY",fg="black",bg="burlywood1", font=("italic",20,"bold")).pack(padx=10, pady=15)
    ps = Button(f1,text="PROBABILITY \n AND \nSTATISTICS",bg="#7A7AC5", activebackground="dark orange", width=20, height=8, fg="blue",
                font=("italic", 12), command=f2, cursor="hand2").place(x=10, y=70)
    pp = Button(f1,cursor="hand2",bg="#A5A52A", text="PYTHON \n PROGRAMMING", width=20, activebackground="dark orange", height=8, fg="blue",
                font=("italic", 12), command=f3).place(x=200, y=70)
    dld = Button(f1,activebackground="dark orange",cursor="hand2",bg="#CDCD33", text="DIGITAL LOGIC DESIGN \n AND \n COMPUTER ORGANISATION", width=20, height=8, fg="blue",
                 font=("italic", 12), command=f4).place(x=10, y=240)
    dbms = Button(f1,cursor="hand2",activebackground="dark orange", text="DATABASE \n MANAGEMENT \n SYSTEM",bg="#8E8EE5", width=20, height=8, fg="blue", font=("italic", 12),
                  command=f5).place(x=200, y=240)
    cn = Button(f1,cursor="hand2",activebackground="dark orange",bg="yellow green", text="COMPUTER NETWORKS", width=41, height=8, command=f6, fg="blue", font=("italic", 12)).place(
        x=10, y=410)
    onof = Button(f1, cursor="hand2",bg="#777788",text="dark mode", width=9, height=1, command=f7, fg="white", font=("italic", 12)).place(x=300,
                                                                                                             y=25)
    btnb = Button(f1, cursor="hand2", bg="#777788",text="any queries?", width=14, height=1, fg="black", font=("italic", 12)).place(x=250, y=590)
    btna = Button(f1,cursor="hand2",bg="#777788", command=login,text="logout", width=14, height=1, fg="red", font=("italic", 12)).place(x=20, y=590)
def pspage():
    webbrowser.open("https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2014/pages/syllabus/")
def pythonpage():
    webbrowser.open("https://www.w3schools.com/python/python_datatypes.asp")
def dldpage():
    webbrowser.open("https://www.arl.wustl.edu/~jon.turner/cse/260/intro.html")
def cnpage():
    webbrowser.open('https://www.javatpoint.com/computer-network-tutorial')
def dbmspage():
    webbrowser.open("https://www.javatpoint.com/dbms-sql-introduction")

def registration():
    u = a1.get()
    p = a2.get()
    cp = a3.get()
    def checkp(check):
        count=0
        for i in range(0, len(check)):
            ver = check[i].split()
            if u == ver[0]:
                count += 1
                messagebox.showerror("error", "this user name is not avilable \n try with another one")
            else:
                pass
        return count
        count=0
    if p==cp:
        f = open("pedagogy.txt", 'r+')
        check = f.readlines()
        k=checkp(check)
        f.close()
        if k==0:
            f=open('pedagogy.txt','a+')
            li=u+' '+p+'\n'
            f.write(li)
            f.close()
            messagebox.showinfo('info','registered successfully\nlogin now ')
        else:
            pass
    else:
        messagebox.showwarning('warning','passwords are not matching')
def loginto():
    us=0
    userc=""
    passc=""
    u = ll1.get()
    p = ll2.get()
    f = open("pedagogy.txt", 'r')
    check1 = f.readlines()
    for i in range(0, len(check1)):
        ver1 = check1[i].split()
        if u == ver1[0]:
            us+=1
            userc=ver1[0]
            passc=ver1[1]
        else:
            pass
    if us==1 or us > 1:
        if p==passc:
            f1()
        else:
            messagebox.showwarning("warning","password is incorrect")
    else:
        messagebox.showwarning("warning","username is not found")
def login():
    global ll1,ll2
    log=Frame(bg="light cyan").place(x=0,y=0,width=400,height=670)
    log1=Frame(bg="gray36").place(x=0,y=180,width=400,height=570)
    ll1=Entry(log1,font=('default',18),fg="black",bg="gray76")
    ll1.insert(0,"username")
    ll1.place(x=70,y=200,width=250)
    ll2 = Entry(font=('arial', 18), fg="black", bg="gray76")
    ll2.insert(0,"password")
    ll2.place(x=70, y=250, width=250)
    b1=Button(log1,text="login",width=22,bg="cyan",command=loginto,fg="black",font=("bold",15)).place(x=69,y=300)
    ca=Canvas(log1,bg="black",width=400,height=2,).place(x=0,y=370)
    b1 = Button(log1, text="register", width=22,command=register, bg="green", fg="black", font=("bold", 15)).place(x=69, y=392)
    ca2 = Canvas(log1, bg="black", width=400, height=2, ).place(x=0, y=450)
def register():
    global a1,a2,a3
    log=Frame(bg="light cyan").place(x=0,y=0,width=400,height=670)
    log1=Frame(bg="gray36").place(x=0,y=180,width=400,height=570)
    a1=Entry(log1,font=('default',18),fg="blue",bg="gray76")
    a1.insert(0,"username")
    a1.place(x=70,y=200,width=250)
    a2 = Entry(font=('arial', 18), fg="blue2", bg="gray76")
    a2.insert(0,"password")
    a2.place(x=70, y=250, width=250)
    a3 = Entry(font=('arial', 18), fg="blue2", bg="gray76")
    a3.insert(0, "confirm password")
    a3.place(x=70, y=300, width=250)
    b1=Button(log1,text="register",width=22,bg="green",fg="black",command=registration,font=("bold",15)).place(x=69,y=350)
    ca=Canvas(log1,bg="black",width=400,height=2,).place(x=0,y=420)
    b1 = Button(log1, text="login", width=22, bg="cyan",command=login, fg="black", font=("bold", 15)).place(x=69, y=442)
    ca2 = Canvas(log1, bg="black", width=400, height=2, ).place(x=0, y=500)
login()
main.mainloop()
