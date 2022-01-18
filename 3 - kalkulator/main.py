from Calculator import Calculator
import CalculatorCommand as cmd


def main(args=None):
    """
    This calculator implements the Command, Memento, and Builder pattern
    for better extensibility and maintainability.
    """
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
        print("Undo: ", calc)

    # Builder pattern
    print("\nExecute multiple commands at once: ")
    print("Add 10, substract 15, multiply by 4, divide by 3: ")
    calc.execute(cmd.AddCommand(10)).execute(cmd.SubstractCommand(15)).execute(
        cmd.MultiplicationCommand(4)).execute(cmd.DividerCommand(3))
    print(calc)


if __name__ == '__main__':
    main()
