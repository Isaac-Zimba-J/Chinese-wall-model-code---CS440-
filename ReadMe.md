**Chinese Wall Model Simulation - Installation Manual and Project Description**

## Project Description
The Chinese Wall Model Simulation is a graphical user interface (GUI) application that demonstrates access control rules based on the Chinese Wall security model. This model enforces conflict-of-interest (COI) policies, ensuring that a user cannot access or modify data from competing companies within the same sector once they have interacted with one company in that sector.

**Key Features:**
- Simulates real-world security policies used in financial and business settings.
- Prevents conflicts of interest by restricting access to competing entities.
- Provides interactive guidance to users about read and write operations.
- Displays clear explanations of access permissions and denials.

## Installation Guide
Follow these steps to install and run the Chinese Wall Model Simulation on your computer.

### **Prerequisites**
- Python 3.7 or later must be installed.
- Tkinter (usually included with Python by default).

### **Step 1: Clone the Repository**
Open a terminal or command prompt and run the following command:
```bash
git clone https://github.com/Isaac-Zimba-J/Chinese-wall-model-code---CS440-.git
cd Chinese-wall-model-code---CS440-
```

### **Step 2: Install Dependencies**
Ensure you have Tkinter installed. If not, install it using:
```bash
pip install tk
```

### **Step 3: Run the Application**
Execute the following command in the terminal:
```bash
python main.py
```

### **Step 4: Using the Application**
1. Enter your name as the user.
2. Type the name of the company you want to access.
3. Click **Read** to view company data.
4. Click **Write** to attempt modifying company data.
5. If access is restricted, the system will provide an explanation based on conflict-of-interest rules.

### **Expected Behavior**
- Users can read data from any company.
- Users can write to a company **only if they have not previously accessed a competitor**.
- If a conflict exists, the system will prevent the write operation and notify the user.

### **Troubleshooting**
- If the application does not start, ensure you are running Python 3.
- If dependencies are missing, reinstall them using `pip install tk`.
- If the GUI does not appear, try restarting your system and running the script again.

---

For more details or contributions, visit the project repository: [GitHub Link](https://github.com/Isaac-Zimba-J/Chinese-wall-model-code---CS440-.git).

