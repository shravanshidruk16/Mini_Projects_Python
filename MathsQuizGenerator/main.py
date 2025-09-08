import time
from ProblemGenerator import generate_problem

OPERATOR = ["+", "-", "*", "/"]

def difficultyLevel():
    n = int(input("Enter the difficulty level (1-easy , 2-medium , 3-hard): "))
    
    if n == 1:  # easy
        return 1, 9, 10
    elif n == 2:  # medium
        return 1, 99, 60
    elif n == 3:  # hard
        return 1, 999, 120
    else:
        print("Invalid choice, setting game to easy mode.")
        return 1, 9, 10

# declare them globally
MIN_OPERAND, MAX_OPERAND, TIME_CONSTRAINED = difficultyLevel()    


def start_quiz(n):
    wrong = 0
    for i in range(n):
        exp, ans = generate_problem(MIN_OPERAND, MAX_OPERAND, OPERATOR)
        while True:
            guess = input("Problem #" + str(i + 1) + " : " + exp + " = ")
            if guess == str(ans):
                break
            wrong += 1
    print(f"Practice quiz completed. Wrong attempts: {wrong}")


def start_actual_quiz(n):
    wrong = 0
    if TIME_CONSTRAINED == 10:
        print("You need to answer these questions in 10 SECONDS and Your time starts NOW!!!")
    elif TIME_CONSTRAINED == 60:
        print("You need to answer these questions in 60 SECONDS and Your time starts NOW!!!")
    else:
        print("You need to answer the questions in 120 SECONDS and Your time starts NOW!!!")
    
    start_time = time.time()
    for i in range(n):
        exp, ans = generate_problem(MIN_OPERAND, MAX_OPERAND, OPERATOR)
        while True:
            guess = input("Problem #" + str(i + 1) + " : " + exp + " = ")
            if guess == str(ans):
                break
            wrong += 1
    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    print(f"The total time taken by the candidate is {total_time} seconds i.e {(total_time)/60:.2f} minutes")
    correct = n - wrong
    if total_time > TIME_CONSTRAINED:
        print("You failed")
        print(f"Correct Answers : {correct}")
        print(f"Wrong Answers: {wrong}")
    else:
        print("Congratulations You Won! ")
        print(f"Correct Answers : {correct}")
        print(f"Wrong Answers: {wrong}")


def main():
    global MIN_OPERAND, MAX_OPERAND, TIME_CONSTRAINED
    
    while True:
        print("***************************************")
        print("\t\tMain Menu\n")
        print("***************************************")
        print("1.Start the Practice Quiz (NO TIME CONSTRAINT)")
        print("2.Change the difficulty level")
        print("3.Start actual Quiz (Time-Bound)")
        print("4.Exit")
        choice = int(input("Enter the choice : "))
        if choice == 1:
            total_problems = int(input("Enter the total number of problems you wish to solve: "))
            start_quiz(total_problems)
        elif choice == 2:
            print("\t\tDifficulty Menu\n") 
            MIN_OPERAND, MAX_OPERAND, TIME_CONSTRAINED = difficultyLevel()
        elif choice == 3:
            total_problems = int(input("Enter the total number of problems you wish to solve: "))
            start_actual_quiz(total_problems)
        elif choice == 4:
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Wrong choice entered (please enter 1,2,3,4): ")


if __name__ == "__main__":
    main()
