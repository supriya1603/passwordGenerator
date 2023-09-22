import string
import random
def generate_password(length,use_special_charts=False):
    characters = string.ascii_letters + string.digits
    if use_special_charts:
        characters +=string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("password Genertrator")
    try:
        length=int(input("Enter your password length:"))
        use_special_charts=input("Include character?y/n").lower()=='y'
        if length<=0:
            print("password length should be positive number.")
        else:
            password= generate_password(length,use_special_charts)
            print("Your Generated_Password=",password)
    except:
        print("Invalid Input")


if __name__ == "__main__":
    main()
