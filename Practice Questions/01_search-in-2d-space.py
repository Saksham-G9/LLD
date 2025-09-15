def searchMatrix(mat: [[int]], target: int) -> bool:
    # Write your code here.
    for row in mat:
        if row[0] <= target <= row[-1]:
            start, end = 0, len(row) - 1

            while start <= end:
                mid = (start + end) // 2

                if row[mid] == target:
                    return True

                elif row[mid] > target:
                    end = mid - 1

                else:
                    start = mid + 1

            return False

    return False


def rotateMatrix(mat, n, m):
    s_rowI, s_colI = 0, 0
    e_rowI, e_colI = n - 1, m - 1
    temp = mat[s_rowI][s_colI]

    # top
    for i in range(s_colI + 1, n):
        mat[s_rowI][i], temp = temp, mat[s_rowI][i]

    s_rowI += 1
    
    # right
    for i in range(s_rowI, m):
        mat[i][e_colI], temp = temp, mat[i][e_colI]

    print(mat)

mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
target = 8

print(rotateMatrix(mat, len(mat[0]), len(mat)))
