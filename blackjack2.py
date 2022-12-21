from tkinter import *
import random
import time

win = Tk()
win.minsize(845,500)
win.maxsize(845,500)
win.title("BlackJack")
win.iconbitmap('l.ico')
win.configure(bg="#3ab503")

dw=0
pw=0

dealertotal=0
playertotal=0

def delay():
    time.sleep(2)

def dest(event=None):
    top.destroy()
    win.unbind("<space>")
    replay()

def oncross():
    top.destroy()
    replay()

def wincheck():
    global dw,pw,playerscore,pcscore,d1i,d2i,d3i,d1,d2,top
    ddif=21-dealertotal
    pdif=21-playertotal
    print("\nstartwincheck\ndealerhand= ",dealerh,"\nplayerhand= ",playerhand)
    print("dealer : ", dw, "player",pw)
    print("d: ", dealertotal,"p:", playertotal,"\nEnd wincheck")
    points="PC: "+ str(dealertotal)+ ", You: "+ str(playertotal)
    end=False
    message=""
    if playertotal>21 and dealertotal>21:
        print("Both bust lose\n")
        message="Both bust lose"
        end=True
    elif playertotal>21:
        print("Player Bust lose\n")
        message="Player Bust lose"
        dw+=1
        end=True
    elif dealertotal>21:
        print("Dealer bust lose\n")
        message="Dealer bust lose"
        pw+=1
        end=True
    elif playertotal==21 and dealertotal==21:
        print("draw\n")
        message="draw"
        end=True
    elif playertotal==21:
        print("Player wins\n")
        message="Player wins"
        pw+=1
        end=True
    elif dealertotal==21:
        print("Dealer wins\n")
        message="Dealer wins"
        dw+=1
        end=True
    elif ddif<pdif:
        print("Dealer wins\n")
        message="Dealer wins"
        dw+=1
        end=True
    elif pdif<ddif:
        print("Player wins\n")
        message="Player wins"
        pw+=1
        end=True
    elif playertotal==dealertotal:
        print("draw\n")
        message="draw"
        end=True
    playerscore.config(text=pw)
    pcscore.config(text=dw)
    
    if end==True:
        if len(dealerh)==4:
            d1.config(image=d2i)
            d2.config(image=d3i)
            d3.config(image=d4i)
        if len(dealerh)==3:
            d1.config(image=d2i)
            d2.config(image=d3i)
        else:
            d1.config(image=d2i)
    try:
        if top:
            top.destroy()
    except:
        print("nothing found")
    top=Toplevel(win)
    Label(top, text=message,font=("Courier", 20, "bold")).pack()
    Label(top, text=points,font=("Courier", 10, "bold")).pack()
    Label(top, text="Press <Space> for New Game",font=("Courier", 10, "bold")).pack()
    top.protocol("WM_DELETE_WINDOW", oncross)
    win.bind('<space>', dest)
        
    
    

def stop():
    global hold, dealerhand,playerhand, dealertotal,playertotal
    hold=True
    for i in range(len(dealerh),3):
        dealerh.append(card[i])
    for i in range(len(dealerhand),3):
        dealerhand.append(card[i])
        if i==1:
            d1.config(image=d2i)
        elif i==2:
            d2.config(image=d3i)
        elif i==3:
            d3.config(image=d4i)
    dealertotal=0
    for i in dealerh:
        if isinstance(i[0], int):
            dealertotal+=i[0]
        elif i[0] in face10:
            dealertotal+=10
        else:
            dealertotal+=11
    playertotal=0
    for i in playerhand:
        if isinstance(i[0], int):
            playertotal+=i[0]
        elif i[0] in face10:
            playertotal+=10
        else:
            playertotal+=11

    wincheck()
face10=['j','q','k']
def dealCard():
    global t, dealerhand,playerhand, dealertotal,playertotal
    if len(playerhand)>=4:
        return wincheck()
    if len(playerhand)<5 and hold==False:
        if t==1:
            if len(playerhand)<4:
                playerhand.append(card[len(playerhand)+4])
                dealerh.append(card[len(dealerh)])
            dealerhand.append(card[len(dealerhand)])
            if len(playerhand)==3:
                if hold==False:
                    p2.config(image=p3i)
                d1.config(image=d2i)
            elif len(playerhand)==4 and len(dealerhand)==3:
                if hold==False:
                    p3.config(image=p4i)
                d2.config(image=d3i)
            else:
                d3.config(image=d4i)
    else:
        print("exit")
        
    dealertotal=0
    for i in dealerh:
        if isinstance(i[0], int):
            dealertotal+=i[0]
        elif i[0] in face10:
            dealertotal+=10
        else:
            dealertotal+=11

    playertotal=0
    for i in playerhand:
        if isinstance(i[0], int):
            playertotal+=i[0]
        elif i[0] in face10:
            playertotal+=10
        else:
            playertotal+=11
    
    if playertotal==21 or dealertotal==21:
        wincheck()
    elif playertotal>21 or dealertotal>21:
        wincheck()
    elif len(playerhand)==4:
        wincheck()
    print("\ndealerhand= ",dealerh,"\nplayerhand= ",playerhand,"\n")
    print("dealer: ", dealertotal, "player: ", playertotal)

t=1
hold=False
card=[]
def distribute_cards():
    global card
    deck = [[2,3,4,5,6,7,8,9,10,'j', 'q', 'k', 'a'],[2,3,4,5,6,7,8,9,10,'j', 'q', 'k', 'a'],[2,3,4,5,6,7,8,9,10,'j', 'q', 'k', 'a'],[2,3,4,5,6,7,8,
    9,10,'j', 'q', 'k', 'a'],[2,3,4,5,6,7,8,9,10,'j', 'q', 'k', 'a']]
    a=random.Random()
    card=[]
    for _ in range(8):
        i=random.randint(0,3)
        cur=[]
        c=random.choice(deck[i])
        cur.append(c)
        deck[i].remove(c)
        cur.append(i)
        card.append(cur)
    print(card)
    name=[]
    for i in card:
        n="cards/"
        if i[1]==0:
            n+="p"+str(i[0])+".png"
        elif i[1]==1:
            n+="d"+str(i[0])+".png"
        elif i[1]==2:
            n+="h"+str(i[0])+".png"
        elif i[1]==3:
            n+="t"+str(i[0])+".png"
        name.append(n)
    return name

name=distribute_cards()

def replay():
    global name, d1i,d2i,d3i,d4i,p1i,p2i,p3i,p4i,hold, dealerhand,playerhand,dealerh, dealertotal,playertotal
    dealertotal=0
    playertotal=0
    name=distribute_cards()
    hold=False
    
    dealerhand=card[:1]
    dealerh=card[:2]
    playerhand=card[4:6]

    d1i=PhotoImage(file=name[0])
    d2i=PhotoImage(file=name[1])
    d3i=PhotoImage(file=name[2])
    d4i=PhotoImage(file=name[3])

    p1i=PhotoImage(file=name[4])
    p2i=PhotoImage(file=name[5])
    p3i=PhotoImage(file=name[6])
    p4i=PhotoImage(file=name[7])
    
    da.config(image=d1i)
    d1.config(image=back)
    d2.config(image=back)
    d3.config(image=back)

    pa.config(image=p1i)
    p1.config(image=p2i)
    p2.config(image=back)
    p3.config(image=back)
    
	
print(card)
print(card[4:6])
dealerhand=card[:1]
dealerh=card[:2]
playerhand=card[4:6]

#back=(129,193)
#cards=(137,201)

back=PhotoImage(file="cards/3.png")

d1i=PhotoImage(file=name[0])
d2i=PhotoImage(file=name[1])
d3i=PhotoImage(file=name[2])
d4i=PhotoImage(file=name[3])

p1i=PhotoImage(file=name[4])
p2i=PhotoImage(file=name[5])
p3i=PhotoImage(file=name[6])
p4i=PhotoImage(file=name[7])

da=Label(win,text="", image=d1i, bg="#3ab503")
da.grid(row=0, column=0)
d1=Label(win,text="", image=back, bg="#3ab503")
d1.grid(row=0, column=1)
d2=Label(win,text="", image=back, bg="#3ab503")
d2.grid(row=0, column=2)
d3=Label(win,text="", image=back, bg="#3ab503")
d3.grid(row=0, column=3)

bar=Label(win,bg="black",width=120, height=2)
bar.grid(row=1, column=0, rowspan=2, columnspan=6)
bar2=Label(win,bg="red",width=20, height=3)
bar2.grid(row=1, column=2, rowspan=2)

Boldsbfont=('Segoe UI', 15, 'bold')
B=('Segoe UI', 23, 'bold')
Buttonfont=('Segoe UI', 10, 'bold')

scoreboard=Label(win, text="PC", font=Boldsbfont, fg="white", bg="RED")
scoreboard.grid(row=1, column=2, sticky='w', padx=7)
pcscore=Label(win, text="0", font=B, fg="white", bg="RED")
pcscore.grid(row=1, column=2, rowspan=2)

bar3=Label(win,bg="gold",width=20, height=3)
bar3.grid(row=1, column=3, rowspan=2)

playerscore=Label(win, text="1", font=B, bg="gold")
playerscore.grid(row=1, column=3, rowspan=2)
scoreboard=Label(win, text="You", font=Boldsbfont, bg="gold")
scoreboard.grid(row=2, column=3, sticky='e', padx=7)

Lb=Button(win,text="Draw", bg="light blue",fg="black", font=Buttonfont, activebackground="white",activeforeground="light blue", width=12, height=2, command=dealCard)
Lb.grid(row=3,column=0, columnspan=2)
Lb=Button(win,text="Hold", bg="Yellow",fg="black", font=Buttonfont, activebackground="white",activeforeground="yellow", width=12, height=2, command=stop)
Lb.grid(row=4,column=0, columnspan=2)
Lb=Button(win,text="Play Again", bg="red",fg="black", font=Buttonfont, activebackground="white",activeforeground="red", width=12, height=2, command=replay)
Lb.grid(row=5,column=0, columnspan=2)


pa=Label(win,text="", image=p1i, bg="#3ab503")
pa.grid(row=3, column=2, rowspan=3)
p1=Label(win,text="", image=p2i, bg="#3ab503")
p1.grid(row=3, column=3, rowspan=3)
p2=Label(win,text="", image=back, bg="#3ab503")
p2.grid(row=3, column=4, rowspan=3)
p3=Label(win,text="", image=back, bg="#3ab503")
p3.grid(row=3, column=5, rowspan=3)


win.mainloop()

