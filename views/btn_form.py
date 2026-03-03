import customtkinter

class BtnForm(customtkinter.CTkButton):
    # **kwargs => la on a mis le texte valider pmais peut etre plus tard on devra changer des paramettre comme ca couleur et son texte et grâce a **kwargs on peut le faire directement a la main ca avoir besoin d'aller changer a la main les couleur en claire en allant dans le constructeur 
    def __init__(self,master,**kwargs):
        super().__init__(master, text="Valider", **kwargs)

       
