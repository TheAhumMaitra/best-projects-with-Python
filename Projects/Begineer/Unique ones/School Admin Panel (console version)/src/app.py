# School Admin Panel - Console version
from dotenv import load_dotenv #load dot env module
import os #import os module

def welcome():
    global user_name
    user_name = input("Enter your name: ")
    print(f"Hello {user_name}, enter required details for next steps!")

def verify():
    global verified
    verified = False
    school_name = input("Enter your school name:\n> ")

    load_dotenv()  # Load environment variables

    # Token mapping
    tokens = {
        "ABC ELEMENTARY SCHOOL": os.getenv('TOKEN_ABC_ELEMENTRY_SCHOOL'),
        "XYZ HIGH SCHOOL": os.getenv('TOKEN_XYZ_HIGH_SCHOOL')
    }

    if school_name not in tokens or tokens[school_name] is None:
        print("School not recognized or token not set in .env.")
        exit()

    token_input = input(f"Enter your secret token for {school_name}:\n> ")

    if token_input == tokens[school_name]:
        print("✅ Verification successful! Access granted.")
        verified = True
        if verified == True :
            print("SYSTEM LOADED ....... VERIFIED IS TRUE AND ALL IS GOOD")
            global school_name_verified
            school_name_verified = token_input
        else:
            exit()
    else:
        print("❌ Invalid token. Access denied.")
        exit()

def view_students_XYZ_HIGH_SCHOOL():
    ask_class_input = False
    ask_class = int(input("Enter class : \n Ex : 1 \n>"))
    ask_class_input = True
    if ask_class_input == True:
        ask_class_input = False
        ask_section = input(f"Enter section of {ask_class} \n Ex : A or B or C or D \n>")
        ask_section_input = True

    if ask_class_input == True and ask_section_input == True:
        if ask_class_input == 1 and ask_section_input == 'A':

            print("Here's the names:")
            global students_7_A
            students_7_A = ["Harry Potter","Hong Hae In" , "Henry Willims" , "Baek Hyun Ho" , "Hermoine Granger" , "Bart Simpson" , "Taro Sakamoto" , "Shinnouske Nohara" , "Anya Fodger" , "Light Yagami" "Youchi Nagumo" , "Do do he" , 'Woo Young Woo']
            print(f"Students of class 7 - A - \n{students_7_A}\nTotal students - {len(students_7_A)}\nEND\nThanks")

def main_XYZ_HIGH_SCHOOL() :

    print(f"Hello {user_name} , welcome to the system....A SYTEM THAT IS EASY BUT EFFICIENT")
    options = ("View Students" , "Add student" , "Suspend student")
    print(f"\n***************System**************\n{options[0]} - index is 0\n{options[1]} - index is 1 \n{options[2]} - index is 2")
    print(f"Enter the index of the option to get the edit panel")
    ask_option = input("\nEnter your option index : \n> ")

    if ask_option == 0 :
        return view_students_XYZ_HIGH_SCHOOL()
# Call functions
welcome()
verify()
if school_name_verified == "XYZ HIGH SCHOOL" and verified == True :
    print(main_XYZ_HIGH_SCHOOL)
