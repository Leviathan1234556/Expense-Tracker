import csv
import os
import mysql.connector as m
try:
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure 
except ImportError:
    os.system('pip install matplotlib')
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure
try:
    import numpy
except ImportError:
    os.system('pip install numpy')
    import numpy
try:
    import customtkinter as tk
except ImportError:
    os.system('pip install customtkinter')
    import customtkinter as tk
try:
    import webbrowser
except ImportError:
    os.system('pip install webbrowser')
    import webbrowser
import math
from tkinter import *
from tkinter import ttk, PhotoImage, messagebox, Canvas
import datetime
from dateutil.relativedelta import relativedelta
import tkinter.font as font
import sv_ttk
new =tk.CTk()
new.title('Expense Tracker')
new.state('zoomed')
image_icon=PhotoImage(file="budget.png")
new.iconphoto(False,image_icon)
tk.set_appearance_mode("dark")  
tk.set_default_color_theme("blue")
label = tk.CTkLabel(master=new, text='MySQL Password:')
Font_tuple = ('default',20)
label.configure(font=Font_tuple)
label.place(x=450,y=325)
entry = tk.CTkEntry(master=new, textvariable=tk.StringVar(), width=175, height=75)
entry.configure(font=Font_tuple)
entry.place(x=700 ,y=300)
upload = PhotoImage(file='upload.png')
nquit = PhotoImage(file='leave.png')
newfont = ('default',15)
def tracker():
    root = tk.CTkToplevel(new)
    root.title('Expense Tracker')
    root.state('zoomed')
    image_icon=PhotoImage(file="budget.png")
    root.iconphoto(False,image_icon)
    password = entry.get()
    mycon = m.connect(host = "localhost",user = "root",passwd = password)
    mycur = mycon.cursor()
    mycur.execute('create database if not exists expense_tracker;')
    mycur.execute('use expense_tracker;')
    mycur.execute('create table if not exists tracker(Date char(10), Expense char(25), Category char(25), Amount int(10), Balance int(10));')
    tot_amount = 0
    temp = 0
    def totalamount():
        global tot_amount
        global temp
        top = tk.CTkToplevel(root)
        top.title('Total amount:')
        top.state('zoomed')
        image_icon=PhotoImage(file="budget.png")
        top.iconphoto(False,image_icon)
        label= tk.CTkLabel(top, text='Total amount', text_font=Font_tuple)
        label.place(x=500,y=325)
        labelbox = tk.CTkEntry(master=top, textvariable=tk.StringVar(),width=175, height=75)
        labelbox.configure(font=Font_tuple)
        labelbox.place(x=700 ,y=300)
        def quitagain():
            top.destroy()
        def submit():
            with open('Check.txt','w') as f:
                labelval = labelbox.get()
                f.write(labelval)
        nsmlframe = tk.CTkFrame(master=top)
        nsmlframe.configure(height=100,width=200)
        nsmlframe.place(x=550, y=500)
        nnsmlframe = tk.CTkFrame(master=top)
        nnsmlframe.configure(height=100,width=200)
        nnsmlframe.place(x=850, y=500)
        submi = tk.CTkButton(master=nsmlframe, text='Submit', command=submit, text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1a592b",border_color="#1a592b", image=upload,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
        submi.place(x=10, y=10)
        button = tk.CTkButton(master=nnsmlframe, text='Quit',command=quitagain, text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1a592b",border_color="#1a592b", image=nquit,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
        button.place(x=10, y=10)
        mycur.execute('select * from tracker;')
        fetch = mycur.fetchall()
        tot_amount = 0
        if fetch == []:
            with open('Check.txt', 'r') as f:
                tot_amount = int(f.read())
                temp = tot_amount
        else:
            tot_amount = fetch[-1][-1]
            with open('Check.txt', 'r') as f:
                temp = f.read()
                temp = int(temp)
    def quit():
        root.destroy()
        new.destroy()
    def create():
        global tot_amount
        global temp
        mycur.execute('select * from tracker;')
        fetch = mycur.fetchall()
        tot_amount = 0
        if fetch == []:
            with open('Check.txt', 'r') as f:
                tot_amount = int(f.read())
                temp = tot_amount
        else:
            tot_amount = fetch[-1][-1]
            with open('Check.txt', 'r') as f:
                temp = f.read()
                temp = int(temp)
        top =tk.CTkToplevel(root)
        top.title('Enter Transaction')
        top.state('zoomed')
        image_icon=PhotoImage(file="budget.png")
        top.iconphoto(False,image_icon)
        date = tk.CTkLabel(master=top, text='Date(YYYY-MM-DD):', text_font=Font_tuple)
        date.place(x=430, y=70)
        datebox = tk.CTkEntry(master=top, textvariable=tk.StringVar(),width=175, height=75, text_font=Font_tuple)
        datebox.place(x=700, y=50)
        expense = tk.CTkLabel(master=top, text="Expense:", text_font=Font_tuple)
        expense.place(x=550,y=170)
        expensebox = tk.CTkEntry(master=top, textvariable=tk.StringVar(),width=175, height=75, text_font=Font_tuple)
        expensebox.place(x=700,y=150)
        category = tk.CTkLabel(master=top, text='Category of expense(like entertainment, food,...):', text_font=Font_tuple)
        category.place(x=120, y=270)
        categorybox = tk.CTkEntry(master=top, textvariable=tk.StringVar(),width=175, height=75, text_font=Font_tuple)
        categorybox.place(x=700, y=250)
        amount = tk.CTkLabel(master=top, text='Amount:', text_font=Font_tuple)
        amount.place(x=550,y=370)
        amountbox = tk.CTkEntry(master=top, textvariable=tk.IntVar(),width=175, height=75, text_font=Font_tuple)
        amountbox.place(x=700,y=350)
        def buton_func():
            global tot_amount
            datevalue = datebox.get()
            expensevalue = expensebox.get()
            categoryvalue = categorybox.get()
            amountvalue = amountbox.get()
            tot_amount = tot_amount - int(amountvalue)
            st = "insert into tracker values('{}','{}','{}',{},{})".format(datevalue, expensevalue, categoryvalue, amountvalue, tot_amount)
            label = tk.CTkLabel(master=top, text='Record added successfully!',text_font=Font_tuple)
            label.place(x=600,y=500)
            mycur.execute(st)
            mycon.commit()
        def quit2():
            top.destroy()
        nsmlframe = tk.CTkFrame(master=top)
        nsmlframe.configure(height=100,width=200)
        nsmlframe.place(x=530, y=600)
        nnsmlframe = tk.CTkFrame(master=top)
        nnsmlframe.configure(height=100,width=200)
        nnsmlframe.place(x=830, y=600)
        button = tk.CTkButton(master=nsmlframe, text='Submit',command=buton_func, text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1a592b",border_color="#1a592b", image=upload,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
        button.place(x=10, y=10)
        button_d = tk.CTkButton(master=nnsmlframe, text='Quit', command=quit2, text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1a592b",border_color="#1a592b", image=nquit,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
        button_d.place(x=10, y=10)
    def display():
        global tot_amount
        global temp
        mycur.execute('select * from tracker;')
        fetch = mycur.fetchall()
        tot_amount = 0
        if fetch == []:
            with open('Check.txt', 'r') as f:
                tot_amount = int(f.read())
                temp = tot_amount
        else:
            tot_amount = fetch[-1][-1]
            with open('Check.txt', 'r') as f:
                temp = f.read()
                temp = int(temp)
        top = tk.CTkToplevel(root)
        top.title('Display details')
        top.state('zoomed')
        image_icon=PhotoImage(file="budget.png")
        top.iconphoto(False,image_icon)
        mycur.execute('select * from tracker;')
        fetch = mycur.fetchall()
        label1 = tk.CTkLabel(master=top, text='Total amount: '+str(temp), text_font=Font_tuple)
        label1.place(x=540, y=0)
        frn = tk.CTkFrame(master=top)
        frn.place(x=0,y=100)
        style = ttk.Style()
        style.configure('Treeview', rowheight=40)
        sv_ttk.set_theme('dark')
        tv = ttk.Treeview(frn, columns = (1,2,3,4,5), show='headings', selectmode='browse')
        tv.pack()
        tv.column('#1', stretch=NO, width=400)
        tv.column('#2', stretch=NO, width=400)
        tv.column('#3', stretch=NO, width=400)
        tv.column('#4', stretch=NO, width=400)
        tv.column('#5', stretch=NO, width=400)
        tv.heading(1, text='Date')
        tv.heading(2, text='Expense')
        tv.heading(3, text='Category')
        tv.heading(4, text='Amount')
        tv.heading(5, text='Balance')
        for i in fetch:
            tv.insert('','end', values=i)
        label2 = tk.CTkLabel(master=top, text='Total balance: '+str(fetch[-1][-1]), text_font=Font_tuple)
        label2.place(x=540, y=40)
        def quit3():
            top.destroy()
        button_l = tk.CTkButton(master=top, text='Quit', command=quit3, text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1a592b",border_color="#1a592b", image=nquit,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
        button_l.place(x=600, y=600)
    def report1():
        top = tk.CTkToplevel(root)
        top.title('Enter date')
        top.state('zoomed')
        image_icon=PhotoImage(file="budget.png")
        top.iconphoto(False,image_icon)
        date1 = tk.CTkLabel(master=top, text='Date(YYYY-MM-DD):',text_font=Font_tuple)
        date1.place(x=475,y=325)
        datebox = tk.CTkEntry(master=top, textvariable=tk.StringVar(),text_font=Font_tuple,height=75,width=175 )
        datebox.place(x=750,y=300)
        nsmlframe = tk.CTkFrame(master=top)
        nsmlframe.configure(height=100,width=200)
        nsmlframe.place(x=530, y=600)
        nnsmlframe = tk.CTkFrame(master=top)
        nnsmlframe.configure(height=100,width=200)
        nnsmlframe.place(x=830, y=600)
        def table():
            newtop = tk.CTkToplevel(top)
            nnsmlframe = tk.CTkFrame(master=newtop)
            nnsmlframe.configure(height=100,width=200)
            nnsmlframe.place(x=650, y=600)
            newtop.title("That day's expense")
            newtop.state('zoomed')
            image_icon=PhotoImage(file="budget.png")
            newtop.iconphoto(False,image_icon)
            datevar = datebox.get()
            mycur.execute('select * from tracker where date="{}";'.format(datevar))
            fetch1 = mycur.fetchall()
            mycur.execute('select sum(Amount) from tracker where date="{}";'.format(datevar))
            fetch2 = mycur.fetchall()
            frn = tk.CTkFrame(newtop)
            frn.place(x=0,y=200)
            style = ttk.Style()
            sv_ttk.set_theme('dark')
            tv = ttk.Treeview(frn, columns = (1,2,3,4,5), show='headings')
            tv.pack()
            tv.column('#1', stretch=NO, width=400)
            tv.column('#2', stretch=NO, width=400)
            tv.column('#3', stretch=NO, width=400)
            tv.column('#4', stretch=NO, width=400)
            tv.column('#5', stretch=NO, width=400)
            tv.heading(1, text='Date')
            tv.heading(2, text='Expense')
            tv.heading(3, text='Category')
            tv.heading(4, text='Amount')
            tv.heading(5, text='Balance')
            for i in fetch1:
                tv.insert('','end', values=i)
            def quit6():
                newtop.destroy()
            label2 = tk.CTkLabel(master=newtop, text='Total balance: '+str(fetch1[-1][-1]), text_font=Font_tuple)
            label2.place(x=540, y=0)
            label3 = tk.CTkLabel(master=newtop, text='Total amount spent: '+str(fetch2[0][0]), text_font=Font_tuple)
            label3.place(x=500,y=40)
            button_l = tk.CTkButton(master=nnsmlframe, text='Quit', command=quit6, text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1a592b",border_color="#1a592b", image=nquit,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
            button_l.place(x=10, y=10)
        datebutton = tk.CTkButton(master=nsmlframe, text='Submit', command=table, text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1a592b",border_color="#1a592b", image=upload,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
        datebutton.place(x=10,y=10)
        def quit4():
            top.destroy()
        button_q = tk.CTkButton(master=nnsmlframe, text='Quit', command=quit4, text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1a592b",border_color="#1a592b", image=nquit,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
        button_q.place(x=10,y=10)
    def pie_chart():
        top = tk.CTkToplevel(root)
        top.title('Enter month')
        top.state('zoomed')
        image_icon=PhotoImage(file="budget.png")
        top.iconphoto(False,image_icon)
        month = tk.CTkLabel(master=top, text='Enter the month to get a overview of your expenses: ',text_font=Font_tuple)
        month.place(x=250,y=220)
        monthbox = tk.CTkEntry(master=top, textvariable=tk.IntVar(),width=175, height=75, text_font=Font_tuple)
        monthbox.place(x=850,y=200)
        nsmlframe = tk.CTkFrame(master=top)
        nsmlframe.configure(height=100,width=200)
        nsmlframe.place(x=530, y=600)
        nnsmlframe = tk.CTkFrame(master=top)
        nnsmlframe.configure(height=100,width=200)
        nnsmlframe.place(x=830, y=600)
        def write():
            newtop = tk.CTkToplevel(top)
            newtop.title('Pie Chart')
            newtop.state('zoomed')
            image_icon=PhotoImage(file="budget.png")
            newtop.iconphoto(False,image_icon)
            mycur.execute('select * from tracker where Date like "_____{}%";'.format(monthbox.get()))
            fetch = mycur.fetchall()
            with open('expense.csv','w',newline='') as f:
                writer = csv.writer(f)
                for i in fetch:
                    rec = [i[0],i[2], i[3]]
                    writer.writerow(rec)
            l = []
            with open('expense.csv','r',newline='') as f:
                d = {}
                reader = csv.reader(f)
                for i in reader:
                    l.append(i[1])
                for i in l:
                    d[i]=(l.count(i)/len(l))*100
                nl = []
                nper = []
                for i in d:
                    nl.append(i)
                    nper.append(d[i])
                graphtab = tk.CTkFrame(master=newtop)
                graphtab.pack()
                fig = Figure(facecolor='#134567', figsize=(17,10))
                ax = fig.add_subplot(111)
                ax.pie(nper, radius=1, labels=nl,autopct='%0.2f%%', shadow=True,)
                canvas = FigureCanvasTkAgg(fig, graphtab)
                canvas.get_tk_widget().pack()
                canvas.draw()
        def quit5():
            top.destroy()
        button_k = tk.CTkButton(master=nnsmlframe, text='Quit', command=quit5, text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1a592b",border_color="#1a592b", image=nquit,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
        button_a = tk.CTkButton(master=nsmlframe,text='Submit', command=write, text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1a592b",border_color="#1a592b", image=upload,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
        button_a.place(x=10, y=10)
        button_k.place(x=10,y=10)
    def incomevsspending():
        top = tk.CTkToplevel(root)
        top.title('Income vs Expense graph')
        top.state('zoomed')
        image_icon=PhotoImage(file="budget.png")
        top.iconphoto(False,image_icon)
        mycur.execute('select * from tracker;')
        with open('Income.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            fetch = mycur.fetchall()
            for i in fetch:
                l = [i[0]]
                writer.writerow(l)
        nl = {}
        with open('Income.csv', 'r', newline='') as f:
            reader = csv.reader(f)
            for i in reader:
                for j in i:
                    nl[j[5:7]] = None
        naml = []
        for i in nl:
            mycur.execute('select sum(Amount) from tracker where Date like "_____{}%";'.format(i))
            fetch = mycur.fetchall()
            for j in fetch:
                for k in j:
                    naml.append(k)
        nlm = []
        with open('Check.txt', 'r') as f:
            x = f.read()
            nlm.append(x)
            nlm = nlm*len(naml)
        income = []
        for i in nlm:
            income.append(int(i))
        width = 0.4
        values = numpy.arange(len(naml))
        spend = [i+width for i in values]
        month = []
        for i in nl:
            dict = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'Novermber', 12:'December'}
            if int(i) in dict:
                month.append(dict[int(i)])
        frame = tk.CTkFrame(master=top)
        frame.pack()
        fig = Figure(figsize=(17,10), dpi=100, facecolor='#134567')
        a = fig.add_subplot(111)
        a.bar(values, income, width, label='Income')
        a.bar(spend, naml, width, label='Expense')
        a.set_xticks(values, month)
        a.set_xticks(range(3))
        a.set_xlabel('Month')
        a.set_ylabel('Amount')
        a.legend()
        canvas = FigureCanvasTkAgg(fig, frame)
        canvas.get_tk_widget().pack()
        canvas.draw()
    def debt():
        new = tk.CTkToplevel(root)
        new.title('Loan calculator')
        new.state('zoomed')
        image_icon=PhotoImage(file="budget.png")
        new.iconphoto(False,image_icon)
        npayoff = PhotoImage(file='loan1.png')
        nmon = PhotoImage(file='salary.png')
        npri = PhotoImage(file='fiat-money.png')
        nsmlframe = tk.CTkFrame(master=new)
        nsmlframe.configure(height=300, width=395)
        nsmlframe.place(x=550,y=100)
        nnsmlframe = tk.CTkFrame(master=new)
        nnsmlframe.configure(width=200,height=100)
        nnsmlframe.place(x=600,y=600)
        def loanpayoff():
            payoff = tk.CTkToplevel(new)
            payoff.title('Loan free by')
            payoff.state('zoomed')
            image_icon=PhotoImage(file="budget.png")
            payoff.iconphoto(False,image_icon)
            nsmlframe = tk.CTkFrame(master=payoff)
            nsmlframe.configure(height=100,width=200)
            nsmlframe.place(x=530, y=600)
            nnsmlframe = tk.CTkFrame(master=payoff)
            nnsmlframe.configure(height=100,width=200)
            nnsmlframe.place(x=830, y=600)
            label0 = tk.CTkLabel(master=payoff, text='Date(YYYY-MM-DD):',text_font=Font_tuple)
            label = tk.CTkLabel(master=payoff, text='Loan principal:',text_font=Font_tuple)
            label1 = tk.CTkLabel(master=payoff, text='Monthly payment:',text_font=Font_tuple)
            label2 = tk.CTkLabel(master=payoff, text='Loan Interest:',text_font=Font_tuple)
            entry0 = tk.CTkEntry(master=payoff, textvariable=tk.StringVar(),width=175,height=75,text_font=Font_tuple)
            entry = tk.CTkEntry(master=payoff, textvariable=tk.IntVar(),width=175,height=75,text_font=Font_tuple)
            entry1 = tk.CTkEntry(master=payoff, textvariable=tk.IntVar(),width=175,height=75,text_font=Font_tuple)
            entry2 = tk.CTkEntry(master=payoff, textvariable=tk.StringVar(),width=175,height=75,text_font=Font_tuple)
            label0.place(x=450,y=70)
            label.place(x=510, y=170)
            label1.place(x=480,y=270)
            label2.place(x=530,y=370)
            entry0.place(x=700,y=50)
            entry.place(x=700,y=150)
            entry1.place(x=700,y=250)
            entry2.place(x=700,y=350)
            def submit():
                d = entry0.get()
                cb = entry.get()
                mp = entry1.get()
                ir = entry2.get()
                i = float(ir)/(12*100)
                print(i)
                nm = math.log(float(mp)/(float(mp)-i*float(cb)),1+i)
                y = (math.ceil(nm))//12
                m = (math.ceil(nm))%12
                year = datetime.datetime(int(d[:4]), int(d[5:7]), int(d[-2:]))
                date = year + relativedelta(months = int(m))
                n = date + relativedelta(years=int(y))
                messagebox.showinfo('Loan free by', 'Loan free by '+ str(n.year) +'-'+ str(n.month)+'-'+str(n.day))
            def quit50():
                payoff.destroy()
            quit10 = tk.CTkButton(master=nsmlframe, text='Quit', command=quit50, text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1a592b",border_color="#1a592b", image=nquit,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
            quit10.place(x=10,y=10)
            submi = tk.CTkButton(master=nnsmlframe, text='Submit', command=submit, text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1a592b",border_color="#1a592b", image=upload,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
            submi.place(x=10,y=10)
        def monthlypayment():
            monthly = tk.CTkToplevel(new)
            monthly.title('Annuity monthly payment amount')
            monthly.state('zoomed')
            nsmlframe = tk.CTkFrame(master=monthly)
            nsmlframe.configure(height=100,width=200)
            nsmlframe.place(x=530, y=600)
            nnsmlframe = tk.CTkFrame(master=monthly)
            nnsmlframe.configure(height=100,width=200)
            nnsmlframe.place(x=830, y=600)
            image_icon=PhotoImage(file="budget.png")
            monthly.iconphoto(False,image_icon)
            label = tk.CTkLabel(master=monthly, text='Loan principal:',text_font=Font_tuple)
            label1 = tk.CTkLabel(master=monthly, text='No. of periods:',text_font=Font_tuple)
            label2 = tk.CTkLabel(master=monthly, text='Loan Interest:',text_font=Font_tuple)
            entry = tk.CTkEntry(master=monthly, textvariable=tk.IntVar(),width=175,height=75,text_font=Font_tuple)
            entry1 = tk.CTkEntry(master=monthly, textvariable=tk.IntVar(),width=175,height=75,text_font=Font_tuple)
            entry2 = tk.CTkEntry(master=monthly, textvariable=tk.StringVar(),width=175,height=75,text_font=Font_tuple)
            label.place(x=560,y=170)
            label1.place(x=560,y=270)
            label2.place(x=560,y=370)
            entry.place(x=750,y=150)
            entry1.place(x=750,y=250)
            entry2.place(x=750,y=350)
            def submit():
                cb = entry.get()
                np = entry1.get()
                ir = entry2.get()
                i = float(ir)/(12*100)
                annuity = float(cb)*((float(i)*(1+float(i))**float(np))/((1+float(i))**float(np)-1))
                mp = math.ceil(annuity)
                messagebox.showinfo('Monthly Payment', 'Monthly Payment is '+ u'\u20B9' +str(mp))
            def quit50():
                monthly.destroy()
            quit10 = tk.CTkButton(master=nnsmlframe, text='Quit', command=quit50, text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1a592b",border_color="#1a592b", image=nquit,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
            quit10.place(x=10,y=10)
            submi = tk.CTkButton(master=nsmlframe, text='Submit', command=submit, text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1a592b",border_color="#1a592b", image=upload,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
            submi.place(x=10,y=10)
        def principal():
            princi = tk.CTkToplevel(new)
            princi.title('Loan principal')
            princi.state('zoomed')
            nsmlframe = tk.CTkFrame(master=princi)
            nsmlframe.configure(height=100,width=200)
            nsmlframe.place(x=530, y=600)
            nnsmlframe = tk.CTkFrame(master=princi)
            nnsmlframe.configure(height=100,width=200)
            nnsmlframe.place(x=830, y=600)
            image_icon=PhotoImage(file="budget.png")
            princi.iconphoto(False,image_icon)
            label = tk.CTkLabel(master=princi, text='Annuity principal:',text_font=Font_tuple)
            label1 = tk.CTkLabel(master=princi, text='No. of periods:',text_font=Font_tuple)
            label2 = tk.CTkLabel(master=princi, text='Loan Interest:',text_font=Font_tuple)
            entry = tk.CTkEntry(master=princi, textvariable=tk.IntVar(),height=75,width=175,text_font=Font_tuple)
            entry1 = tk.CTkEntry(master=princi, textvariable=tk.IntVar(),height=75,width=175,text_font=Font_tuple)
            entry2 = tk.CTkEntry(master=princi, textvariable=tk.StringVar(),height=75,width=175,text_font=Font_tuple)
            label.place(x=530,y=170)
            label1.place(x=560,y=270)
            label2.place(x=560, y=370)
            entry.place(x=750,y=150)
            entry1.place(x=750,y=250)
            entry2.place(x=750,y=350)
            def submit():
                mp = float(entry.get())
                np = float(entry1.get())
                ir = float(entry2.get())
                i = ir/(12*100)
                principa = mp/((i*(1+i)**np)/((1+i)**np-1))
                realprincipa = round(principa)
                messagebox.showinfo('Loan principal', 'Loan principal is '+ u'\u20B9' +str(realprincipa))
            def quit50():
                princi.destroy()
            quit10 = tk.CTkButton(master=nnsmlframe, text='Quit', command=quit50, text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1a592b",border_color="#1a592b", image=nquit,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
            quit10.place(x=10,y=10)
            submi = tk.CTkButton(master=nsmlframe, text='Submit', command=submit, text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1a592b",border_color="#1a592b", image=upload,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
            submi.place(x=10,y=10)
        button = tk.CTkButton(master=nsmlframe, text='Loan free by', command=loanpayoff,text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#484876",border_color="#484876", image=npayoff,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
        button1 = tk.CTkButton(master=nsmlframe, text='Annuity monthly payment amount', command=monthlypayment,text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#484876",border_color="#484876", image=nmon,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
        button2 = tk.CTkButton(master=nsmlframe, text='Loan principal', command=principal,text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#484876",border_color="#484876", image=npri,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
        def quitnew():
            new.destroy()
        button3 = tk.CTkButton(master=nnsmlframe, text='Quit', command=quitnew,text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#D35B58",border_color="#D35B58", image=nquit,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
        button.place(x=10, y=10)
        button1.place(x=10, y=110)
        button2.place(x=10, y=210)
        button3.place(x=10, y=10)
    details = PhotoImage(file='gross.png')
    ndetails = PhotoImage(file='list.png')
    ndisplay = PhotoImage(file='accounts.png')
    graph = PhotoImage(file='expenses.png')
    ngraph = PhotoImage(file='bar-chart.png')
    loan = PhotoImage(file ='loan.png')
    idea = PhotoImage(file='idea.png')
    frameCnt = 60
    frames = [PhotoImage(file='download.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
    frames1 = [PhotoImage(file='download1.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        label.configure(image=frame)
        root.after(100, update, ind)
    def update1(ind):
        frame = frames1[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        nlabel.configure(image=frame)
        root.after(100, update1, ind)
    label = tk.CTkLabel(master = root)
    label.place(x=540,y=0)
    root.after(0, update, 0)
    nlabel = tk.CTkLabel(master = root)
    nlabel.place(x=540,y=92)
    root.after(0, update1, 0)
    with open('Check.txt', 'r') as f:
        x = f.readlines()
        if x == []:
            gframe = tk.CTkFrame(master=root, width=275, height=300, corner_radius=15)
            gframe.place(x=400, y=200)
            nframe = tk.CTkFrame(master=root, width=550,height=300, corner_radius=15)
            nframe.place(x=800, y=200)
            smlframe = tk.CTkFrame(master=root)
            smlframe.place(x=30, y=250)
            smlframe.configure(height=100, width=260)
            button = tk.CTkButton(master=smlframe,
             text='Enter total amount',
              command=totalamount, text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1f6aa5",border_color='#1f6aa5', image=details,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
            button.place(x=10, y=10)
            button1 = tk.CTkButton(master=gframe,
             text='Enter Transaction', 
             command=create, text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1f6aa5",border_color='#1f6aa5', image=ndetails,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
            button1.place(x=10, y=10)
            button2 = tk.CTkButton(master=gframe, 
            text='Display', 
            command=display, 
            text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1f6aa5",border_color='#1f6aa5', image=ndisplay,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
            button2.place(x=10, y=110)
            button3 = tk.CTkButton(master=gframe, 
            text='Expense of that day', 
            command=report1, text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1f6aa5",border_color='#1f6aa5', image=ndisplay,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
            button3.place(x=10, y=210)
            button4 = tk.CTkButton(master=nframe, 
            text='Graphical representation of expenses of that month', 
            command=pie_chart, 
            text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1f6aa5",border_color='#1f6aa5', image=graph,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
            button4.place(x=10, y=10)
            button6 = tk.CTkButton(master=nframe, 
            text='Income vs Expense graph of the year', 
            command=incomevsspending, 
            text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1f6aa5",border_color='#1f6aa5', image=ngraph,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
            button6.place(x=10, y=110)
            button7 = tk.CTkButton(master=nframe, 
            text='Loan calculator', 
            command=debt, 
            text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1f6aa5",border_color='#1f6aa5', image=loan,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
            button7.place(x=10, y=210)
            nsmlframe = tk.CTkFrame(master=root)
            nsmlframe.place(x=500, y=600)
            nsmlframe.configure(height=100, width=200)
            button8 = tk.CTkButton(master=nsmlframe, 
            text='Quit', 
            command=quit, 
            text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#D35B58",border_color="#D35B58", image=nquit,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
            button8.place(x=10, y=10)
        else:
            ngframe = tk.CTkFrame(master=root, width=275, height=300, corner_radius=15)
            ngframe.place(x=350, y=200)
            gnframe = tk.CTkFrame(master=root, width=550,height=300, corner_radius=15)
            gnframe.place(x=800, y=200)
            button1 = tk.CTkButton(master=ngframe,
             text='Enter Transaction', 
             command=create, text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1f6aa5",border_color='#1f6aa5', image=ndetails,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
            button1.place(x=10, y=10)
            button2 = tk.CTkButton(master=ngframe, 
            text='Display', 
            command=display, 
            text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1f6aa5",border_color='#1f6aa5', image=ndisplay,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
            button2.place(x=10, y=110)
            button3 = tk.CTkButton(master=ngframe, 
            text='Expense of that day', 
            command=report1, text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1f6aa5",border_color='#1f6aa5', image=ndisplay,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
            button3.place(x=10, y=210)
            button4 = tk.CTkButton(master=gnframe, 
            text='Graphical representation of expenses of that month', 
            command=pie_chart, 
            text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1f6aa5",border_color='#1f6aa5', image=graph,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
            button4.place(x=10, y=10)
            button6 = tk.CTkButton(master=gnframe, 
            text='Income vs Expense graph of the year', 
            command=incomevsspending, 
            text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1f6aa5",border_color='#1f6aa5', image=ngraph,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
            button6.place(x=10, y=110)
            button7 = tk.CTkButton(master=gnframe, 
            text='Loan calculator', 
            command=debt, 
            text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1f6aa5",border_color='#1f6aa5', image=loan,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
            button7.place(x=10, y=210)
            nsmlframe = tk.CTkFrame(master=root)
            nsmlframe.place(x=500, y=600)
            nsmlframe.configure(height=100, width=200)
            button8 = tk.CTkButton(master=nsmlframe, 
            text='Quit', 
            command=quit, 
            text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#D35B58",border_color="#D35B58", image=nquit,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
            button8.place(x=10, y=10)
    def tipsfunc():
        tiplevel = tk.CTkToplevel(root)
        tiplevel.title('Financial Tips')
        tiplevel.state('zoomed')
        ntipframe = tk.CTkFrame(master=tiplevel)
        ntipframe.place(x=550, y=200)
        ntipframe.configure(height=240, width=450)
        image_icon=PhotoImage(file="budget.png")
        tiplevel.iconphoto(False,image_icon)
        label1 = tk.CTkLabel(master=ntipframe, text='Financial tips:',text_font=Font_tuple)
        label1.place(x=150, y=10)
        label2 = tk.CTkLabel(master=ntipframe, text='1.Create A Budget \n2.Use Cash Instead Of Plastic Money \n3.Create An Emergency Fund \n4.Avoid Taking On Debt \n5.Start Investing', text_font=Font_tuple)
        label2.place(x=10, y=60)
        browser = PhotoImage(file='internet.png')
        def url():
            nurl = 'https://mint.intuit.com/blog/planning/money-101-27-financial-tips-to-live-by/'
            webbrowser.open_new_tab(nurl)
        nntipframe = tk.CTkFrame(master=tiplevel)
        nntipframe.place(x=500,y=600 )
        nntipframe.configure(height=100, width=200)
        moretips = tk.CTkButton(master=nntipframe,text='More tips', command=url,text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#1f6aa5",border_color='#1f6aa5', image=browser,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
        nsmlframe = tk.CTkFrame(master=tiplevel)
        nsmlframe.place(x=750, y=600)
        nsmlframe.configure(height=100, width=200)
        def quit():
            tiplevel.destroy()
        button8 = tk.CTkButton(master=nsmlframe, 
                                text='Quit', 
                                command=quit, 
                                text_color="white",
                                  hover= True,
                                  width = 175, corner_radius=5,
                                  border_width=2,fg_color=None, hover_color="#D35B58",border_color="#D35B58", image=nquit,height=75,
                                  bg_color="#262626",  compound="right", text_font=newfont)
        moretips.place(x=10, y=10)
        button8.place(x=10,y=10)
    tips = tk.CTkFrame(master=root)
    tips.place(x=725, y=600)
    tips.configure(height=100, width=210)
    tipbutton = tk.CTkButton(master=tips,text='Financial tips', command=tipsfunc,text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#D35B58",border_color="#D35B58", image=idea,height=75,
              bg_color="#262626",  compound="right", text_font=newfont)
    tipbutton.place(x=10,y=10)
submit = tk.CTkButton(master=new, text='Submit', command=tracker,
            text_color="white",
              hover= True,
              width = 175, corner_radius=5,
              border_width=2,fg_color=None, hover_color="#D35B58",border_color="#D35B58",height=75,
              bg_color="#262626",text_font=Font_tuple, image=upload, compound='right')
submit.place(x=635, y=400)
new.mainloop()