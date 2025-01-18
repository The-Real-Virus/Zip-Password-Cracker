# 💀Zip Password Cracker💀

## 📜Description
Welcome to the ZIP Password Cracker! This Python script is a lightweight tool designed to help you  
crack password-protected ZIP files using a dictionary attack.  
It's easy to use, interactive, and a great demonstration of Python scripting  
for file manipulation and password testing.  

## 🔑Features
- Banner Display: A cool ASCII-art banner to make the script visually appealing.  
- Interactive Prompts: Simple and intuitive prompts guide the user through the process.  
- Progress Feedback: See which password is being tried in real-time.  
- Error Handling: Comprehensive error handling ensures the script doesn’t crash due to missing files or invalid ZIP files.  
- Compatibility: Works seamlessly across major platforms (Windows, Linux, macOS).  

## 🚀Step-by-Step Guide in Linux Terminal !

Step 1: Update & upgrade your system  
>sudo apt update  
>sudo apt upgrade  

Step 2: Clone the repository  
>git clone https://github.com/The-Real-Virus/Zip-Password-Cracker.git  

Step 3: Go to the Tool Directory where u clone it and read requirements.txt file !  
>cd Zip-Password-Cracker  
(read requirements.txt file using cat or gedit)  

Step 4: extract the rockyou file using unrar  
>sudo apt install unrar (if it is not installed in ur kali linux)  
>unrar x rockyou.rar  

Step 5: After Completing the process now u can run script  
>python3 Script.py  

## ⚙️Troubleshooting

1) `Error: File Not Found`  
- Ensure the ZIP file and the password list are in the same directory as the script, or provide the correct file path.  

2) `Error: The ZIP file is invalid or corrupted`  
- Verify that the ZIP file is not damaged and can be opened manually.  

3) `Passwords not working`  
- Double-check the password list. The correct password may not be included.  

4) `Script doesn’t display correctly`  
- Ensure your terminal or IDE supports UTF-8 encoding for proper banner display.  

## 💡How iT Works !
This script utilizes the zipfile module in Python to extract ZIP files with a password.  
By providing a ZIP file and a password list, it attempts each password from the list until the correct one is found.  
Whether you're a cybersecurity enthusiast or just exploring file security concepts,  
this script is a fun way to dive into the basics of password cracking using Python!  

## 🤝Follow the Prompts !
- The script will guide you step-by-step:  
- Enter the name of the ZIP file you want to crack.  
- Provide the name of the password list file.  
- Watch as the script tests each password and informs you of success or failure.  

## 🛠️MODIFICATION ( use own wordlist )

if u want to use ur own wordlist instead of rockyou.txt , u can modify in the script ,  

Step 1: create ur own wordlist  

Step 2: move it into the Zip-Password-Cracker Directory ( deleting rockyou is not necessory )  

Step 3: While running the script , it ask for password file then type the name of ur own created list .  

## 📂Example Usage
	Welcome to the ZIP Password Cracker!
	Press 'y' to continue or 'n' to exit: y

	Enter the name of the ZIP file (with extension): protected.zip
	Enter the name of the password list file (with extension): rockyou.txt

	Reading password file...
	Trying password 1: 12345
	Trying password 2: password
	Trying password 3: letmein

	Success! Password found: letmein

# ⚠️Disclaimer !
This tool is intended for ethical and educational use only.  
Do not use it for illegal activities. The author is not responsible for any misuse.  
This script is intended for educational purposes and authorized testing only.  
Unauthorized use of this script is illegal and unethical.  
Ensure you have explicit permission before testing any system.  
- Obtain explicit permission before testing any system.  
- Adhere to all applicable laws and regulations.  
- Respect user privacy and data.  
- By using this script, you agree to take full responsibility for your actions.  
