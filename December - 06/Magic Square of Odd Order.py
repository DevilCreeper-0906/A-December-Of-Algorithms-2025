n = int(input("Enter the value of n (order of the magic square): "))

if n % 2 == 0:
    print("Magic square is only possible for odd values of n.")
else:
    square = [[0 for j in range(n)] for i in range(n)]

    row = 0
    column = n // 2
    num = 1

    while num <= n * n:
        square[row][column] = num
        num = num + 1

        new_row = row - 1
        new_col = column + 1

        if new_row < 0:
            new_row = n - 1
        if new_col == n:
            new_col = 0

        if square[new_row][new_col] != 0:
            row = row + 1
        else:
            row = new_row
            column = new_col

    result = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = (n*n + 1) - square[j][i]

    M = n * (n**2 + 1) // 2
    print("Magic constant:", M)

    for i in range(n):
        for j in range(n):
            print(result[i][j], end=" ")
        print()
