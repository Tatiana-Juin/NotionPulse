import customtkinter;
from views.form import Form
class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Application Notion")
        self.geometry("1000x600")
        self.configure(fg_color="#F9F9F9")
        # Titre du formulaire  
        self.titre = customtkinter.CTkLabel(self, text=" Question récurente")
        self.titre.grid(row=1,column=1,pady=3,padx=3)

        # Appelle du formulaire 
        self.saisie_frame = Form(self)
        self.saisie_frame.grid(row=2,column=1, padx=3,pady=3)
        

main = Main()
main.mainloop()

