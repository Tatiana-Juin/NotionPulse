import customtkinter;
from views.form import Form
class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Application Notion")
        self.geometry("500x500")
        self.configure(fg_color="#F9F9F9")

        # Appelle du formulaire 
        self.saisie_frame = Form(self)
        self.saisie_frame.grid(row=2,column=1, padx=3,pady=3)
        

main = Main()
main.mainloop()

