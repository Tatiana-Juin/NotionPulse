import customtkinter
# from btn_form import BtnForm

class Form(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master,fg_color="#F9F9F9")
        
        self.question = customtkinter.CTkEntry(self,placeholder_text="Test a saisir");
        self.question.grid(row=2,column=1, padx=3,pady=3)

        # self.btn_frame = BtnForm(self)
        # self.btn_frame.grid(row=2,column=2,pady=3,padx=3)

