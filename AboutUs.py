from tkinter import *


window = Tk()
window.title("Theory Of Graphs Application")
window.geometry("1080x720")
window.resizable(width=False, height=False)
bg = PhotoImage(file="yess.png")
my_label=Label(window, image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)
window.iconbitmap("app.ico")
#window.config(background="#5d8a82")

#--------------------------------FUNCTIONS----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    window.destroy()
    import main



#----------------------------------MENU-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#1) -creer la barre des menu

menuBar = Menu(window)

# 2) -creer les menus principaux

buttonHome= Button(menuBar)
buttonAbtus= Button(menuBar)

# 3) -ajouter les menus principaux a la barre des menus
menuBar.add_cascade(label ="Home",menu=buttonHome,command=main)
menuBar.add_cascade(label ="About us",menu=buttonAbtus)

window.config(menu=menuBar)

#--------------------------------LABELS----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
label_title = Label(window, text="About Us", font=("Kefa 25", 30), fg='black')
label_title.pack(pady=20)
label_subtitle = Label(window, text="""
                       
=>Theory Of Graphs Application vous permet de créer des graphes, afficher leurs caractéristriques et vous permet également d'utiliser 
les divers algorithms de la theorie de graphes:
                       
                       
1-En cliquant sur le bouton 'Create Your graph' une menu d informations à remplir à propos de votre graphe vous sera affichée.
                       

2-Ensuite vous allez entrez les arcs de votre graphes avec leurs capacités si vous avez selectionné ce choix dans le menu 
précédent
                       

3-Aprés la validation, vous serez capable d afficher votre graphe ainsi que ses caractéristiques et vous pouvez lui appliquer
 les divers algorithms. 
                       
                     """, font=("Courrier",12), fg='black')
label_subtitle.pack()

#---------------------------------------------------------DATAFRAME--------------------------------------------------------------------------------------

window.mainloop()

