#Tuple
rows = int(input("Enter row: "))
cols = int(input("Enter column: "))
tup = []
for x in range(rows):
    print(f"row {x+1}")
    tuple_list = []
    for y in range(cols):
        print(f"Enter score {y+1}: ")
        score = float(input())
        tuple_list.append(score)
    tup.append(tuple(tuple_list))
tup = tuple(tup)
for r in range(rows):
    for c in range(cols):
        print(tup[r][c], end=" ")
    print()
print("Search: ")
search_tup = float(input())
for n in range(rows):
    for m in range(cols):
        if tup[n][m] == search_tup:
            print(f"Number {search_tup} found at row {n+1}, column {m+1}")