def main():
    works = []

    while True:
        print("\n===== To-Do List Manager=====")
        print("1. Add Tasks to be done")
        print("2. Show Tasks in my list")
        print("3. Mark Task as completed")
        print("4. Quit")

        opt= input("Enter your choice: ")

        if opt == '1':
            print()
            n_works = int(input("How many task you need to add your list: "))
            
            for i in range(n_works):
                task = input("Enter the task: ")
                works.append({"task": task, "done": False})
                print("Task added!")

        elif opt == '2':
            print("\nWorks:")
            for index, task in enumerate(works):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif opt == '3':
            work_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= work_index < len(works):
                works[work_index]["done"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

        elif opt == '4':
            print("Quitting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()