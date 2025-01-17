import os
import zipfile

def show_banner():
    """Displays the script's banner."""
    banner = r"""
                       ______
                    .-"      "-.
                   /  *ViRuS*   \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(_0_/\_0_)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
 ____________________________________________________
 ----------------------------------------------------        
        #  Zip Password Cracker
        #  Author : The-Real-Virus
        #  https://github.com/The-Real-Virus
 ____________________________________________________
 ----------------------------------------------------
"""
    print(banner)

def extract_file(zfile, password):
    """Attempts to extract the ZIP file with the given password."""
    try:
        zfile.extractall(pwd=password.encode('utf-8'))
        return password
    except (RuntimeError, zipfile.BadZipFile):
        return None  # Incorrect password or bad ZIP file

def main():
    """Main function to run the ZIP password cracker."""
    show_banner()

    # Prompt user for continuation
    choice = input("\nPress 'y' to continue or 'n' to exit: ").strip().lower()
    if choice == 'n':
        print("\nExiting the script. Goodbye!")
        return
    elif choice == 'y':
        os.system('clear' if os.name == 'posix' else 'cls')  # Clear the console screen
        print("Welcome to the ZIP Password Cracker!")
    else:
        print("\nInvalid choice. Exiting the script.")
        return

    # Get user inputs for ZIP file and password file
    zip_file_name = input("Enter the name of the ZIP file (with extension): ").strip()
    password_file_name = input("Enter the name of the password list file (with extension): ").strip()

    try:
        # Open the ZIP file
        zfile = zipfile.ZipFile(zip_file_name)
        print(f"\nOpened ZIP file: {zip_file_name}")

        # Open the password file
        with open(password_file_name, 'r', encoding='utf-8', errors='ignore') as passfile:
            print("Reading password file...")

            for line_number, line in enumerate(passfile):
                password = line.strip()  # Remove whitespace and newline characters
                print(f"Trying password {line_number + 1}: {password}", end='\r')

                guess = extract_file(zfile, password)
                if guess:
                    print(f"\nSuccess! Password found: {password}")
                    return  # Exit the program after finding the password

        print("\nPassword not found in the provided list.")

    except FileNotFoundError:
        print("Error: One of the specified files does not exist.")
    except zipfile.BadZipFile:
        print("Error: The ZIP file is invalid or corrupted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
