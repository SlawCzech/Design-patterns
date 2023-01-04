from builder.before_builder_three.my_computer import MyComputer

builder = MyComputer()
builder.build_computer()

comp = builder.get_computer()
comp.display()
