import os
import textwrap
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

from PIL import Image, ImageDraw, ImageFont

FONT_PATH = os.path.join(os.path.dirname(__file__), "sketchy_notes", "Sketchy Notes.otf")
FONT_SIZE = 32
PAGE_WIDTH = 800
PAGE_HEIGHT = 1000
MARGIN = 50
LINE_SPACING = 10


def render_handwriting(text: str, output_path: str) -> None:
    text = text.strip()
    if not text:
        raise ValueError("Please enter some text before saving.")

    background = Image.new("RGB", (PAGE_WIDTH, PAGE_HEIGHT), (255, 255, 255))
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    offset = MARGIN
    for line in textwrap.wrap(text, width=40):
        draw.text((MARGIN, offset), line, font=font, fill=(0, 0, 0))
        offset += FONT_SIZE + LINE_SPACING

    background.save(output_path)


class HandwritingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Handwriting Notes")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Enter your note:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        self.note_text = scrolledtext.ScrolledText(self, width=60, height=15, wrap=tk.WORD, font=("Arial", 11))
        self.note_text.grid(row=1, column=0, padx=10, pady=10)

        button_frame = tk.Frame(self)
        button_frame.grid(row=2, column=0, pady=(0, 10), sticky="e")

        self.save_button = tk.Button(button_frame, text="Save as Image", command=self.on_save)
        self.save_button.pack(side=tk.RIGHT, padx=5)

        self.status_label = tk.Label(self, text="", fg="green")
        self.status_label.grid(row=3, column=0, padx=10, sticky="w")

    def on_save(self):
        output_path = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[("JPEG Image", "*.jpg"), ("PNG Image", "*.png")],
            title="Save handwritten note as...",
            initialfile="output.jpg",
        )
        if not output_path:
            return

        text = self.note_text.get("1.0", tk.END)
        try:
            render_handwriting(text, output_path)
            self.status_label.config(text=f"Saved to {output_path}", fg="green")
            messagebox.showinfo("Success", f"Image saved to:\n{output_path}")
        except Exception as exc:
            self.status_label.config(text="Failed to save image.", fg="red")
            messagebox.showerror("Error", str(exc))


if __name__ == "__main__":
    app = HandwritingApp()
    app.mainloop()
