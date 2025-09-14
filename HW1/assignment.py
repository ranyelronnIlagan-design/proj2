#List
# rows = int(input("Enter row: "))
# cols = int(input("Enter column: "))
# list = []
# for x in range(rows):
#     print(f"row {x+1}")
#     row_list= []
#     for y in range(cols):
#         print(f"Enter score {y+1}: ")
#         score = float(input())
#         row_list.append(score)
#     list.append(row_list)
# for x in range(len(list)):
#     for y in range(len(list[x])):
#         print(list[x][y], end=" ")
#     print()
# print("Search: ")
# search = float(input())
# for c in range(rows):
#     for n in range(cols):
#         if list [c][n] == search:
#             print(f"Number {search} found at row {c+1}, column {n+1}")
#Dictionary
rows = int(input("Enter row: "))
cols = int(input("Enter column: "))
dict = {}
for x in range(rows):
    print(f"\nRow {x+1}")
    for y in range(cols):
        num = float(input(f"Enter score {y+1}: "))
        dict[(x, y)] = num
for x in range(rows):
    for y in range(cols):
        print(dict[(x, y)], end=" ")
    print()
print("Search: ")
search_dict = float(input())
for c in range(rows):
    for n in range(cols):
        if dict [(c, n)] == search_dict:
            print(f"Number {search_dict} found at row {c+1}, column {n+1}")
#Tuple
# rows = int(input("Enter row: "))
# cols = int(input("Enter column: "))
# tup = []
# for x in range(rows):
#     print(f"row {x+1}")
#     tuple_list = []
#     for y in range(cols):
#         print(f"Enter score {y+1}: ")
#         score = float(input())
#         tuple_list.append(score)
#     tup.append(tuple(tuple_list))
# tup = tuple(tup)
# for r in range(rows):
#     for c in range(cols):
#         print(tup[r][c], end=" ")
#     print()
# print("Search: ")
# search_tup = float(input())
# for n in range(rows):
#     for m in range(cols):
#         if tup[n][m] == search_tup:
#             print(f"Number {search_tup} found at row {n+1}, column {m+1}")