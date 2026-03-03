import customtkinter

class BtnForm(customtkinter.CTkButton):
    def __init__(self,master):
        super().__init__(master,fg_color="#F9F9F9")

        self.btn = customtkinter.CTkButton(self,text="Valider")
        self.btn.grid(row=2,column=2,pady=3,padx=3)
