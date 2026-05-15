import re
import tkinter as tk


class CalculatorApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Dark Neon Calculator")
        self.root.geometry("380x560")
        self.root.resizable(False, False)

        self.expression = ""
        self.error_state = False
        self.just_evaluated = False
        self.operators = {"+", "-", "*", "/"}

        self._build_ui()
        self.update_display("0")

    def _build_ui(self) -> None:
        self.canvas = tk.Canvas(self.root, width=380, height=560, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self._draw_gradient_background()

        self.main_frame = tk.Frame(self.root, bg="#14141e", bd=0, highlightthickness=0)
        self.canvas.create_window(190, 280, window=self.main_frame, width=340, height=500)

        self.display_var = tk.StringVar(value="0")
        self.display_label = tk.Label(
            self.main_frame,
            textvariable=self.display_var,
            font=("Consolas", 34, "bold"),
            fg="#e8f3ff",
            bg="#0e0e16",
            anchor="e",
            padx=18,
            pady=18,
            relief="flat",
            bd=0,
        )
        self.display_label.pack(fill="x", pady=(0, 16))

        self.button_frame = tk.Frame(self.main_frame, bg="#14141e")
        self.button_frame.pack(fill="both", expand=True)

        for col in range(4):
            self.button_frame.grid_columnconfigure(col, weight=1)
        for row in range(5):
            self.button_frame.grid_rowconfigure(row, weight=1)

        buttons = [
            ["C", "", "", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", ""],
        ]

        for r_idx, row in enumerate(buttons):
            for c_idx, token in enumerate(row):
                if token == "":
                    spacer = tk.Label(self.button_frame, text="", bg="#14141e")
                    spacer.grid(row=r_idx, column=c_idx, padx=6, pady=6, sticky="nsew")
                    continue

                btn = self._create_button(token)
                btn.grid(row=r_idx, column=c_idx, padx=6, pady=6, sticky="nsew")

    def _draw_gradient_background(self) -> None:
        top = (7, 8, 18)
        bottom = (21, 29, 52)
        height = 560

        for y in range(height):
            t = y / height
            r = int(top[0] * (1 - t) + bottom[0] * t)
            g = int(top[1] * (1 - t) + bottom[1] * t)
            b = int(top[2] * (1 - t) + bottom[2] * t)
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.canvas.create_line(0, y, 380, y, fill=color)

    def _create_button(self, token: str) -> tk.Button:
        if token in self.operators or token == "=":
            base_bg = "#102946"
            hover_bg = "#163e66"
            fg_color = "#7ed1ff"
        elif token == "C":
            base_bg = "#3a1120"
            hover_bg = "#52172d"
            fg_color = "#ff7aa2"
        else:
            base_bg = "#1a1a28"
            hover_bg = "#24243a"
            fg_color = "#e6e9ff"

        btn = tk.Button(
            self.button_frame,
            text=token,
            font=("Consolas", 18, "bold"),
            bg=base_bg,
            fg=fg_color,
            activebackground=hover_bg,
            activeforeground=fg_color,
            relief="flat",
            bd=0,
            highlightthickness=1,
            highlightbackground="#26334f",
            cursor="hand2",
            command=lambda t=token: self.on_button_click(t),
        )
        btn.bind("<Enter>", lambda _e, b=btn, c=hover_bg: b.configure(bg=c))
        btn.bind("<Leave>", lambda _e, b=btn, c=base_bg: b.configure(bg=c))
        return btn

    def on_button_click(self, token: str) -> None:
        if token == "C":
            self.clear()
            return

        if token == "=":
            self.evaluate_expression()
            return

        if self.error_state:
            if token.isdigit() or token == ".":
                self.expression = ""
                self.error_state = False
            else:
                return

        if token in self.operators:
            if not self.expression:
                if token == "-":
                    self.expression = "-"
                else:
                    return
            elif self.expression[-1] in self.operators:
                self.expression = self.expression[:-1] + token
            else:
                self.expression += token

            self.just_evaluated = False
            self.update_display(self.expression or "0")
            return

        if token == ".":
            if self.just_evaluated:
                self.expression = ""
                self.just_evaluated = False

            current_number = re.split(r"[+\-*/]", self.expression)[-1]
            if "." in current_number:
                return
            if not self.expression or self.expression[-1] in self.operators:
                self.expression += "0"
            self.expression += "."
            self.update_display(self.expression)
            return

        if token.isdigit():
            if self.just_evaluated:
                self.expression = ""
                self.just_evaluated = False

            self.expression += token
            self.update_display(self.expression)

    def clear(self) -> None:
        self.expression = ""
        self.error_state = False
        self.just_evaluated = False
        self.update_display("0")

    def evaluate_expression(self) -> None:
        if not self.expression:
            return
        if self.expression[-1] in self.operators:
            self._show_error()
            return

        if not re.fullmatch(r"[0-9+\-*/. ]+", self.expression):
            self._show_error()
            return

        try:
            result = eval(self.expression, {"__builtins__": None}, {})
        except ZeroDivisionError:
            self._show_error()
            return
        except Exception:
            self._show_error()
            return

        if isinstance(result, float) and result.is_integer():
            result_text = str(int(result))
        else:
            result_text = str(result)

        self.expression = result_text
        self.error_state = False
        self.just_evaluated = True
        self.update_display(result_text)

    def update_display(self, value: str) -> None:
        text = value if value else "0"
        self.display_var.set(text)

    def _show_error(self) -> None:
        self.expression = ""
        self.error_state = True
        self.just_evaluated = False
        self.update_display("Error")


def main() -> None:
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()