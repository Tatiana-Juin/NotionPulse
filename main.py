import customtkinter;

class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Application Notion")
        self.geometry("500x500")
        self.configure(fg_color="#F9F9F9")

main = Main()
main.mainloop()

