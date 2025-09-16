#List
rows = int(input("Enter row: "))
cols = int(input("Enter column: "))
list = []
for x in range(rows):
    print(f"row {x+1}")
    row_list= []
    for y in range(cols):
        print(f"Enter score {y+1}: ")
        score = float(input())
        row_list.append(score)
    list.append(row_list)
for x in range(len(list)):
    for y in range(len(list[x])):
        print(list[x][y], end=" ")
    print()
print("Search: ")
search = float(input())
for c in range(rows):
    for n in range(cols):
        if list [c][n] == search:
            print(f"Number {search} found at row {c+1}, column {n+1}")