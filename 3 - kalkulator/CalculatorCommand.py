from abc import ABC, abstractmethod


class CalculatorCommand(ABC):
    @abstractmethod
    def __init__(self, value: float):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def execute(self, calcValue: float) -> float:
        pass

    @abstractmethod
    def undo(self, calcValue: float) -> float:
        pass


class AddCommand(CalculatorCommand):
    def __init__(self, value: float):
        self.value = value

    def __str__(self) -> str:
        return f"AddCommand({self.value})"

    def execute(self, calcValue) -> float:
        return calcValue + self.value

    def undo(self, calcValue) -> float:
        return calcValue - self.value


class SubstractCommand(CalculatorCommand):
    def __init__(self, value: float):
        self.value = value

    def __str__(self) -> str:
        return f"SubstractCommand({self.value})"

    def execute(self, calcValue: float) -> float:
        return calcValue - self.value

    def undo(self, calcValue: float) -> float:
        return calcValue + self.value


class MultiplicationCommand(CalculatorCommand):
    def __init__(self, value: float):
        self.value = value

    def __str__(self) -> str:
        return f"MultiplicationCommand({self.value})"

    def execute(self, calcValue: float) -> float:
        return calcValue * self.value

    def undo(self, calcValue: float) -> float:
        return calcValue / self.value


class DividerCommand(CalculatorCommand):
    def __init__(self, value: float):
        self.value = value

    def __str__(self) -> str:
        return f"DividerCommand({self.value})"

    def execute(self, calcValue: float) -> float:
        return calcValue / self.value

    def undo(self, calcValue: float) -> float:
        return calcValue * self.value
