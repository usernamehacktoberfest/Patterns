Height = eval(input("Enter diamond's Hegight: "))

for x in range(Height):
    print(" " * (Height - x), "*" * (2*x + 1))
for x in range(Height - 2, -1, -1):
    print(" " * (Height - x), "*" * (2*x + 1))
