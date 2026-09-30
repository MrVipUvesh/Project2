print("Welcome to the Pattern Generator and Number Analyzer!")

while True:  
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if(choice == 1):
        rows = int(input("Enter the number of rows for the pattern: "))        
        for i in range(rows + 1):
            if(i == 1):
                print("Pattern:")
            for j in range(i):
                print("*", end = "")
            print()
    elif(choice == 2):
        start = int(input("\nEnter the start of the range: "))
        end = int(input("Enter the end of the range:"))
        sum = 0
        for i in range(start,end + 1):
            print(f"Number {i} is {"Even" if i % 2 == 0 else "Odd"}")
            sum += i
        print(f"Sum of all numbers from {start} to {end} is: {sum}")
    elif(choice == 3):
        print("Exiting the program. Goodbye!")
        break   
    else:
        print("Invalid Choice!")