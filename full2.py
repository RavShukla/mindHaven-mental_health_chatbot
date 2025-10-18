import tkinter as tk
from tkinter import messagebox, scrolledtext, font as tkfont
from PIL import Image, ImageTk
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


template = """
Conversation history:
{context}

User question: {question}
Answer:
"""

model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


users_db = {}

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Consult Doctor 🩺")
        self.context = ""
        self.root.state('zoomed')


        self.bg_color = "#1e1e1e"
        self.text_color = "#ffffff"
        self.input_bg = "#2e2e2e"
        self.input_fg = "#ffffff"
        self.bot_color = "#a6e22e"
        self.user_color = "#66d9ef"
        self.chat_font = tkfont.Font(family="Arial", size=16)
        self.input_font = tkfont.Font(family="Arial", size=14)
        self.root.configure(bg=self.bg_color)


        self.chat_display = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, state='disabled', width=60, height=20,
            bg=self.bg_color, fg=self.text_color, font=self.chat_font,
            insertbackground=self.text_color
        )
        self.chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")


        self.user_input = tk.Entry(
            root, width=50, bg=self.input_bg, fg=self.input_fg,
            font=self.input_font, insertbackground=self.input_fg
        )
        self.user_input.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.user_input.bind("<Return>", self.send_message)


        self.send_button = tk.Button(
            root, text="Send", command=self.send_message,
            bg="#444444", fg="#ffffff", font=self.input_font
        )
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)


        self.send_first_message()

    def send_first_message(self):
        first_message = "Hello! I'm Man-Sathi. How can I assist you today?"
        self.display_message("Doctor Bot", first_message, self.bot_color)
        self.context += f"Doctor Bot: {first_message}\n"

    def send_message(self, event=None):
        user_text = self.user_input.get().strip()
        if not user_text:
            return
        if user_text.lower() == "exit":
            self.root.destroy()
            return

        self.display_message("You", user_text, self.user_color)
        self.user_input.delete(0, tk.END)

        # AI response
        response = chain.invoke({
            "context": self.context,
            "question": user_text,
            "text_blob": user_text
        })
        self.display_message("Doctor Bot", response, self.bot_color)
        self.context += f"\nUser: {user_text}\nDoctor Bot: {response}"

    def display_message(self, sender, message, color):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, f"{sender}: {message}\n\n", sender)
        self.chat_display.tag_config(sender, foreground=color, font=self.chat_font)
        self.chat_display.config(state='disabled')
        self.chat_display.yview(tk.END)


class MindHavenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MindHaven - Mental Health Creator")
        self.root.geometry("1000x700")
        self.root.resizable(False, False)

        self.frames = {}
        for F in (HomePage, LoginPage, SignupPage, DashboardPage):
            page_name = F.__name__
            frame = F(parent=root, controller=self)
            self.frames[page_name] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f9faf9")

        tk.Label(self, text="MindHaven", font=("Arial", 36, "bold"), bg="#f9faf9").pack(pady=20)
        tk.Label(self, text='"Healthcare is incomplete without mental care"',
                 font=("Arial", 16), bg="#f9faf9").pack(pady=5)

        btn_frame = tk.Frame(self, bg="#f9faf9")
        btn_frame.pack(pady=20)
        tk.Button(btn_frame, text="Sign Up", width=15, font=("Arial", 14),
                  command=lambda: controller.show_frame("SignupPage")).grid(row=0, column=0, padx=20)
        tk.Button(btn_frame, text="Login", width=15, font=("Arial", 14),
                  command=lambda: controller.show_frame("LoginPage")).grid(row=0, column=1, padx=20)

        tk.Label(self, text="🎯 Objective", font=("Arial", 18, "bold"), bg="#e8f0ed").pack(pady=10)
        tk.Label(self, text="At MindHaven, we genuinely care about you and your well-being. "
                            "This is a safe space where your thoughts are valued and feelings understood.",
                 wraplength=700, justify="center", bg="#e8f0ed", font=("Arial", 14)).pack(pady=5)

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#fff")

        tk.Label(self, text="Login to MindHaven", font=("Arial", 24, "bold"), bg="#fff").pack(pady=20)
        tk.Label(self, text="Email", bg="#fff").pack()
        self.email_entry = tk.Entry(self, width=30, font=("Arial", 14))
        self.email_entry.pack(pady=5)
        tk.Label(self, text="Password", bg="#fff").pack()
        self.pass_entry = tk.Entry(self, width=30, font=("Arial", 14), show="*")
        self.pass_entry.pack(pady=5)
        tk.Button(self, text="Login", font=("Arial", 14), width=15, bg="#3f51b5", fg="#fff",
                  command=self.login_user).pack(pady=20)
        tk.Button(self, text="Back to Home", command=lambda: controller.show_frame("HomePage")).pack()

    def login_user(self):
        email = self.email_entry.get().strip()
        password = self.pass_entry.get().strip()
        if email in users_db and users_db[email]["password"] == password:
            messagebox.showinfo("Login Success", f"Welcome back {users_db[email]['name']}!")
            self.controller.show_frame("DashboardPage")
        else:
            messagebox.showerror("Login Failed", "Invalid email or password!")

class SignupPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#fff")

        tk.Label(self, text="Sign Up for MindHaven", font=("Arial", 24, "bold"), bg="#fff").pack(pady=20)
        tk.Label(self, text="Name", bg="#fff").pack()
        self.name_entry = tk.Entry(self, width=30, font=("Arial", 14))
        self.name_entry.pack(pady=5)
        tk.Label(self, text="Email", bg="#fff").pack()
        self.email_entry = tk.Entry(self, width=30, font=("Arial", 14))
        self.email_entry.pack(pady=5)
        tk.Label(self, text="Password", bg="#fff").pack()
        self.pass_entry = tk.Entry(self, width=30, font=("Arial", 14), show="*")
        self.pass_entry.pack(pady=5)
        tk.Button(self, text="Sign Up", font=("Arial", 14), width=15, bg="#007bff", fg="#fff",
                  command=self.signup_user).pack(pady=20)
        tk.Button(self, text="Back to Home", command=lambda: controller.show_frame("HomePage")).pack()

    def signup_user(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.pass_entry.get().strip()
        if not name or not email or not password:
            messagebox.showwarning("Validation Error", "All fields are required!")
            return
        if len(password) < 6:
            messagebox.showwarning("Validation Error", "Password must be at least 6 characters!")
            return
        users_db[email] = {"name": name, "password": password}
        messagebox.showinfo("Success", f"Account created for {name}!")
        self.controller.show_frame("LoginPage")

class DashboardPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f0f4f8")

        tk.Label(self, text="Dashboard", font=("Arial", 28, "bold"), bg="#f0f4f8").pack(pady=20)

        widget_frame = tk.Frame(self, bg="#f0f4f8")
        widget_frame.pack(pady=20)

        # Load images (replace with your own file paths)
        try:
            doctor_img = Image.open("images/consult_doctor.png").resize((120, 120))
            self.doctor_photo = ImageTk.PhotoImage(doctor_img)
        except:
            self.doctor_photo = None

        try:
            analysis_img = Image.open("images/analyze.png").resize((120, 120))
            self.analysis_photo = ImageTk.PhotoImage(analysis_img)
        except:
            self.analysis_photo = None

        # Consult Doctor Button
        tk.Button(widget_frame, text="Consult Doctor", font=("Arial", 16), width=25, height=2,
                  image=self.doctor_photo, compound="top",
                  command=self.open_chatbot).grid(row=0, column=0, padx=20, pady=10)

        # Analyze Mental Health Button
        tk.Button(widget_frame, text="Analyze Mental Health", font=("Arial", 16), width=25, height=2,
                  image=self.analysis_photo, compound="top",
                  command=self.under_maintenance).grid(row=0, column=1, padx=20, pady=10)

        tk.Button(self, text="Logout", font=("Arial", 14),
                  command=lambda: controller.show_frame("HomePage")).pack(pady=20)

    def open_chatbot(self):
        chatbot_window = tk.Toplevel(self.controller.root)
        ChatbotApp(chatbot_window)

    def under_maintenance(self):
        messagebox.showinfo("🚧 Under Maintenance", "This feature is currently under maintenance. Please check back later!")



if __name__ == "__main__":
    root = tk.Tk()
    app = MindHavenApp(root)
    root.mainloop()
