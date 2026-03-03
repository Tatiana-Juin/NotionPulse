import customtkinter
# on met. => pour dire que le fichier est dans le meme dossier 
from  .btn_form import BtnForm
from api.notion_api import NotionAPI

class Form(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master,fg_color="#F9F9F9")
        # Pour saisir du texte 
        self.question = customtkinter.CTkEntry(self,placeholder_text="Test a saisir");
        self.question.grid(row=2,column=1, padx=3,pady=3)
        # Pour le bouton
        self.btn_frame = BtnForm(self,command=self.valider_formulaire)
        self.btn_frame.grid(row=2,column=2,pady=3,padx=3)

        self.message_label = customtkinter.CTkLabel(self, text="")
        self.message_label.grid(row=3, column=1, columnspan=2, pady=10)

    def valider_formulaire(self):
        question = self.question.get()

        # APPELLE DE NOTRE CLASSE API 
        succes, message = NotionAPI.verification(question)

        # MISE A JOURS DE L'INTERFACE 
        self.message_label.configure(text=message)
        if succes:
            self.message_label.configure(text_color="green")
            NotionAPI.ajout_question(question)
            
            # Efface le texte de l'index 0 à la fin
            self.question.delete(0, "end")
        else:
            self.message_label.configure(text_color="red")
        


