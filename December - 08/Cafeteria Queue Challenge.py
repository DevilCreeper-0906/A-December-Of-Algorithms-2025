students = list(map(int, input("Enter student preferences (0/1) separated by space: ").split()))
sandwiches = list(map(int, input("Enter sandwich stack (0/1) separated by space: ").split()))

count0 = students.count(0)
count1 = students.count(1)

for s in sandwiches:
    if s == 0 and count0 > 0:
        count0 -= 1
    elif s == 1 and count1 > 0:
        count1 -= 1
    else:
        break

unable_to_eat = count0 + count1
print("Number of students unable to eat:", unable_to_eat)
