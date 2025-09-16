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