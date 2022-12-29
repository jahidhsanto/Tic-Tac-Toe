import tkinter as tk


def gameBoard(boardSize, userSymbol='X'):
    if userSymbol == 1:
        userSymbol = "X"
    else:
        userSymbol = "0"
    print(userSymbol)
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Tic Tac Toe")

    tk.Label(root, text="Tic Tac Toe", font=('Ariel', 25)).pack()

    play_area = tk.Frame(root, width=300, height=300, bg='white')
    XO_points = []

    class XOPoint:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.value = None
            self.button = tk.Button(play_area, text="", width=10, height=5)
            self.button.grid(row=x, column=y)

        def reset(self):
            self.button.configure(text="", bg='white')
            self.value = None

    for x in range(0, boardSize):
        for y in range(0, boardSize):
            XOPoint(x, y)
    play_area.pack(pady=10, padx=10)

    root.mainloop()


if __name__ == '__main__':
    gameBoard()