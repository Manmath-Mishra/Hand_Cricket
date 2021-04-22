from tkinter import *
from tkinter import messagebox
import random
import time
ballsleft=6
cballsleft=6
total=0  
ctotal=0  
def bat():
        
   
    def humanball():
        global ctotal
        global cballsleft
        humball= random.randint(1,6)
        comprun= random.randint(1,6)
        cscore.set(f"Computer scored {comprun} runs.")
        hbal.set(f"You bowled {humball}")
        ctotal+=comprun
        cballsleft-=1
        cr.set(f"{ctotal}             (Balls left :{cballsleft})")
        if humball==comprun and ctotal<total+1:
            cscore.set("Computer is bowled!!")
            cr.set(f"{ctotal-humball}             (Balls left :{cballsleft})")
            bowls.update()
            time.sleep(5)
            messagebox.showinfo("Result- WON!!!",f"Well played!!\nYou have won the match.")
            bowls.destroy()
        if cballsleft==0 and ctotal<total+1:
            cr.set(f"{ctotal}             (Balls left :{cballsleft})")
            bowls.update()
            time.sleep(5)
            messagebox.showinfo("Result- WON!!!","Well played!!\nYou have won the match.")
            bowls.destroy()
        if cballsleft!=0 and ctotal>=total+1:
            cr.set(f"{ctotal}             (Balls left :{cballsleft})")
            messagebox.showinfo("Result- LOST!!","Sorry!!\nYou have lost the match.")
            bowls.destroy()
    def humanrun():
        global total
        global ballsleft
        runs= random.randint(1,6)
        cballs= random.randint(1,6)
        hscore.set(f"You have scored {runs} runs.")
        cbal.set(f"Computer bowled {cballs}")
        total+=runs
        ballsleft-=1
        if runs==cballs:
            hscore.set("You are bowled!!")
            tr.set(f"{total-cballs}             (Balls left :{ballsleft})")
            bats.update()
            time.sleep(5)
            messagebox.showinfo("Result",f"Well played!!\nYou scored a total of {total-cballs}\nGet ready to bowl.")
            bats.destroy()
            
        tr.set(f"{total}             (Balls left :{ballsleft})")
        if ballsleft==0:
            tr.set(f"{total}             (Balls left :{ballsleft})")
            bats.update()
            time.sleep(5)
            messagebox.showinfo("Result",f"Well played!!\nYou scored a total of {total}\nGet ready to bowl.")
            bats.destroy()
            
    messagebox.showinfo("TOSS","You have chose to bat first.")
    root.destroy()
    bats= Tk()
    bats.geometry("600x400")
    bats.title("Hand Cricket BATTING innings")
    bats.config(bg="yellow")
    l3=Label(bats,text="Human Runs :",font="algerian 20 bold",fg="red")
    l3.place(x=40,y=70)
    hscore= StringVar()
    score= Entry(bats,textvariable=hscore,font="lucida 15")
    score.place(x=240,y=70)
    b3= Button(bats,text="Bat",font="lucida 15",command=humanrun)
    b3.place(x=500,y=70)
    l4=Label(bats,text="Total runs :",font="algerian 20 bold",fg="red")
    l4.place(x=40,y=140)
    tr=StringVar()
    totalrun=Entry(bats,textvariable=tr,font="lucida 15")
    totalrun.place(x=230,y=140)
    l5= Label(bats,text="Computer ball",font="algerian 20 bold",fg="red")
    l5.place(x=40,y=200)
    cbal= StringVar()
    computer=Entry(bats,textvariable=cbal,font="lucida 15")
    computer.place(x=270,y=200)
    bats.mainloop()
    bowls=Tk()
    bowls.geometry("600x400")
    bowls.title("Hand Cricket BOWLING innings")
    bowls.config(bg="yellow")
    l8=Label(bowls,text="Computer Runs :",font="algerian 20 bold",fg="red")
    l8.place(x=40,y=70)
    cscore= StringVar()
    compscore= Entry(bowls,textvariable=cscore,font="lucida 15")
    compscore.place(x=270,y=70)
    b7= Button(bowls,text="Bowl",font="lucida 15",command=humanball)
    b7.place(x=520,y=70)
    l9=Label(bowls,text="Total runs :",font="algerian 20 bold",fg="red")
    l9.place(x=40,y=140)
    cr=StringVar()
    comprun=Entry(bowls,textvariable=cr,font="lucida 15")
    comprun.place(x=230,y=140)
    l9= Label(bowls,text="Human ball",font="algerian 20 bold",fg="red")
    l9.place(x=40,y=200)
    hbal= StringVar()
    human=Entry(bowls,textvariable=hbal,font="lucida 15")
    human.place(x=270,y=200)
    l10= Label(bowls,text=f"Target - {total+1}",font="lucida 15",fg="red")
    l10.place(x=40,y=270)
def ball():
    messagebox.showinfo("TOSS","Feature not yet available pls try batting.")
    


root=Tk()
root.geometry("600x400")
root.title("Hand Cricket")
root.config(bg="green")
f= Frame(root,bg="grey")
f.pack(fill=BOTH)
l= Label(f,text="Welcome to toss",font="algerian 20 bold",fg="red")
l.pack(fill=BOTH)
l1= Label(root,text="Choose your innings:",font="lucida 14 bold")
l1.place(x=100,y=100)
b= Button(root,text="BOWLING",font="algerian 18",command=ball)
b1=Button(root,text="BATTING",font="algerian 18",command=bat)
b.place(x=120,y=170)
b1.place(x=300,y=170)
l2= Label(root,text="Rules of game:\n1.The game will be of 1 over.\n2.Maximum runs per ball is 6.\n3.If the opponent plays the same ball, you are out!.",font="lucida 15",bg="yellow")
l2.place(x=20,y=250)
root.mainloop()
