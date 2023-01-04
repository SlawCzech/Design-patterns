from builder.builder.budget_computer_builder import BudgetBoxBuilder
from builder.builder.director import Director
from builder.builder.my_computer_builder import MyComputerBuilder

# computer_builder = Director(BudgetBoxBuilder())
computer_builder = Director(MyComputerBuilder())
computer_builder.build_computer()
computer = computer_builder.get_computer()

computer.display()