matrix = [[66, 2, 82, 65, 71], [27, 70, 96, 64, 53], [33, 27, 90, 35, 34], [96, 60, 17, 71, 32], [5, 58, 36, 45, 76]]
ele = ''
#iterate over and print out every element in this matrix
ans = "false"
x = 53
for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == x:
            ans = 'True'
print(ans)
