import random
import string

def generate_password(length): # taking the user input for length to generate the passcode
    characters = string.ascii_letters + string.digits + string.punctuation # performing concatination
    password = ''.join(random.choice(characters) for _ in range(length)) #random password generation
    return password #returning passcode

def main():
    try:
        password_length = int(input("Enter the desired length of the password: ")) #asking user prompt
        if password_length <= 0: #must be a positive number for length of passcode
            print("Password length must be a positive integer.")
        else:
            generated_password = generate_password(password_length)
            print("Generated Password: ", generated_password) #password generated printed
    except ValueError:
        print("Invalid input. Please enter a valid positive integer for password length.") #else case

if __name__ == "__main__":
    main()
