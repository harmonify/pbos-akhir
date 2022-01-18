from __future__ import annotations
from CalculatorCommand import CalculatorCommand


class Calculator:
    def __init__(self, value = 0) -> None:
        self.value: float = float(value)
        self.history: list[CalculatorCommand] = []

    def __str__(self) -> str:
        return str(self.value)

    def execute(self, command: CalculatorCommand) -> Calculator:
        self.value = command.execute(self.value)
        self.history.append(command)
        return self

    def undo(self) -> Calculator:
        if len(self.history) > 0:
            last_command = self.history.pop()
            self.value = last_command.undo(self.value)
        else:
            print("Nothing to undo.")
        return self

    def print_history(self):
        for index, item in enumerate(self.history):
            print(f"{index+1}. {item}")

    def clear_history(self):
        self.history = []
