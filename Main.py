


import tkinter as tk
from tkinter import messagebox

class ChineseWallModel:
    def __init__(self):
        self.user_access = {}  # Tracks what a user has accessed
        self.coi_groups = {
            "Bank": {"Citibank", "Bank of America", "Bank of the West"},
            "Gasoline": {"Shell", "Mobil", "Sunoco", "Texaco"}
        }

    def can_read(self, user, company):
        return True  # Users can always read any company

    def can_write(self, user, company):
        if user not in self.user_access:
            return True  # First-time users can write to any caompany

        accessed_groups = {group for group, companies in self.coi_groups.items() if self.user_access[user] & companies}
        
        for group, companies in self.coi_groups.items():
            if company in companies and group in accessed_groups:
                return False  # Conflict detected, cannot write
        
        return True

    def access_company(self, user, company, action):
        if action == "read":
            self.user_access.setdefault(user, set()).add(company)
            return f"{user} read {company}.\nYou can now attempt to write, but be aware of potential conflicts."
        elif action == "write":
            if self.can_write(user, company):
                self.user_access.setdefault(user, set()).add(company)
                return f"{user} wrote to {company}.\nYou may be restricted from writing to competing companies now."
            else:
                return f"Access denied: {user} cannot write to {company} due to conflict-of-interest rules.\nYou have previously accessed a competing company."

class ChineseWallGUI:
    def __init__(self, root):
        self.system = ChineseWallModel()
        self.root = root
        self.root.title("Chinese Wall Model")
        self.root.geometry("600x450")
        
        intro_text = """
        Welcome to the Chinese Wall Model Simulation!
        This system enforces conflict-of-interest (COI) policies.
        You will learn how access control is implemented to prevent information leakage.
        """
        
        tk.Label(root, text=intro_text, wraplength=580, justify="left", fg="black", font=("Arial", 12, "bold")).pack(pady=10)
        
        instruction_text = """
        Instructions:
        1. Enter your name as the user.
        2. Enter the company you want to access.
        3. Click "Read" to access the company's data.
        4. Click "Write" to attempt modifying the company's data.
        5. The system will determine if access is allowed based on COI rules.
        """
        
        tk.Label(root, text=instruction_text, wraplength=580, justify="left", fg="White").pack(pady=5)
        
        form_frame = tk.Frame(root)
        form_frame.pack(pady=10)
        
        tk.Label(form_frame, text="User:").grid(row=0, column=0)
        self.user_entry = tk.Entry(form_frame)
        self.user_entry.grid(row=0, column=1)

        tk.Label(form_frame, text="Company:").grid(row=1, column=0)
        self.company_entry = tk.Entry(form_frame)
        self.company_entry.grid(row=1, column=1)

        self.read_button = tk.Button(form_frame, text="Read", command=self.read_action)
        self.read_button.grid(row=2, column=0, pady=10)

        self.write_button = tk.Button(form_frame, text="Write", command=self.write_action)
        self.write_button.grid(row=2, column=1, pady=10)

        self.output_label = tk.Label(root, text="", fg="blue", wraplength=580, justify="left")
        self.output_label.pack(pady=10)

    def read_action(self):
        user = self.user_entry.get()
        company = self.company_entry.get()
        message = self.system.access_company(user, company, "read")
        self.output_label.config(text=message)
        messagebox.showinfo("Result", message)

    def write_action(self):
        user = self.user_entry.get()
        company = self.company_entry.get()
        message = self.system.access_company(user, company, "write")
        self.output_label.config(text=message)
        messagebox.showinfo("Result", message)

if __name__ == "__main__":
    root = tk.Tk()
    gui = ChineseWallGUI(root)
    root.mainloop()
