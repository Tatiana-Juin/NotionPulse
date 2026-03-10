import customtkinter
# on met. => pour dire que le fichier est dans le meme dossier 
from  .btn import Btn
from api.notion_api import NotionAPI
from api.config_api import Config

class Form(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master,fg_color="#F9F9F9")
        # Pour saisir du texte 
        self.question = customtkinter.CTkEntry(self,placeholder_text="Test a saisir",width=250);
        self.question.grid(row=2,column=0, padx=5,pady=5)
        # Pour le bouton
        self.btn_question = Btn(self, command=lambda: self.valider_formulaire("question"),text="valider")
        self.btn_question.grid(row=2,column=1,pady=5,padx=5)

        # pour la recherche 
        self.recherche = customtkinter.CTkEntry(self,placeholder_text="recherche a faire",width=250);
        self.recherche.grid(row=2,column=2, padx=5,pady=5)
        # Pour le bouton
        self.btn_recherche = Btn(self,command=lambda: self.valider_formulaire("recherche"),text="rechercher")
        self.btn_recherche.grid(row=2,column=3,pady=5,padx=5)

        self.message_label = customtkinter.CTkLabel(self, text="")
        self.message_label.grid(row=3, column=0, columnspan=4, pady=10)
    
    # fonction pour la validation 
    def valider_formulaire(self,type_donnee):
        # question = self.question.get()
        if type_donnee == "question":
            texte = self.question.get()
            db_id = Config.DB_QUESTIONS
            methode_ajout = NotionAPI.ajout
        else:
            texte=self.recherche.get()
            db_id = Config.DB_RECHERCHES
            methode_ajout = NotionAPI.ajout

        # verification avec id dynamique 
        succes, message = NotionAPI.verification(texte, db_id)
        
        if succes:
            # ajout_question()
            NotionAPI.ajout(texte, db_id)
            self.message_label.configure(text=f"✅ {type_donnee} ajouté", text_color="green")

            if type_donnee =="question":
                self.question.delete(0, "end")
            else:
                self.recherche.delete(0, "end")
        else:
            self.message_label.configure(text=f"❌ {message}", text_color="red")

        
        


