#Jared Stephenson's Quiz Version 6 (Final Version)
from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.title("Quiz")
root.geometry("400x200")

i = 0
score = 0

def main_routine():
    global i
    global score
    
    main_frame = Frame(root)
    main_frame.pack()
    
    q1 = "Which company owns the video game Minecraft?"
    q2 = "Which company owns the video game Grand Theft Auto V?"
    q3 = "Which company owns the video game Rust?"
    q4 = "Which company owns the video game Counter Strike: Global Offensive?"
    q5 = "Which company owns the video game franchise Assassin's Creed?"       
    questions = [q1, q2, q3, q4, q5]
    
    q1_options = ["Microsoft", "Bethesda", "Square Enix"] 
    q2_options = ["Rockstar Games", "Epic Games", "Activision"]
    q3_options = ["Activison", "Facepunch Studios", "Valve"]
    q4_options = ["Valve", "Activison", "Bethesda"]
    q5_options = ["Rockstar Games", "Nintendo", "Ubisoft"]
    options = [q1_options, q2_options, q3_options, q4_options, q5_options]    
    
    a1 = "Microsoft"
    a2 = "Rockstar Games"
    a3 = "Facepunch Studios"
    a4 = "Valve"
    a5 = "Ubisoft"
    answers = [a1, a2, a3, a4, a5]
    
    def submit_button_function():
        global i
        global score        
        try:
            if options_combobox.get() == answers[i]:
                answer_label.configure(text="Correct")
                i += 1
                score += 1
                options_combobox.configure(values=options[i])
                question_label.configure(text=questions[i])
                options_combobox.set("Choose an option.")
            else:
                answer_label.configure(text="Incorrect")
                i += 1
                options_combobox.configure(values=options[i])
                question_label.configure(text=questions[i])
                options_combobox.set("Choose an option.")
        except IndexError:
            retry_messagebox = messagebox.askquestion(title="Score", message=f"You scored {score}/5\nWould you like to restart?")
            if retry_messagebox == "yes":
                i = 0
                score = 0                
                main_frame.destroy()
                main_routine()
                
            else:
                root.destroy()
            
    def skip_button_function():
        global i
        global score
        try:
            answer_label.configure(text="Skipped Question.")
            i += 1
            options_combobox.configure(values=options[i])
            question_label.configure(text=questions[i])
            options_combobox.set("Choose an option.")  
        except IndexError:
            retry_messagebox = messagebox.askquestion(title="Score", message=f"You scored {score}/5\nWould you like to restart?")
            if retry_messagebox == "yes":
                i = 0
                score = 0                
                main_frame.destroy()
                main_routine()
                
            else:
                root.destroy()

    question_label = Label(main_frame, text=questions[i])
    question_label.pack(padx=5, pady=5)
    
    options_combobox = ttk.Combobox(main_frame, values=options[i])
    options_combobox.set("Choose an option.")
    options_combobox.pack(padx=5, pady=5)
    
    submit_button = Button(main_frame, text="Submit", command=submit_button_function)
    submit_button.pack(padx=5, pady=5)
    
    skip_button = Button(main_frame, text="Skip Question", command=skip_button_function)
    skip_button.pack(padx=5, pady=5)
    
    answer_label = Label(main_frame)
    answer_label.pack(padx=5, pady=5)
    
    
main_routine()

root.mainloop()
                   
