import tkinter as tk
import random

fenetre = tk.Tk()
fenetre.title("cacamou")
fenetre.geometry("1280x720")

def aficher_page2():
    frame_page1.pack_forget()
    frame_page2.pack(fill="both", expand=True)

def aficher_page3():
    frame_page1.pack_forget()
    frame_page3.pack(fill="both", expand=True)


frame_page1=tk.Frame(fenetre)
frame_page1.pack(fill="both", expand=True)
tk.Label(frame_page1, text=("Bienvenue a l'interrogatoire."),font=("Arial", 20)).pack(pady=20)
tk.Label(frame_page1, text=("T'aime le caca mou ?"),font=("Arial", 20)).pack(pady=5)
tk.Button(frame_page1, text="oui", command=aficher_page2).pack(pady=10)
tk.Button(frame_page1, text="non, command=aficher_page3).pack(pady=10)



frame_page2=tk.Frame(fenetre)
tk.Label(frame_page2, text=("t'ai un bon."),font=("Arial", 20)).pack(pady=20)




frame_page3=tk.Frame(fenetre)
tk.Label(frame_page3, text=("Sal yaman va."),font=("Arial", 20)).pack(pady=20)





fenetre.mainloop()
                    
