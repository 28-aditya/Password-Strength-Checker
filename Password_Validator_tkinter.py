import customtkinter as tk
from PIL import Image

class App:
    def __init__(self):
        # Window setup
        self.mainApp = tk.CTk()
        self.mainApp.title("Password Strength Checker")
        self.mainApp.geometry("600x775")
        self.mainApp.resizable(False, False)
        self.mainApp.iconbitmap("images/logo.ico")

        # Set color theme
        tk.set_appearance_mode("dark")
        tk.set_default_color_theme("blue")
        
        # Configure grid for main window
        self.mainApp.grid_columnconfigure(0, weight=1)
        
        # Header Frame
        self.headerFrame = tk.CTkFrame(self.mainApp, fg_color="transparent")
        self.headerFrame.grid(row=0, column=0, pady=0, padx=0, sticky="ew")
        
        # Logo
        logoPIL = Image.open("images/logo.png")
        self.logoImage = tk.CTkImage(light_image=logoPIL,
                                     dark_image=logoPIL,
                                     size = (125,125)
                                    )
        self.logoLabel = tk.CTkLabel(
            self.headerFrame,
            image = self.logoImage,
            text="",
            font=("Arial", 80)
        )
        self.logoLabel.pack()
        
        # Title
        self.titleLabel = tk.CTkLabel(
            self.headerFrame,
            text="Password Strength Checker",
            font=("Helvetica", 32, "bold"),
            text_color="#3b8ed0"
        )
        self.titleLabel.pack(pady=(10, 5))
        
        # Subtitle
        self.subtitleLabel = tk.CTkLabel(
            self.headerFrame,
            text="Create a secure password that protects your account",
            font=("Helvetica", 14),
            text_color="#a0a0a0"
        )
        self.subtitleLabel.pack()
        
        # Instructions Frame
        self.instructionsFrame = tk.CTkFrame(self.mainApp, corner_radius=15)
        self.instructionsFrame.grid(row=1, column=0, pady=20, padx=40, sticky="ew")
        
        self.instructionsTitle = tk.CTkLabel(
            self.instructionsFrame,
            text="📋 Instructions",
            font=("Helvetica", 16, "bold"),
            anchor="w"
        )
        self.instructionsTitle.pack(pady=(15, 5), padx=20, anchor="w")
        
        instructions_text = "• Enter your first and last name\n• Create a strong password\n• Password should not contain your name\n• Use a mix of letters, numbers, and symbols"
        self.instructionsLabel = tk.CTkLabel(
            self.instructionsFrame,
            text=instructions_text,
            font=("Helvetica", 13),
            justify="left",
            anchor="w",
            text_color="#c0c0c0"
        )
        self.instructionsLabel.pack(pady=(0, 15), padx=20, anchor="w")
        
        # Input Form Frame
        self.formFrame = tk.CTkFrame(self.mainApp, corner_radius=15)
        self.formFrame.grid(row=2, column=0, pady=10, padx=40, sticky="ew")
        
        # Configure form grid
        self.formFrame.grid_columnconfigure(0, weight=1)
        self.formFrame.grid_columnconfigure(1, weight=1)
        
        # Name Section Label
        self.nameSectionLabel = tk.CTkLabel(
            self.formFrame,
            text="Personal Information",
            font=("Helvetica", 16, "bold"),
            anchor="w"
        )
        self.nameSectionLabel.grid(row=0, column=0, columnspan=2, pady=(20, 10), padx=20, sticky="w")
        
        # First Name
        self.firstNameTB = tk.CTkEntry(
            self.formFrame,
            placeholder_text="First Name",
            height=45,
            font=("Helvetica", 14),
            corner_radius=10
        )
        self.firstNameTB.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="ew")
        
        # Last Name
        self.lastNameTB = tk.CTkEntry(
            self.formFrame,
            placeholder_text="Last Name",
            height=45,
            font=("Helvetica", 14),
            corner_radius=10
        )
        self.lastNameTB.grid(row=1, column=1, padx=(10, 20), pady=10, sticky="ew")
        
        # Password Section Label
        self.passwordSectionLabel = tk.CTkLabel(
            self.formFrame,
            text="Password",
            font=("Helvetica", 16, "bold"),
            anchor="w"
        )
        self.passwordSectionLabel.grid(row=2, column=0, columnspan=2, pady=(20, 10), padx=20, sticky="w")
        
        # Password Entry
        self.passwordTB = tk.CTkEntry(
            self.formFrame,
            placeholder_text="Enter your password",
            show="•",
            height=45,
            font=("Helvetica", 14),
            corner_radius=10
        )
        self.passwordTB.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
        
        # Show/Hide Password Toggle
        self.showPasswordVar = tk.BooleanVar()
        self.showPasswordCheckbox = tk.CTkCheckBox(
            self.formFrame,
            text="Show password",
            variable=self.showPasswordVar,
            command=self.togglePassword,
            font=("Helvetica", 12)
        )
        self.showPasswordCheckbox.grid(row=4, column=0, columnspan=2, padx=20, pady=(5, 20), sticky="w")
        
        # Results Frame (for password validation feedback)
        self.resultsFrame = tk.CTkFrame(self.mainApp, corner_radius=15, fg_color="transparent")
        self.resultsFrame.grid(row=3, column=0, pady=10, padx=40, sticky="ew")
        
        # Validation feedback label (shows failed requirements in red)
        self.validationLabel = tk.CTkLabel(
            self.resultsFrame,
            text="",
            font=("Helvetica", 13),
            text_color="#ff4444",
            justify="left",
            anchor="w"
        )
        self.validationLabel.pack(pady=10, padx=20, anchor="w")
                       
        # Submit Button
        self.submissionButton = tk.CTkButton(
            self.mainApp,
            text="Check Password Strength",
            command=self.passwordSubmission,
            height=50,
            font=("Helvetica", 16, "bold"),
            corner_radius=10,
            fg_color="#3b8ed0",
            hover_color="#7d0cc3"
        )
        self.submissionButton.grid(row=3, column=0, pady=20, padx=40, sticky="ew")
        
        # Footer
        self.footerLabel = tk.CTkLabel(
            self.mainApp,
            text="Tip: A strong password is at least 12 characters long",
            font=("Helvetica", 11),
            text_color="#585252"
        )
        self.footerLabel.grid(row=5, column=0, pady=(0, 20))
        
        self.mainApp.mainloop()
    
    def togglePassword(self):
        # Toggle password visibility
        if self.showPasswordVar.get():
            self.passwordTB.configure(show="")
        else:
            self.passwordTB.configure(show="•")
    
    def passwordSubmission(self):
        print("Password submission triggered")
        self.firstName = self.firstNameTB.get().strip()
        self.lastName = self.lastNameTB.get().strip()
        self.password = self.passwordTB.get().strip()

        print(f"First Name: {self.firstName}")
        print(f"Last Name: {self.lastName}")
        print(f"Password: {self.password}")
        print(self.firstName,self.lastName)

        
App()