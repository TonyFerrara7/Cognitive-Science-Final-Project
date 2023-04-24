import tkinter as tk
from tkinter import messagebox
from random import randint
import webbrowser


class NumberMemoryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Memory Test")
        self.level = 1
        self.attempts = []

        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(pady=20)

        self.start_button = tk.Button(self.main_frame, text="Start Test", command=self.start_test)
        self.start_button.pack()

    def start_test(self):
        self.start_button.config(state=tk.DISABLED)
        self.show_number()

    def show_number(self):
        self.number = ''.join(str(randint(0, 9)) for _ in range(self.level))
        self.number_label = tk.Label(self.main_frame, text=self.number, font=("Helvetica", 20))
        self.number_label.pack(pady=20)
        self.master.after(1000 * self.level, self.hide_number)

    def hide_number(self):
        self.number_label.pack_forget()
        self.enter_number()

    def enter_number(self):
        self.entry_var = tk.StringVar()
        self.number_entry = tk.Entry(self.main_frame, textvariable=self.entry_var, font=("Helvetica", 20))
        self.number_entry.pack(pady=20)
        self.submit_button = tk.Button(self.main_frame, text="Submit", command=self.check_answer)
        self.submit_button.pack()

    def check_answer(self):
        answer = self.entry_var.get()
        if answer == self.number:
            self.attempts.append(1)
            self.level += 1
            self.number_entry.pack_forget()
            self.submit_button.pack_forget()
            self.show_number()
        else:
            self.attempts.append(0)
            messagebox.showinfo("Game Over", f"Your highest level was: {self.level}")
            self.master.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = NumberMemoryApp(root)
    root.protocol("WM_DELETE_WINDOW", root.quit)
    root.mainloop()

    url = "https://cdn.discordapp.com/attachments/1043007664302587995/1092509378273345636/s8ojLBjIZTAAAAAElFTkSuQmCC.png"
    webbrowser.open(url)
