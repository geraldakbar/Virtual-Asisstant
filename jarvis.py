import tkinter as tk
import  wolframalpha
import wikipedia

def set_indo():
    wikipedia.set_lang("id")
def set_english():
    wikipedia.set_lang("en")
root= tk.Tk()
root.winfo_toplevel().title('JARVIS')

introduction = tk.Label(master = root, text = 'Halo namaku jarvis, ada yang bisa kubantu?')
introduction.grid(row = 0 )

canvas = tk.Canvas(root, width = 500, height = 500)
canvas.grid(row = 2, column = 0)

canvas2 = tk.Canvas(root,width = 500, height = 20)
canvas2.grid(row = 3)

frame = tk.Text(canvas, bg = 'white')
frame.pack(side = tk.LEFT)

Question = tk.Entry(master=root, width = 106)
Question.grid(row = 1,column = 0)

def dark_mode():
    frame.configure(bg = 'black', fg = 'white')
    Question.configure(bg = 'black', fg = 'white')

def light_mode():
    frame.configure(bg = 'white', fg ='black')
    Question.configure(bg = 'White', fg = 'black')

dark_button = tk.Button(master = canvas2, command = dark_mode, text = 'Night mode')
dark_button.pack(side = tk. RIGHT)
light_button = tk.Button(master= canvas2, command = light_mode, text = 'Light Mode')
light_button.pack(side = tk.RIGHT)

indo_button = tk.Button(master = canvas2, text = 'ID', command = set_indo)
english_button = tk.Button(master = canvas2,text = 'ENG', command = set_english)

indo_button.pack(side = tk.LEFT)
english_button.pack(side = tk.LEFT)

scroll = tk.Scrollbar(master = canvas)
scroll.pack(side = tk.RIGHT, fill = tk.Y)
scroll.configure(command = frame.yview)
frame.config(yscrollcommand = scroll.set)

def jawaban(event):
    frame.delete(1.0, tk.END)
    pertanyaan = Question.get()
    try:
        app_id = 'UUXP2T-T4H59E584W'
        client = wolframalpha.Client(app_id)
        res = client.query(pertanyaan)
        jawaban = next(res.results).text
        frame.insert(tk.END, jawaban)
    except:
        tes = wikipedia.summary(pertanyaan)
        frame.insert(tk.END, tes)

root.bind('<Return>', jawaban)

root.mainloop()
