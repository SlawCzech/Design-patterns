from builder.before_builder_four.my_computer import MyComputerBuilder

builder = MyComputerBuilder()
builder.build_computer()

comp = builder.get_computer()
comp.display()
