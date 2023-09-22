from Diary import Diary
from TaskList import TaskList
from DiaryEntry import DiaryEntry
from TaskUnit import TaskUnit

user1 = Diary()
menu = "MENU:\n* DIARY PAGE [D]\n* TODOS PAGE [T]\n* CONTACTS PAGE [C]\n* EXIT [EXIT]\n"
print("WELCOME IN YOUR DIARY!")

while True:
    print("\n=============== MAIN PAGE =============== ")
    menu_choice = input(f"{menu}Command: ")
    match menu_choice:
        case "D":
            print("\n=============== DAIRY PAGE =============== ")
            choice_diary = input("MENU:\n* VIEW DIARY [V]\n* ADD NEW ENTRY [A]\n* READ ENTRY [R]\n* EXIT TO MAIN PAGE [X]\n")
            if choice_diary == "V":
                print("\n*********** MY DAIRY ***********\n")
                print(user1.view_diary())

            if choice_diary == "A":
                choice_title = input("Title: ")
                choice_contents = input("Contents: ")
                new_entry = DiaryEntry(choice_title, choice_contents)
                user1.add_entry(new_entry)

            if choice_diary == "R":
                choice_wpm = input("Whats your reading speed (words per minute): ")
                choice_time = input("How much time do you have: ")
                new_entry = DiaryEntry(choice_wpm, choice_time)
                print(user1.view_entry_to_read(choice_wpm, choice_time))

            if choice_diary == "X":
                menu_choice = input(f"{menu}Command: ")

        case "T":
            print("\n=============== TODOs PAGE =============== ")
            # user can choos the view and add task
            choice_tasks = input("TASK PAGE MENU:\n[ALL] - all tasks\n[C] - completed tasks\n[I] - incompleted tasks\n[A] - add new task\n* EXIT TO MAIN PAGE [X]\n")
            if choice_tasks == "ALL":
                print(user1.view_tasks())

            if choice_tasks == "C":
                print(user1.Task_List.view_completed())

            if choice_tasks == "I":
                print(user1.Task_List.view_incompleted())
            
            if choice_tasks == "A":
                user1.add_task()

            if choice_tasks == "X":
                menu_choice = input(f"{menu}Command: ")
    
        case "C":
            print("\n=============== CONTACTS PAGE =============== ")
            choice_contacts = input("CONTACT PAGE MENU:\n[V] - view contacts\n* EXIT TO MAIN PAGE [X]\n")
            if choice_contacts == "V":
                print(user1.view_contacts())
            else:
               menu_choice = input(f"{menu}Command: ") 
        
        case "EXIT":
            break
        
