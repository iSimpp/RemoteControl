import os
from tkinter import Tk, Label, Entry, Button, messagebox

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_token(token, directory):
    try:
        create_directory(directory)
        token_file_path = os.path.join(directory, "token.txt")  # Specify the file name
        with open(token_file_path, 'w') as token_file:
            token_file.write(token)
    except Exception:
        return token

def read_token(directory):
    try:
        token_file_path = os.path.join(directory, "token.txt")  # Specify the file name
        if os.path.exists(token_file_path):
            with open(token_file_path, 'r') as token_file:
                return token_file.read().strip()
    except Exception as e:
        print("error: ", e)
    else:
        return None

def show_token_popup(directory):
    root = Tk()
    root.title("Enter Bot Token")
    root.geometry("500x300")
    root.configure(bg="#1e1e1e")

    label = Label(root, text="Enter your bot's token:", bg="#1e1e1e", fg="white", font=("Arial", 14))
    label.pack(pady=20)

    entry = Entry(root, width=50, font=("Arial", 12))
    entry.pack()

    def save_and_close():
        token = entry.get()
        if token:
            save_token(token, directory)
            root.destroy()
        else:
            messagebox.showerror("Error", "Please enter a valid token.")

    button = Button(root, text="Submit", command=save_and_close, bg="#303030", fg="white", font=("Arial", 12))
    button.pack(pady=20)

    root.mainloop()
