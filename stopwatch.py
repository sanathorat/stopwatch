# stopwatch

import tkinter as tk
from datetime import datetime, timedelta

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.running = False
        self.start_time = None
        self.elapsed_time = timedelta(0)

        self.display = tk.Label(root, text="00:00:00.000", font=("Helvetica", 48))
        self.display.pack()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start)
        self.start_button.grid(row=0, column=0, padx=10)

        self.stop_button = tk.Button(self.button_frame, text="Stop", command=self.stop)
        self.stop_button.grid(row=0, column=1, padx=10)

        self.reset_button = tk.Button(self.button_frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=0, column=2, padx=10)

        self.update_display()

    def start(self):
        if not self.running:
            self.start_time = datetime.now() - self.elapsed_time
            self.running = True
            self.update()

    def stop(self):
        if self.running:
            self.elapsed_time = datetime.now() - self.start_time
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = timedelta(0)
        self.update_display()

    def update(self):
        if self.running:
            self.elapsed_time = datetime.now() - self.start_time
            self.update_display()
            self.root.after(10, self.update)

    def update_display(self):
        total_seconds = self.elapsed_time.total_seconds()
        minutes = int(total_seconds // 60)
        seconds = int(total_seconds % 60)
        milliseconds = int((total_seconds % 1) * 1000)
        self.display.config(text=f"{minutes:02}:{seconds:02}:{milliseconds:03}")

if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()