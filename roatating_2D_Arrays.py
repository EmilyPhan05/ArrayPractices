arr1 = [1, 2, 3]
arr2 = [8, "*", 4]
arr3 = [7, 6, 5]

arr2D = [arr1, arr2, arr3]

print(arr1)
print(arr2)
print(arr3)
print()

#groups the values into separate arrays
xMoveTop = []
yMoveRight = []
xMove = []
yMove = []
for x in range(len(arr2D)):
    for y in range(len(arr2D[x])):
        if x == 1 and y == 1:
            next
        elif x == 0 and y < 2:
            xMoveTop.append(arr2D[x][y])
        elif x != 2 and y == 2:
            yMoveRight.append(arr2D[x][y])
        elif x == 2 and y != 0:
            xMove.append(arr2D[x][y])
        else:
            yMove.append(arr2D[x][y])

#moves the values
for x in range(len(arr2D)):
    for y in range(len(arr2D[x])):
        if x == 1 and y == 1:
            next
        elif x == 0 and y != 0:
            arr2D[x][y] = xMoveTop[0]
            xMoveTop.pop(0)
        elif x != 0 and y == 2:
            arr2D[x][y] = yMoveRight[0]
            yMoveRight.pop(0)
        elif x == 2 and y != 2:
            arr2D[x][y] = xMove[0]
            xMove.pop(0)
        else:
            arr2D[x][y] = yMove[0]
            yMove.pop(0)

print(arr2D[0])
print(arr2D[1])
print(arr2D[2])