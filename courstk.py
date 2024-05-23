import tkinter as tk

app = tk.Tk()
titre = tk.Label(
    app, text=("Bienvenue"), font=("time new roman", 40), bg="red"
    )

titre.pack()
saisi = tk.Entry(app)
saisi.pack()


def somme():
    print("Fatima djouguel fiiiiiiiiiii")

btn = tk.Button(app, text="Envoyer", command=somme)
btn.pack()
app.mainloop()