#!/usr/bin/python3
for i in range (10):
    for j in range (10):
        if i >= j:
            continue
        else:
            print(f"{i}{j}", end="")
            if i != 8:
                print(", ", end="")
print()

