import tkinter as tk


class TicTacToeApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Neon Tic Tac Toe")
        self.root.geometry("460x620")
        self.root.resizable(False, False)

        self.current_player = "X"
        self.board = ["" for _ in range(9)]
        self.buttons = []
        self.game_over = False

        self.winning_lines = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]

        self._build_ui()

    def _build_ui(self) -> None:
        self.canvas = tk.Canvas(self.root, width=460, height=620, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self._draw_gradient_background()

        self.container = tk.Frame(self.root, bg="#121827")
        self.canvas.create_window(230, 310, window=self.container, width=400, height=560)

        title = tk.Label(
            self.container,
            text="TIC TAC TOE",
            font=("Consolas", 28, "bold"),
            fg="#d7f5ff",
            bg="#121827",
        )
        title.pack(pady=(12, 8))

        self.status_var = tk.StringVar(value="Player X Turn")
        status = tk.Label(
            self.container,
            textvariable=self.status_var,
            font=("Consolas", 14, "bold"),
            fg="#8de6ff",
            bg="#121827",
        )
        status.pack(pady=(0, 14))

        board_frame = tk.Frame(self.container, bg="#121827")
        board_frame.pack(pady=(6, 18))

        for r in range(3):
            board_frame.grid_rowconfigure(r, weight=1)
            board_frame.grid_columnconfigure(r, weight=1)

        for i in range(9):
            btn = tk.Button(
                board_frame,
                text="",
                font=("Consolas", 36, "bold"),
                width=4,
                height=2,
                bg="#1a2340",
                fg="#e6f7ff",
                activebackground="#22305a",
                activeforeground="#e6f7ff",
                relief="flat",
                bd=0,
                highlightthickness=2,
                highlightbackground="#2f467a",
                cursor="hand2",
                command=lambda idx=i: self.make_move(idx),
            )
            btn.grid(row=i // 3, column=i % 3, padx=6, pady=6)
            btn.bind("<Enter>", lambda _e, b=btn: b.configure(bg="#22305a"))
            btn.bind("<Leave>", lambda _e, b=btn: self._restore_button_bg(b))
            self.buttons.append(btn)

        self.reset_button = tk.Button(
            self.container,
            text="New Round",
            font=("Consolas", 13, "bold"),
            bg="#10243d",
            fg="#8dd8ff",
            activebackground="#18395f",
            activeforeground="#8dd8ff",
            relief="flat",
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.reset_game,
        )
        self.reset_button.pack()

    def _draw_gradient_background(self) -> None:
        top = (8, 10, 22)
        bottom = (18, 39, 70)
        height = 620

        for y in range(height):
            t = y / height
            r = int(top[0] * (1 - t) + bottom[0] * t)
            g = int(top[1] * (1 - t) + bottom[1] * t)
            b = int(top[2] * (1 - t) + bottom[2] * t)
            self.canvas.create_line(0, y, 460, y, fill=f"#{r:02x}{g:02x}{b:02x}")

    def _restore_button_bg(self, button: tk.Button) -> None:
        if button.cget("text") == "":
            button.configure(bg="#1a2340")

    def make_move(self, index: int) -> None:
        if self.game_over or self.board[index] != "":
            return

        self.board[index] = self.current_player
        self.buttons[index].configure(
            text=self.current_player,
            fg="#7dffb0" if self.current_player == "X" else "#ffb3de",
            bg="#26335f",
        )

        winner, line = self.check_winner()
        if winner:
            self.game_over = True
            self.status_var.set(f"Player {winner} Wins")
            self._highlight_winning_line(line)
            return

        if "" not in self.board:
            self.game_over = True
            self.status_var.set("Draw")
            return

        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_var.set(f"Player {self.current_player} Turn")

    def check_winner(self):
        for a, b, c in self.winning_lines:
            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a], (a, b, c)
        return None, None

    def _highlight_winning_line(self, line) -> None:
        for idx in line:
            self.buttons[idx].configure(bg="#1f6b57", highlightbackground="#51f2c3")

    def reset_game(self) -> None:
        self.current_player = "X"
        self.board = ["" for _ in range(9)]
        self.game_over = False
        self.status_var.set("Player X Turn")

        for btn in self.buttons:
            btn.configure(
                text="",
                bg="#1a2340",
                fg="#e6f7ff",
                highlightbackground="#2f467a",
            )


def main() -> None:
    root = tk.Tk()
    TicTacToeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()