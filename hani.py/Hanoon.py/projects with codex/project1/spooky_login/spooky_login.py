import random
import tkinter as tk
from tkinter import messagebox


class SpookyLoginApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Spooky Login")
        self.root.geometry("900x600")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=900, height=600, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self._draw_gradient_background()
        self.particles = self._create_particles(85)
        self.ghosts = self._create_ghosts()
        self._draw_moon()

        self.login_card = tk.Frame(self.root, bg="#140b22", bd=0, highlightthickness=2, highlightbackground="#7f5af0")
        self.login_window = self.canvas.create_window(450, 315, window=self.login_card)

        title = tk.Label(
            self.login_card,
            text="SPOOKY LOGIN",
            font=("Consolas", 24, "bold"),
            fg="#f7f2ff",
            bg="#140b22",
        )
        title.pack(pady=(24, 16))

        user_label = tk.Label(self.login_card, text="Username", font=("Consolas", 11), fg="#cab8ff", bg="#140b22")
        user_label.pack(anchor="w", padx=34)
        self.username_entry = tk.Entry(
            self.login_card,
            width=30,
            font=("Consolas", 12),
            fg="#f5ecff",
            bg="#23143a",
            insertbackground="#f5ecff",
            relief="flat",
        )
        self.username_entry.pack(padx=34, pady=(4, 14), ipady=8)

        pass_label = tk.Label(self.login_card, text="Password", font=("Consolas", 11), fg="#cab8ff", bg="#140b22")
        pass_label.pack(anchor="w", padx=34)
        self.password_entry = tk.Entry(
            self.login_card,
            width=30,
            show="*",
            font=("Consolas", 12),
            fg="#f5ecff",
            bg="#23143a",
            insertbackground="#f5ecff",
            relief="flat",
        )
        self.password_entry.pack(padx=34, pady=(4, 20), ipady=8)

        self.login_button = tk.Button(
            self.login_card,
            text="Enter If You Dare",
            command=self._attempt_login,
            width=26,
            font=("Consolas", 11, "bold"),
            bg="#ff4d6d",
            fg="#fff8f8",
            activebackground="#ff7590",
            activeforeground="#fff8f8",
            relief="flat",
            cursor="hand2",
        )
        self.login_button.pack(pady=(0, 24), ipady=8)

        self.hint = tk.Label(
            self.login_card,
            text="Hint: user = ghost, pass = pumpkin",
            font=("Consolas", 9),
            fg="#9d8ad8",
            bg="#140b22",
        )
        self.hint.pack(pady=(0, 20))

        self.username_entry.bind("<Return>", lambda _: self._attempt_login())
        self.password_entry.bind("<Return>", lambda _: self._attempt_login())

        self._animate_scene()

    def _draw_gradient_background(self) -> None:
        top = (8, 5, 16)
        bottom = (37, 18, 56)
        for y in range(600):
            t = y / 600
            r = int(top[0] * (1 - t) + bottom[0] * t)
            g = int(top[1] * (1 - t) + bottom[1] * t)
            b = int(top[2] * (1 - t) + bottom[2] * t)
            self.canvas.create_line(0, y, 900, y, fill=f"#{r:02x}{g:02x}{b:02x}")

    def _draw_moon(self) -> None:
        self.canvas.create_oval(90, 70, 230, 210, fill="#f4ecb2", outline="")
        self.canvas.create_oval(125, 55, 240, 180, fill="#150a26", outline="")

    def _create_particles(self, count: int):
        particles = []
        for _ in range(count):
            x = random.randint(0, 900)
            y = random.randint(0, 600)
            size = random.randint(1, 3)
            speed = random.uniform(0.4, 1.2)
            item = self.canvas.create_oval(x, y, x + size, y + size, fill="#d7cfff", outline="")
            particles.append({"item": item, "speed": speed, "size": size})
        return particles

    def _create_ghosts(self):
        ghosts = []
        positions = [(140, 440, 0.9), (760, 470, 1.2), (740, 170, 0.75)]
        for x, y, speed in positions:
            body = self.canvas.create_oval(x - 35, y - 48, x + 35, y + 40, fill="#ddd4ff", outline="")
            wave1 = self.canvas.create_arc(x - 36, y + 18, x - 6, y + 58, start=0, extent=180, style="chord", fill="#ddd4ff", outline="")
            wave2 = self.canvas.create_arc(x - 10, y + 16, x + 20, y + 56, start=0, extent=180, style="chord", fill="#ddd4ff", outline="")
            wave3 = self.canvas.create_arc(x + 14, y + 18, x + 44, y + 58, start=0, extent=180, style="chord", fill="#ddd4ff", outline="")
            eye_l = self.canvas.create_oval(x - 16, y - 18, x - 6, y - 8, fill="#1d1032", outline="")
            eye_r = self.canvas.create_oval(x + 6, y - 18, x + 16, y - 8, fill="#1d1032", outline="")
            ghosts.append(
                {
                    "parts": [body, wave1, wave2, wave3, eye_l, eye_r],
                    "x": x,
                    "y": y,
                    "base_y": y,
                    "dx": speed,
                    "phase": random.uniform(0, 6.28),
                }
            )
        return ghosts

    def _animate_scene(self) -> None:
        for p in self.particles:
            self.canvas.move(p["item"], 0, p["speed"])
            x1, y1, x2, y2 = self.canvas.coords(p["item"])
            if y1 > 605:
                new_x = random.randint(0, 900)
                self.canvas.coords(p["item"], new_x, -5, new_x + p["size"], -5 + p["size"])

        for g in self.ghosts:
            g["phase"] += 0.06
            target_y = g["base_y"] + 8 * __import__("math").sin(g["phase"])
            dy = target_y - g["y"]
            g["y"] = target_y

            next_x = g["x"] + g["dx"]
            if next_x < 70 or next_x > 830:
                g["dx"] *= -1
            g["x"] += g["dx"]

            for part in g["parts"]:
                self.canvas.move(part, g["dx"], dy)

        self.root.after(30, self._animate_scene)

    def _attempt_login(self) -> None:
        user = self.username_entry.get().strip().lower()
        password = self.password_entry.get().strip().lower()

        if user == "ghost" and password == "pumpkin":
            messagebox.showinfo("Welcome", "Access granted. Happy haunting!")
            return

        self._shake_card()
        messagebox.showerror("Denied", "Wrong credentials. The ghosts are watching.")

    def _shake_card(self) -> None:
        x, y = self.canvas.coords(self.login_window)
        offsets = [-10, 10, -8, 8, -5, 5, -2, 2, 0]

        def step(i: int = 0) -> None:
            if i >= len(offsets):
                return
            self.canvas.coords(self.login_window, x + offsets[i], y)
            self.root.after(35, lambda: step(i + 1))

        step()


def main() -> None:
    root = tk.Tk()
    SpookyLoginApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
