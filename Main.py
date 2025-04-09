import os
# Suppress Tk deprecation warning
os.environ['TK_SILENCE_DEPRECATION'] = '1'

import customtkinter as ctk
import datetime
from typing import Set, Dict, List

class ChineseWallModel:
    def __init__(self):
        self.user_access: Dict[str, Set[str]] = {}  # Tracks what a user has accessed
        self.access_log: List[Dict] = []  # Logs all access attempts
        self.coi_groups = {
            "Bank": {"Citibank", "Bank of America", "Bank of the West"},
            "Gasoline": {"Shell", "Mobil", "Sunoco", "Texaco"},
            "Technology": {"Apple", "Microsoft", "Google", "Amazon"}
        }
        self.valid_companies = {company for companies in self.coi_groups.values() for company in companies}

    def log_access(self, user: str, company: str, action: str, success: bool, reason: str = "") -> None:
        """Log an access attempt with timestamp and details."""
        log_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "user": user,
            "company": company,
            "action": action,
            "success": success,
            "reason": reason
        }
        self.access_log.append(log_entry)

    def get_user_access_history(self, user: str) -> List[Dict]:
        """Get access history for a specific user."""
        return [entry for entry in self.access_log if entry["user"] == user]

    def get_conflict_report(self, user: str) -> Dict:
        """Generate a conflict report for a user."""
        if user not in self.user_access:
            return {"conflicts": [], "access_history": []}
        
        conflicts = []
        accessed_groups = {group for group, companies in self.coi_groups.items() 
                         if self.user_access[user] & companies}
        
        for group, companies in self.coi_groups.items():
            if group in accessed_groups:
                conflicts.extend(companies - self.user_access[user])
        
        return {
            "conflicts": list(conflicts),
            "access_history": self.get_user_access_history(user)
        }

    def can_read(self, user: str, company: str) -> tuple[bool, str]:
        """Check if a user can read from a company."""
        if company not in self.valid_companies:
            return False, "Invalid company"
        return True, ""

    def can_write(self, user: str, company: str) -> tuple[bool, str]:
        """Check if a user can write to a company."""
        if company not in self.valid_companies:
            return False, "Invalid company"
            
        if user not in self.user_access:
            return True, "First-time access allowed"
            
        accessed_groups = {group for group, companies in self.coi_groups.items() 
                         if self.user_access[user] & companies}
        
        for group, companies in self.coi_groups.items():
            if company in companies and group in accessed_groups:
                return False, f"Conflict of interest: Cannot write to {company} after accessing {group} group"
        
        return True, ""

    def access_company(self, user: str, company: str, action: str) -> tuple[bool, str]:
        """Attempt to access a company with proper logging."""
        if not user or not company:
            return False, "User and company must be specified"
            
        if action == "read":
            can_access, reason = self.can_read(user, company)
            if can_access:
                self.user_access.setdefault(user, set()).add(company)
                self.log_access(user, company, action, True)
                return True, f"{user} read {company} successfully."
            else:
                self.log_access(user, company, action, False, reason)
                return False, f"Read access denied: {reason}"
                
        elif action == "write":
            can_access, reason = self.can_write(user, company)
            if can_access:
                self.user_access.setdefault(user, set()).add(company)
                self.log_access(user, company, action, True)
                return True, f"{user} wrote to {company} successfully."
            else:
                self.log_access(user, company, action, False, reason)
                return False, f"Write access denied: {reason}"
                
        return False, "Invalid action specified"

class ChineseWallGUI:
    def __init__(self):
        self.system = ChineseWallModel()
        
        # Configure the appearance mode and color theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Create the main window
        self.root = ctk.CTk()
        self.root.title("Chinese Wall Model - Conflict of Interest Management")
        self.root.geometry("800x600")
        
        # Create main frame
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Header
        self.header_label = ctk.CTkLabel(
            self.main_frame,
            text="Chinese Wall Model - Conflict of Interest Management System",
            font=("Arial", 20, "bold")
        )
        self.header_label.pack(pady=20)
        
        # Instructions
        instructions = """
        This system enforces conflict-of-interest (COI) policies by preventing access to competing companies.
        
        Instructions:
        1. Enter your name as the user
        2. Select a company from the dropdown
        3. Choose an action (Read/Write)
        4. View the access result and conflict report
        
        The system will automatically detect and prevent conflicts of interest.
        """
        
        self.instructions_label = ctk.CTkLabel(
            self.main_frame,
            text=instructions,
            wraplength=700,
            justify="left"
        )
        self.instructions_label.pack(pady=10)
        
        # Input form frame
        self.form_frame = ctk.CTkFrame(self.main_frame)
        self.form_frame.pack(fill="x", pady=20, padx=20)
        
        # User input
        self.user_label = ctk.CTkLabel(self.form_frame, text="User:")
        self.user_label.grid(row=0, column=0, padx=10, pady=10)
        self.user_entry = ctk.CTkEntry(self.form_frame, width=200)
        self.user_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Company selection
        self.company_label = ctk.CTkLabel(self.form_frame, text="Company:")
        self.company_label.grid(row=1, column=0, padx=10, pady=10)
        self.company_var = ctk.StringVar()
        self.company_dropdown = ctk.CTkComboBox(
            self.form_frame,
            values=sorted(self.system.valid_companies),
            variable=self.company_var,
            width=200
        )
        self.company_dropdown.grid(row=1, column=1, padx=10, pady=10)
        
        # Action buttons
        self.button_frame = ctk.CTkFrame(self.form_frame)
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=20)
        
        self.read_button = ctk.CTkButton(
            self.button_frame,
            text="Read",
            command=self.read_action,
            width=100
        )
        self.read_button.pack(side="left", padx=10)
        
        self.write_button = ctk.CTkButton(
            self.button_frame,
            text="Write",
            command=self.write_action,
            width=100
        )
        self.write_button.pack(side="left", padx=10)
        
        self.report_button = ctk.CTkButton(
            self.button_frame,
            text="View Report",
            command=self.show_report,
            width=100
        )
        self.report_button.pack(side="left", padx=10)
        
        # Output area
        self.output_frame = ctk.CTkFrame(self.main_frame)
        self.output_frame.pack(fill="both", expand=True, pady=20, padx=20)
        
        self.output_text = ctk.CTkTextbox(
            self.output_frame,
            height=150,
            width=700,
            wrap="word"
        )
        self.output_text.pack(pady=10, padx=10)
        
        # Status bar
        self.status_var = ctk.StringVar()
        self.status_bar = ctk.CTkLabel(
            self.main_frame,
            textvariable=self.status_var,
            height=30
        )
        self.status_bar.pack(side="bottom", fill="x", pady=10)

    def update_status(self, message: str) -> None:
        """Update the status bar message."""
        self.status_var.set(message)

    def read_action(self) -> None:
        """Handle read action."""
        user = self.user_entry.get().strip()
        company = self.company_var.get().strip()
        
        if not user or not company:
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", "Error: Please enter both user and company")
            return
            
        success, message = self.system.access_company(user, company, "read")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", message)
        self.update_status(f"Last action: Read attempt by {user} on {company}")

    def write_action(self) -> None:
        """Handle write action."""
        user = self.user_entry.get().strip()
        company = self.company_var.get().strip()
        
        if not user or not company:
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", "Error: Please enter both user and company")
            return
            
        success, message = self.system.access_company(user, company, "write")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", message)
        self.update_status(f"Last action: Write attempt by {user} on {company}")

    def show_report(self) -> None:
        """Show the conflict report for the current user."""
        user = self.user_entry.get().strip()
        if not user:
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", "Error: Please enter a user name")
            return
            
        report = self.system.get_conflict_report(user)
        
        # Create report window
        report_window = ctk.CTkToplevel(self.root)
        report_window.title(f"Conflict Report - {user}")
        report_window.geometry("600x400")
        
        # Create notebook for tabs
        notebook = ctk.CTkTabview(report_window)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Conflicts tab
        conflicts_tab = notebook.add("Conflicts")
        conflicts_text = ctk.CTkTextbox(conflicts_tab, wrap="word")
        conflicts_text.pack(fill="both", expand=True, padx=10, pady=10)
        
        if report["conflicts"]:
            conflicts_text.insert("1.0", "Current Conflicts of Interest:\n\n")
            for company in report["conflicts"]:
                conflicts_text.insert("end", f"• Cannot access {company}\n")
        else:
            conflicts_text.insert("1.0", "No current conflicts of interest")
        
        # History tab
        history_tab = notebook.add("Access History")
        history_text = ctk.CTkTextbox(history_tab, wrap="word")
        history_text.pack(fill="both", expand=True, padx=10, pady=10)
        
        if report["access_history"]:
            history_text.insert("1.0", "Access History:\n\n")
            for entry in report["access_history"]:
                history_text.insert("end", 
                    f"• {entry['timestamp']}: {entry['action'].upper()} {entry['company']} - "
                    f"{'Success' if entry['success'] else 'Denied'}\n")
        else:
            history_text.insert("1.0", "No access history found")

if __name__ == "__main__":
    app = ChineseWallGUI()
    app.root.mainloop()
