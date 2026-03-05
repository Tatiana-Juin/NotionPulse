import customtkinter;
from views.form import Form
from views.btn import Btn
from views.liste import Liste
class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()
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
        self.afficher_question.grid(row=4,column=0,padx=3,pady=3)

        # Pour voir les 10 premiere question on devra cliquer sur un button 
        self.btn = Btn(self,text="Voir les idées de publication",command=self.afficher_question.actualiser)
        self.btn.grid(row=3,column=0,padx=3,pady=3)

        

main = Main()
main.mainloop()

