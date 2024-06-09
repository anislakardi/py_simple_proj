num = ((1, 2, 3),
       (4, 5, 6),
       (7, 8, 9),
       ("*", 0, "#"))

for x in num:
    i = 0
    for i in x:
        print(i , end=" ")
    print()