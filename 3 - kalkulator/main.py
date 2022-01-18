from Calculator import Calculator
import CalculatorCommand as cmd


def main(args=None):
    """
    This calculator implements the Command, Memento, and Builder pattern
    for better extensibility and maintainability.
    """
    print_demo()
    print("\n")
    get_user_command()


def print_demo():
    print("==========================================================")
    print("Calculator Demo")
    print("==========================================================")
    # value to start with
    calc = Calculator(10)
    print("Initial Value: ")
    print(calc)
    print()

    # add 5
    calc.execute(cmd.AddCommand(5))
    print("Add by 5: ", calc)

    # substract 2
    calc.execute(cmd.SubstractCommand(2))
    print("Subtract by 2: ", calc)

    # multiply by 3
    calc.execute(cmd.MultiplicationCommand(3))
    print("Multiply by 3: ", calc)

    # divide by 2
    calc.execute(cmd.DividerCommand(2))
    print("Divide by 2: ", calc)

    # print history
    print("\nCommand History:")
    calc.print_history()

    # Memento Pattern
    print("\nUndo Operations: ")
    for _ in range(4):
        calc.undo()
        print("Undo.")
        print("Current value: ", calc)

    # Builder pattern
    print("\nExecute multiple commands at once: ")
    print("Add 10, substract 15, multiply by 4, divide by 3: ")
    calc.execute(cmd.AddCommand(10)).execute(cmd.SubstractCommand(15)).execute(
        cmd.MultiplicationCommand(4)).execute(cmd.DividerCommand(3))
    print("Current value: ", calc)


def get_user_command():
    print("==========================================================")
    print("Calculator Program")
    print("==========================================================")
    calc = Calculator(int(input("Enter initial value: ")))

    while True:
        print("\nCurrent value: ", calc)
        print("1. Add\n2. Substract\n3. Multiply\n4. Divide\n5. Undo\n6. Print History\n7. Exit")
        input_cmd = input("Enter command: ")
        if input_cmd.isdigit() and int(input_cmd) in range(1, 5):
            input_value = int(input("Enter number: "))
        print()
        if input_cmd == "1":
            calc.execute(cmd.AddCommand(input_value))
        elif input_cmd == "2":
            calc.execute(cmd.SubstractCommand(input_value))
        elif input_cmd == "3":
            calc.execute(cmd.MultiplicationCommand(input_value))
        elif input_cmd == "4":
            calc.execute(cmd.DividerCommand(input_value))
        elif input_cmd == "5":
            calc.undo()
        elif input_cmd == "6":
            calc.print_history()
        elif input_cmd == "7":
            break


if __name__ == '__main__':
    main()
