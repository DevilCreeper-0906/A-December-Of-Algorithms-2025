target = int(input("Enter target position: "))
n = int(input("Enter number of turtles: "))

if n == 0:
    print("No turtle fleets formed.")
else:
    position = list(map(int, input("Enter starting positions: ").split()))
    speed = list(map(int, input("Enter speeds: ").split()))

    turtles = list(zip(position, speed))
    turtles.sort(reverse=True)

    stack = []

    for pos, spd in turtles:
        time = (target - pos) / spd
        if not stack or time > stack[-1]:
            stack.append(time)

    print("The number of turtle fleets is:", len(stack))
