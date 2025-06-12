import tkinter as tk

def click(event):
    current = entry.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

app = tk.Tk()
app.title("Simple Calculator")
app.geometry("300x400")

entry = tk.Entry(app, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
]

for row in buttons:
    frame = tk.Frame(app)
    frame.pack()
    for text in row:
        btn = tk.Button(frame, text=text, font="Arial 18", width=5, height=2)
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", click)

app.mainloop()
