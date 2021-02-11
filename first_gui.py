picture = [[0, 0, 0, 1, 0, 0, 0],
           [0, 0, 1, 1, 1, 0, 0],
           [0, 1, 1, 1, 1, 1, 0],
           [1, 1, 1, 1, 1, 1, 1],
           [0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0]]


for row in picture:
    display = ''
    for pixel in row:
        if pixel == 0:
            display += ' '
        else:
            display += '*'
    print(display)
