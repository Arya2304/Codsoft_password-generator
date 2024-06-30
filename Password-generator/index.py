import customtkinter as ctk
import random
import string

# Function to generate password
def generate_password():
    length = int(length_entry.get())
    difficulty = difficulty_slider.get()
    
    characters = string.ascii_letters
    if difficulty >= 2:
        characters += string.digits
    if difficulty == 3:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    password_display.configure(text=password)

# Initialize the application window
app = ctk.CTk()
app.title("Password Generator")
app.geometry("400x300")

# Length entry
ctk.CTkLabel(app, text="Password Length:").pack(pady=10)
length_entry = ctk.CTkEntry(app)
length_entry.pack(pady=10)

# Difficulty slider
ctk.CTkLabel(app, text="Password Difficulty:").pack(pady=10)
difficulty_slider = ctk.CTkSlider(app, from_=1, to=3, number_of_steps=2)
difficulty_slider.pack(pady=10)

# Generate button
generate_button = ctk.CTkButton(app, text="Generate Password", command=generate_password)
generate_button.pack(pady=20)

# Display generated password
password_display = ctk.CTkLabel(app, text="")
password_display.pack(pady=10)

# Run the application
app.mainloop()
