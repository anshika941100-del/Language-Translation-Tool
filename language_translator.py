from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Chinese": "zh-CN"
}

def translate():
    try:
        text = input_box.get("1.0", END).strip()

        if text == "":
            messagebox.showwarning("Warning", "Please enter some text")
            return

        source = languages[source_lang.get()]
        target = languages[target_lang.get()]

        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        output_box.delete("1.0", END)
        output_box.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))

root = Tk()
root.title("Language Translation Tool")
root.geometry("700x500")

title = Label(
    root,
    text="Language Translation Tool",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

Label(root, text="Enter Text").pack()

input_box = Text(root, height=8, width=70)
input_box.pack(pady=5)

frame = Frame(root)
frame.pack(pady=10)

source_lang = ttk.Combobox(
    frame,
    values=list(languages.keys()),
    state="readonly"
)
source_lang.set("English")
source_lang.grid(row=0, column=0, padx=20)

target_lang = ttk.Combobox(
    frame,
    values=list(languages.keys()),
    state="readonly"
)
target_lang.set("Hindi")
target_lang.grid(row=0, column=1, padx=20)

translate_button = Button(
    root,
    text="Translate",
    command=translate
)
translate_button.pack(pady=10)

Label(root, text="Translated Text").pack()

output_box = Text(root, height=8, width=70)
output_box.pack(pady=5)

root.mainloop()