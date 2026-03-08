import customtkinter
from .btn import Btn
from api.notion_api import NotionAPI
class Liste(customtkinter.CTkScrollableFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,width=400,**kwargs)
        
        # marque page pour notion pour la pagination
        self.curseur_actuel = None
        # pour savoir si on affiche le bouton suivant 
        self.a_une_suite = False;
        
        self.grid_columnconfigure(0,weight=1)
        self.btn_suivant = Btn(self,text="chatger plus", command = self.charger_questions)
        # self.actualiser()
    
    def actualiser(self):
        # La on va nettoyer enlever les ancien label 
        # winfo_children() => verifier tout les widget qui sont present

       
        self.curseur_actuel = None 
        
        # On cache le bouton pour qu'il ne reste pas bloqué sur une vieille ligne
        self.btn_suivant.grid_forget()
        
        for child in self.winfo_children():
            if isinstance(child, customtkinter.CTkLabel):
                child.destroy()
            
        # Maintenant on charge les données toutes fraîches
        self.charger_questions()
        
        # questions = NotionAPI.voir_question()

        # On créer un label pour chaque question 
        # for i , texte in enumerate(questions):
        #     label = customtkinter.CTkLabel(self, text=f"• {texte}", anchor="w")
        #     label.grid(row=i, column=0, sticky="w", pady=5, padx=10)

    
    def charger_questions(self):
        resultat = NotionAPI.voir_question(self.curseur_actuel)
        
        questions = resultat["questions"]
        self.curseur_actuel = resultat['next_cursor']
        self.a_une_suite = resultat["has_more"]
        
        

        # calcule de la ligne de depart pour les nouveaux labels 
        # compte tout sauf le bouton 
        nb_widgets_actuels = len(
            [c for c in self.winfo_children()
            if c.winfo_viewable() and c != self.btn_suivant
            ]
        )

        # Ajout de nouveaux label 
        for i, texte in enumerate(questions):
            lbl = customtkinter.CTkLabel(self,text=texte)
            lbl.grid(row=nb_widgets_actuels + i, column=0, pady=5, padx=10)
        
        #gestion du bouton suivant 
        if self.a_une_suite:
            nouvelle_ligne_btn = nb_widgets_actuels + len(questions)
            self.btn_suivant.grid(row=nouvelle_ligne_btn,column=0,pady=10)
        else:
            self.btn_suivant.grid_forget()

    
