import customtkinter
from api.notion_api import NotionAPI
class Liste(customtkinter.CTkScrollableFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.grid_columnconfigure(0,weight=1)

        self.actualiser()
    
    def actualiser(self):
        # La on va nettoyer enlever les ancien label 
        # winfo_children() => verifier tout les widget qui sont present 
        for child in self.winfo_children():
            if isinstance(child, customtkinter.CTkLabel):
                # pour detruire  les widget donc les ancien label 
                child.destroy()
            
            # child.destroy()
        
        questions = NotionAPI.voir_question()

        # On créer un label pour chaque question 
        for i , texte in enumerate(questions):
            label = customtkinter.CTkLabel(self, text=f"• {texte}", anchor="w")
            label.grid(row=i, column=0, sticky="w", pady=5, padx=10)

    

    
