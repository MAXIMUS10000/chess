import tkinter
from main import queen, knight, pawngo, bishop, rook, output, board
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
brook = tkinter.PhotoImage(file='figures/br.png').subsample(3)
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

for i in range(8):
    l[6][i].configure(image=pawnimg)

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


def ch(x, y):
    global  x1, y1
    print(board[x][y],x,y)
    if 'w' in board[y][x]:
        print('white figure')
        x1 = x
        y1 = y
        return
    if x1!=-1 and y1!=-1:
        x2 = x
        y2 = y
        print(l[y1][x1]['image'], queenimg)
        if str(l[y1][x1]['image']) == str(queenimg):
            print(y1, x1, y2, x2)
            if queen(x1, y1, x2, y2):
                l[y1][x1].configure(image='')
                l[y2][x2].configure(image=queenimg)
        if str(l[y1][x1]['image']) == str(knightimg):
            print(y1, x1, y2, x2)

            if knight(x1, y1, x2, y2):
                l[y1][x1].configure(image='')
                l[y2][x2].configure(image=knightimg)
        if str(l[y1][x1]['image']) == str(pawnimg):
            print(y1, x1, y2, x2)
            paw = pawngo(x1, y1, x2, y2)

            if type(paw)!=tuple and paw==True:
                l[y1][x1].configure(image='')
                l[y2][x2].configure(image=pawnimg)

            elif paw[1]:
                choose = [queenimg, knightimg, bishiopimg, rookimg]
                l[y1][x1].configure(image='')
                l[y2][x2].configure(image=choose[paw[0]])

        if str(l[y1][x1]['image']) == str(bishiopimg):
            print(y1, x1, y2, x2)
            if bishop(x1, y1, x2, y2):
                print('Test')
                l[y1][x1].configure(image='')
                l[y2][x2].configure(image=bishiopimg)
        if str(l[y1][x1]['image']) == str(rookimg):
            print(y1, x1, y2, x2)
            if rook(x1, y1, x2, y2):
                print('Test')
                l[y1][x1].configure(image='')
                l[y2][x2].configure(image=rookimg)
        output()
    x1=-1
    y1=-1


window.mainloop()
