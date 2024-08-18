my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

row = 0
while row < len(my_list):
    col = 0
    while col < len(my_list[row]):
        if my_list[row][col] % 2 == 0:
            print(my_list[row][col])
        col += 1
    row += 1
