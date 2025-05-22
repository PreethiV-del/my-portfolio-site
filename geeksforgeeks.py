def transpose(mat):
  
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

if __name__ == '__main__':
    mat = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    res = transpose(mat)

    print("Result matrix is:")
    for row in res:
        print(" ".join(map(str, row)))