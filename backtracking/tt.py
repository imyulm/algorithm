for i in range(5):
    for j in range(5):
        print(i, j)
        print((i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0))

        if i % 2 == 0 and j % 2 == 0:
            bishop1.append([i, j])
        elif i % 2 != 0 or j % 2 != 0:
            bishop2.append([i, j])