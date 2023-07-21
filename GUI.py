import tkinter
from main import queen, knight, pawngo, bishop, rook, output, board, king
from white_bot import bot
from change import show

window = tkinter.Tk()
window.geometry('400x400')
queenimg = tkinter.PhotoImage(file='figures/wq.png').subsample(3)
pawnimg = tkinter.PhotoImage(file='figures/wp.png').subsample(3)
knightimg = tkinter.PhotoImage(file='figures/wn.png').subsample(3)
bishiopimg = tkinter.PhotoImage(file='figures/wb.png').subsample(3)
rookimg = tkinter.PhotoImage(file='figures/wr.png').subsample(3)
kingimg = tkinter.PhotoImage(file='figures/wk.png').subsample(3)

bqueenimg = tkinter.PhotoImage(file='figures/bq.png').subsample(3)
bpawnimg = tkinter.PhotoImage(file='figures/bp.png').subsample(3)
bknightimg = tkinter.PhotoImage(file='figures/bk.png').subsample(3)
brookimg = tkinter.PhotoImage(file='figures/br.png').subsample(3)
bbishop = tkinter.PhotoImage(file='figures/bb.png').subsample(3)
bking = tkinter.PhotoImage(file='figures/bk.png').subsample(3)
c = False
click = True
l = []
x1 = 0
y1 = 0
for y in range(0, 8):
    c = not c
    q = []
    for x in range(0, 8):
        if c == True:
            b = tkinter.Button(window, bg='white', fg='Blue')
            b.configure(command=lambda x1=x, y1=y: ch(x1, y1))
            b.place(x=50 * x, y=50 * y, width=50, height=50)
            c = False
        else:
            b = tkinter.Button(window, bg='black', fg='Blue')
            b.configure(command=lambda x1=x, y1=y: ch(x1, y1))

            b.place(x=50 * x, y=50 * y, width=50, height=50)
            c = True
        q.append(b)
    l.append(q)


l[7][7].configure(image=rookimg)
l[7][0].configure(image=rookimg)
l[7][2].configure(image=bishiopimg)
l[7][5].configure(image=bishiopimg)
l[7][1].configure(image=knightimg)
l[7][6].configure(image=knightimg)
l[7][3].configure(image=kingimg)
l[7][4].configure(image=queenimg)
for i in range(8):
    l[1][i].configure(image=bpawnimg)
l[6][3].configure(image=brookimg)

def ch(x, y):
    global  x1, y1
    if 'w' in board[y][x]:
        x1 = x
        y1 = y
        return
    if x1!=-1 and y1!=-1:
        x2 = x
        y2 = y
        if str(l[y1][x1]['image']) == str(queenimg):

            if queen(x1, y1, x2, y2):
                l[y1][x1].configure(image='')
                l[y2][x2].configure(image=queenimg)
        if str(l[y1][x1]['image']) == str(knightimg):


            if knight(x1, y1, x2, y2):
                l[y1][x1].configure(image='')
                l[y2][x2].configure(image=knightimg)
        if str(l[y1][x1]['image']) == str(pawnimg):

            paw = pawngo(x1, y1, x2, y2)

            if type(paw)!=tuple:
                if paw==True:
                    l[y1][x1].configure(image='')
                    l[y2][x2].configure(image=pawnimg)

            elif paw[1]:
                choose = [queenimg, knightimg, bishiopimg, rookimg]
                ch=['wq','wn','wb','wr']
                l[y1][x1].configure(image='')

                l[y2][x2].configure(image=choose[paw[0]])
                board[y2][x2]=ch[paw[0]]
                board[y1][x1]='__'
        if str(l[y1][x1]['image']) == str(bishiopimg):

            if bishop(x1, y1, x2, y2):

                l[y1][x1].configure(image='')
                l[y2][x2].configure(image=bishiopimg)
        if str(l[y1][x1]['image']) == str(rookimg):

            if rook(x1, y1, x2, y2):

                l[y1][x1].configure(image='')
                l[y2][x2].configure(image=rookimg)
        if str(l[y1][x1]['image']) == str(kingimg):

            if king(x1, y1, x2, y2):

                l[y1][x1].configure(image='')
                l[y2][x2].configure(image=kingimg)
        output()
        print(bot(1,1,1,1,True))
    x1=-1
    y1=-1


window.mainloop()
