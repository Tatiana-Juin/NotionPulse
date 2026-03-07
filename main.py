import customtkinter;
from views.form import Form
from views.btn import Btn
from views.liste import Liste
class Main(customtkinter.CTk):
    def __init__(self):
    
        super().__init__()
        self.est_afficher = False;
        self.title("Application Notion")
        self.geometry("1200x600")
        self.configure(fg_color="#F9F9F9")

        # La 0 et la 2 vont "pousser" pour que la 1 reste bien au centre
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.titre_page = customtkinter.CTkLabel(self,text="Application pour les lives",font=("Helvetica",24,"bold"))
        self.titre_page.grid(row=0,column=0,columnspan=3,pady=20)

        # Titre du formulaire  
        self.titre = customtkinter.CTkLabel(self, text=" Question récurente",font=("Helvetica",15))
        self.titre.grid(row=1,column=0,pady=3,padx=3)

        # Appelle du formulaire 
        self.saisie_frame = Form(self)
        self.saisie_frame.grid(row=2,column=0, padx=3,pady=3)

        # pour afficher les question
        self.afficher_question = Liste(self)
        self.liste_visible = False;
        # self.afficher_question.grid(row=4,column=0,padx=3,pady=3)

        # Pour voir les 10 premiere question on devra cliquer sur un button 
        self.btn = Btn(self,text="voir les questions",command=self.toggle)
        self.btn.grid(row=3,column=0,padx=3,pady=3)

    def toggle(self):
        self.est_afficher = not self.est_afficher;

        if self.est_afficher == True:
            self.btn.configure(text="masquer les questions")
            self.afficher_question.grid(row=4,column=0,padx=3,pady=3)
            self.afficher_question.actualiser()
        else:
            print("Action : Je cache la liste")
            self.afficher_question.grid_forget()
            # self.btn.configure(text="")
            self.btn.configure(text="voir les questions")


s = Main()
s.mainloop()

