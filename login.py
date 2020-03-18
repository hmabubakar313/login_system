from tkinter import*
from PIL import ImageTk
from tkinter import messagebox


class Login_system:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1500x900+0+0")

        # images
        self.bg_icon = ImageTk.PhotoImage(file="bg.jpg")
        self.logo_icon = PhotoImage(file="logo.png")
        self.pass_icon = ImageTk.PhotoImage(file="pass.png")
        self.user_icon = PhotoImage(file="user.png")

        # variables
        self.username = StringVar()
        self.password = StringVar()

        bg_lbl = Label(self.root, image=self.bg_icon).pack()
        title = Label(self.root, text="Login System", font=(
            "Arial", 40, "bold  "), bg="DeepSkyBlue", fg="White", bd=10, relief=GROOVE)
        # title.place(x=0, y=0, relwidth=1)
        title.place(x=0, y=0, relwidth=1)

        Login_Frame = Frame(self.root, bg="white")
        Login_Frame.place(x=400, y=150)

        logolbl = Label(Login_Frame, image=self.logo_icon, bd=0).grid(
            row=0, columnspan=2, pady=20)

        lbluser = Label(Login_Frame, text="Username", image=self.user_icon, compound=LEFT, font=(
            "Arial", 40, "bold  "), bg="White").grid(
            row=1, column=0, padx=20, pady=10)
        txtuser = Entry(Login_Frame,  bd=5, textvariable=self.username, relief=GROOVE,
                        font=("", 15)).grid(row=1, column=1, padx=20)

        lblpass = Label(Login_Frame, text="Password", image=self.pass_icon, compound=LEFT, font=(
            "Arial", 40, "bold  "), bg="White").grid(
            row=2, column=0, padx=20, pady=10)
        txtpass = Entry(Login_Frame,  bd=5, relief=GROOVE, textvariable=self.password,
                        font=("", 15)).grid(row=2, column=1, padx=20)

        btn_log = Button(Login_Frame, text="Login Here", width=10, font=(
            "Arial", 40, "bold  "), bg="DeepSkyBlue", fg="White").grid(
            row=3, column=1,  pady=10)

    def login(self):
        if self.username.get() == "" and self.password_.get() == "":
            messagebox.showerror("Error", "Please enter all the fields")


root = Tk()
obj = Login_system(root)
root.mainloop()
