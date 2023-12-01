from flask import Flask, render_template
import tkinter as tk
from tkinter import Label

app = Flask(__name__)

# Fonction pour créer une fenêtre Tkinter
def create_tkinter_window():
    window = tk.Tk()
    window.title("Tkinter Window")

    label = Label(window, text="Contenu Tkinter")
    label.pack(padx=20, pady=20)

    window.mainloop()

# Route pour afficher l'interface utilisateur
@app.route('/')
def home():
    return render_template('index.html')

# Route pour afficher la fenêtre Tkinter
@app.route('/tkinter')
def show_tkinter():
    create_tkinter_window()
    return "Fenêtre Tkinter affichée"

if __name__ == '__main__':
    app.run(debug=True)

