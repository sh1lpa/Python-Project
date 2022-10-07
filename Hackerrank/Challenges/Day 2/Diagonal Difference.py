import enum


def diagonalDifference(arr):
    primary = 0
    secondary = 0
    for i, val in enumerate(arr):
        for j, val in enumerate(arr):
            if i==j:
                primary = primary + arr[i][j]
                if (i+j) == len(arr)-1:
                    secondary = secondary+arr[i][j]
            elif (i + j) == len(arr)-1:
                secondary = secondary+arr[i][j]
    return abs(primary - secondary)


def main():
    arr = [[11, 2, 4],
            [4, 5, 6],
            [10, 8, -12]]

    print(diagonalDifference(arr))


if __name__ == '__main__':
    main()