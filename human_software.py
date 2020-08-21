import pyttsx3
import os
pyttsx3.speak("Welcome to my tools:")
# software_list = ["notepad", "firefox", "calc", "chrome", "exit"]
# firefox,ping,calc,exit
with open('software_lists.txt', 'w+') as f:
    isEmpty = f.read().strip()
    if isEmpty == "":
        previous = "firefox,ping,calc,exit"
        software_list = list(previous.split(","))
        f.write(previous)
    # print(software_list)

while True:
    print("------------------------------------------------------------------------")
    print("\t\t\t\tMENU\t\t\t\t")
    print("1. To ask query.\n2. Hint.\n3. Modify Software List.\n4. Exit.")
    print("------------------------------------------------------------------------")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        pyttsx3.speak(
            "What task should we do for you please mention in the query..")
        query = input("What should we do: ")
        software = ""
        software = "".join(
            [element for element in software_list if element in query.lower()])

        if (("open" in query.lower() or "run" in query.lower() or "execute" in query.lower()) and (software != "")):
            os.system(software)
        elif("close" in query.lower() or "exit" in query.lower() or "kill" in query.lower() or "quit" in query.lower()):
            pyttsx3.speak(
                "I hope whatever task you won't to perform is completed, Bye.")
            print("\nBye")
            exit(0)
        else:
            print("\nThe item you are looking for does not exist")

    elif ch == 2:
        pyttsx3.speak(
            "We provide you a hint section if you don't like to use query just press the mention numbers.")
        while True:
            print("\t\t\t\tHINT\t\t\t\t")
            count = 1
            for element in software_list:
                print(str(count)+". "+element.capitalize())
                count += 1
            hint_ch = int(input("Enter your choice: "))

            if hint_ch > len(software_list):
                print("Invalid input")
            elif software_list[hint_ch - 1] == "exit":
                pyttsx3.speak(
                    "You are exited from hint section now you are in Menu section.")
                break
            else:
                os.system(software_list[hint_ch - 1])

    elif ch == 3:
        while True:
            print("\n\t\t\t\tCURRENT SOFTWARE LIST\t\t\t\t")
            count = 1
            for element in software_list:
                print(str(count)+". "+element.capitalize())
                count += 1
                if count == len(software_list):
                    break
            print("\n\t\t\t\tMODIFY SOFTWARE LIST\t\t\t\t")
            print("\n1. Insert\n2. Delete\n3. Exit")
            modify_list_ch = int(input("Enter your choice: "))

            if modify_list_ch == 1:
                insert = input("Enter new software: ")
                if insert in software_list:
                    print("\nSoftware already present.")
                else:
                    software_list.insert(len(software_list) - 1, insert)
                    pyttsx3.speak(
                        "Your new software is successfully inserted into the software list.")
                    print(insert+" is inserted successfully into the list")
                    with open('software_lists.txt', 'w+') as f:
                        f.write(previous+","+insert)
                    with open('software_lists.txt', 'r') as f:
                        previous = f.read().strip()
            elif modify_list_ch == 2:
                remove = int(
                    input("Enter numeric value of current software list: "))
                delete = software_list[remove-1]
                software_list.remove(delete)
                pyttsx3.speak(
                    "Your software is deleted successfully into the software list.")
                with open('software_lists.txt', 'w+') as f:
                    f.write(previous.replace(","+delete, ""))
                with open('software_lists.txt', 'r') as f:
                    previous = f.read().strip()
                print("Your software is deleted successfully from the list.")
                print("Your software is deleted successfully from the list.")
            elif modify_list_ch == 3:
                break
            else:
                print("Enter valid input")

    elif ch > 4:
        print("Please enter valid input...")
        pyttsx3.speak("Please provide valid input.")

    else:
        print("\nBye")
        pyttsx3.speak(
            "I hope whatever task you won't to perform is completed, Bye.")
        exit(0)
