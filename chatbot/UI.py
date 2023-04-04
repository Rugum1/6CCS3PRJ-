from tkinter import *
import json 
import customtkinter
import helpers 
import chatbot

#This class was taken from https://github.com/TomSchimansky/CustomTkinter and adapted to the project.

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # #create chatbot 
        self.bot = chatbot.ChatBotStudentAid()
       
        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Chatbot", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.clear_chat_log,text = "Clear")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.text_box_label =  customtkinter.CTkLabel(self.sidebar_frame, text="Concepts covered by the chatbot", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.text_box_label.grid(row=2, column=0, padx=20, pady=(20, 10))
        
        self.terms_covered_text_box =  customtkinter.CTkTextbox(self.sidebar_frame, width=140)
        self.terms_covered_text_box.grid(row=3, column=0, padx=20, pady=10,sticky = "nsew")
        self.populate_terms_text_box()

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        
        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Type a question")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),command =self.input_button_event,text = "Submit")
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, rowspan=3, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox.configure(state= 'disabled')

        #Create context text box 
        self.context_textbox = customtkinter.CTkTextbox(self, width=250)
        self.context_textbox.grid(row=0, column=3,rowspan=3, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.context_textbox.configure(state= 'disabled')


        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        
    def input_button_event(self):
        self.textbox.configure(state= 'normal')
        self.context_textbox.configure(state = "normal")
        
        self.textbox.insert(END, self.entry.get() + '\n')
        self.context_textbox.delete('1.0', END)
        context = helpers.get_context_without_tokenized_query(self.entry.get())
        self.context_textbox.insert(END, context)

        user_query = self.entry.get()
        self.entry.delete("0",END)
        
        bot_answer =  self.bot.get_answer(user_query)

        self.textbox.insert(END, bot_answer.text + '\n')
        self.textbox.insert(END, " " + '\n')
        self.textbox.configure(state= 'disabled')
        self.context_textbox.configure(state = 'disabled')
    
    def clear_chat_log(self): 
        self.textbox.configure(state= 'normal')
        self.context_textbox.configure(state = 'normal')
        self.textbox.delete('1.0', END)
        self.context_textbox.delete('1.0', END)
        self.textbox.configure(state= 'disabled')
        self.context_textbox.configure(state = 'disabled')

    def get_answer_from_bot(self,query): 
        return self.bot.get_answer(self.entry.get())
   
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def populate_terms_text_box(self): 
        with open("data/terms_covered_concat.json" , "r", encoding ="utf-8") as f:
            data = json.load(f)

            for term in data: 
                self.terms_covered_text_box.insert(END, term + '\n')
            
            self.terms_covered_text_box.configure(state = 'disabled')

if __name__ == "__main__":
    app = App()
    app.mainloop()