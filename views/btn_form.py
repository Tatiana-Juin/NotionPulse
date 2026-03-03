import customtkinter

class BtnForm(customtkinter.CTkButton):
    def __init__(self,master,**kwargs):
        super().__init__(master, text="Valider", **kwargs)

       
