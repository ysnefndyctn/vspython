# from functions import get_todos,write_todos
import functions
import time
now = time.strftime("%b %d , %Y %H : %M : %S")
print("It is", now)
user_prompt = "Enter a To Do: "

while True:
    user_action = input("Type add ,show ,edit ,complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo+'\n')
        functions.write_todos(todos)
        """with open("todos.txt", "r")as file:
            todos = file.readlines()
        todos.append(todo+"\n")
        # todos.append("\n") todoları bitişik yazarsa diye,
        with open("todos.txt", "w") as file:
            file.writelines(todos)"""

    elif user_action.startswith("show"):
        """with open("todos.txt", "r")as file:
            todos = file.readlines()"""
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1} - {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = (input("Number of the todo to edit: "))
            number = int(number)
            print(number)
            number = number-1
            todos = functions.get_todos()
            """with open("todos.txt", "r")as file:
                todos = file.readlines()"""

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + "\n"
            functions.write_todos(todos)

            """with open("todos.txt", "w") as file:
                file.writelines(todos)"""
        except IndexError:
            print("Index that you are trying to edit is out of range!")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(input("Number of the todo to complete: "))
            todos = functions.get_todos()
            """with open("todos.txt", "r")as file:
                todos = file.readlines()"""
            index = number-1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            """with open("todos.txt", "w") as file:
                file.writelines(todos)"""
            functions.write_todos(todos)
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is item with that number.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid try to enter a valid command please!")
print(" bye bye ")
