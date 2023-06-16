import tkinter as tk
from main import queen, knight, pawngo, bishop, rook, output, board
from change import show


def ch(x, y):
    global click, x1, y1
    print(click)
    if click:
        x1 = x
        y1 = y
        click = not click
        return
    x2 = x
    y2 = y
    click = not click
    print(l[y1][x1]['image'], queenimg)

    if str(l[y1][x1]['image']) == str(pawnimg):
        print(y1, x1, y2, x2)
        if pawngo(x1, y1, x2, y2):
            print('Test')
            l[y1][x1].configure(image='')
            l[y2][x2].configure(image=pawnimg)
            if y2 == 0 or y2 == 7:  # Check if pawn reached the end of the board
                open_promotion_window(x2, y2)
                board[y2][x2] = 'wq'  # Assign the promoted piece to the board

    # Rest of your code


window = tk.Tk()
window.geometry('400x400')
queenimg = tk.PhotoImage(file='figures/wq.png').subsample(3)
pawnimg = tk.PhotoImage(file='figures/wp.png').subsample(3)
knightimg = tk.PhotoImage(file='figures/wn.png').subsample(3)
bishiopimg = tk.PhotoImage(file='figures/wb.png').subsample(3)
rookimg = tk.PhotoImage(file='figures/wr.png').subsample(3)
kingimg = tk.PhotoImage(file='figures/wk.png').subsample(3)
bqueenimg = tk.PhotoImage(file='figures/bq.png').subsample(3)
bpawnimg = tk.PhotoImage(file='figures/bp.png').subsample(3)
bknightimg = tk.PhotoImage(file='figures/bk.png').subsample(3)
brook = tk.PhotoImage(file='figures/br.png').subsample(3)
bbishop = tk.PhotoImage(file='figures/bb.png').subsample(3)
bking = tk.PhotoImage(file='figures/bk.png').subsample(3)
c = False
click = True
l = []
x1 = 0
y1 = 0

def open_promotion_window(x, y):
    promotion_window = tk.Toplevel(window)
    promotion_window.title("Promotion Window")

    def promote_pawn(selected_piece):
        if selected_piece == "Queen":
            l[y][x].configure(image=queenimg)
        elif selected_piece == "Knight":
            l[y][x].configure(image=knightimg)
        elif selected_piece == "Bishop":
            l[y][x].configure(image=bishiopimg)
        elif selected_piece == "Rook":
            l[y][x].configure(image=rookimg)

        promotion_window.destroy()

    pieces = ["Queen", "Knight", "Bishop", "Rook"]
    selected_piece = tk.StringVar()

    label = tk.Label(promotion_window, text="Choose a piece:")
    label.pack()

    dropdown = tk.OptionMenu(promotion_window, selected_piece, *pieces)
    dropdown.pack()

    button = tk.Button(promotion_window, text="Promote", command=lambda: promote_pawn(selected_piece.get()))
    button.pack()

def ch(x, y):
    global click, x1, y1
    print(click)
    if click:
        x1 = x
        y1 = y
        click = not click
        return
    x2 = x
    y2 = y
    click = not click
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
        if pawngo(x1, y1, x2, y2):
            print('Test')
            l[y1][x1].configure(image='')
            l[y2][x2].configure(image=pawnimg)
            if y2 == 0:
                open_promotion_window(x2, y2)
                board[y2][x2] = 'wq'
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

print(show())
window.mainloop()