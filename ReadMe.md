🔧 Installation Manual
1️⃣ System Requirements
Before installing and running the application, ensure that you have the following installed on your system:

✅ Software Requirements:
Python 3.8 or higher (Check with python --version)

Pip (Python Package Installer) (Check with pip --version)

Git (Optional for cloning the repository)

✅ Python Libraries Required:
customtkinter (for a modern UI)

tkinter (built into Python)

messagebox (for pop-up alerts, included in tkinter)

2️⃣ Installation Steps
Step 1: Download the Project
(A) Clone from GitHub (Recommended)
If you have Git installed, you can clone the repository using:

bash
Copy
Edit
git clone https://github.com/Isaac-Zimba-J/Chinese-wall-model-code---CS440-.git
cd Chinese-wall-model-code---CS440-
(B) Download Manually
Go to the GitHub repository: GitHub Link

Click on the green "Code" button.

Select "Download ZIP".

Extract the ZIP file to a desired location.

Step 2: Install Required Dependencies
Navigate to the project folder and install required dependencies:

bash
Copy
Edit
pip install customtkinter
Step 3: Run the Application
Now, you can start the program by running:

bash
Copy
Edit
python main.py
If using Windows, you can also double-click main.py to run it.

3️⃣ Troubleshooting Common Issues
Issue Solution
Command 'python' not found Use python3 instead of python.
Pip not installed Install pip using python -m ensurepip --default-pip.
customtkinter module not found Run pip install customtkinter again.
Window doesn't open Ensure tkinter is properly installed (python -m tkinter).
📌 Expanded User Guide
🎯 Introduction
This application simulates the Chinese Wall Model, a security policy designed to prevent conflicts of interest by restricting access to company data.

In this simulation, users interact with financial companies, and the system enforces access control rules. If a user writes to one company, they are blocked from writing to a competitor in the same conflict-of-interest (COI) group.

🛠 How to Use the Application
Step 1: Launch the App
After installation, run:

bash
Copy
Edit
python main.py
The application window will open.

Step 2: Home Page
Upon opening, you'll see the Home Page with an introduction to the Chinese Wall Model.

🚀 Actions:

Click "Start Simulation" to proceed.

Read the explanation carefully before continuing.

Step 3: Enter User & Company Details
Once in the main interface:

Enter a User's Name (e.g., Alice, Bob).

Enter a Company Name (e.g., Citibank, Shell).

Choose an Action:

📖 Read: Allows the user to view company data (no restrictions).

✍️ Write: Writes to the company (triggers COI restrictions).

Step 4: Observe the Results
After performing an action, the system will:

Show a confirmation message in the UI.

Display a popup message explaining the outcome.

📌 Examples of Scenarios

Scenario Expected Result
Bob reads Citibank ✅ Allowed
Bob writes to Citibank ✅ Allowed
Bob tries to write to Bank of America (same COI group) ❌ Denied (Conflict detected)
Alice reads Shell ✅ Allowed
Alice writes to Mobil ✅ Allowed
Alice tries to write to Texaco (same COI group) ❌ Denied (Conflict detected)
Step 5: Experiment with Different Users
Each user has an independent access history.

Try different company names and observe how conflicts occur.

🔍 How Does the Chinese Wall Model Work Here?
The Chinese Wall Model prevents a user from writing to two competing companies in the same Conflict of Interest (COI) group.

Example COI Groups in this app:

Banking Industry: Citibank, Bank of America, Bank of the West

Oil & Gas Industry: Shell, Mobil, Texaco, Sunoco

If a user writes to Citibank, they will not be able to write to Bank of America or Bank of the West but can still interact with oil companies like Shell.

🎨 Features of the App
✔ Modern UI with CustomTkinter (Dark Mode)
✔ User-Friendly Navigation (Home → Simulation → Back)
✔ Conflict Detection & Alerts
✔ Pop-Up Messages for Better Understanding
✔ Real-Time COI Enforcement

🌟 Advanced Usage & Customization
🔹 How to Add More Companies
Modify the coi_groups dictionary in main.py:

python
Copy
Edit
self.coi_groups = {
"Bank": {"Citibank", "Bank of America", "Bank of the West"},
"Gasoline": {"Shell", "Mobil", "Sunoco", "Texaco"},
"Tech": {"Google", "Microsoft", "Apple"}
}
🔹 How to Reset User Access
Modify self.user_access = {} in main.py.

🔹 How to Change UI Theme
In main.py, change:

python
Copy
Edit
ctk.set_appearance_mode("dark") # Options: "light", "dark", "system"
🎯 Conclusion
The Chinese Wall Model prevents unethical access to sensitive business data. This GUI simulates how a security policy controls data access based on conflicts of interest. 🔒

🚀 Try different users and company interactions to see access rules in action! 🚀
