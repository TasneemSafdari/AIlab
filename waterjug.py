#water jug problem

a = int(input("Enter capacity of Jug A: "))
b = int(input("Enter capacity of Jug B: "))
target = int(input("Enter target amount: "))

x = 0  #initially jug A is empty
y = 0  #jugB is empty
step = 0

while x != target and y != target:
    if y == 0:  #jug b is empty
        y = b
        action = "Fill Jug B"
    elif x + y >= a: #if both capacity is enough to fill jug A
        y = x + y - a
        x = a

        action = "Pour B into A"
    else:
        x = x + y
        y = 0
        action = "Pour B into A"


    step += 1
    print("Step", step, ":", action)
    print("Jug A =", x, "Jug B =", y)

print("Target reached!")
