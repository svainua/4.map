# π¨ Don't change the code below π
row1 = ["β¬οΈ", "β¬οΈ", "β¬οΈ"]
row2 = ["β¬οΈ", "β¬οΈ", "β¬οΈ"]
row3 = ["β¬οΈ", "β¬οΈ", "β¬οΈ"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# π¨ Don't change the code above π

# Write your code below this row π

positionX = int(position)

if positionX == 11:
    row1[0] = "X"
elif positionX == 21:
    row1[1] = "X"
elif positionX == 31:
    row1[2] = "X"
elif positionX == 12:
    row2[0] = "X"
elif positionX == 22:
    row2[1] = "X"
elif positionX == 32:
    row2[2] = "X"
elif positionX == 13:
    row3[0] = "X"
elif positionX == 23:
    row3[1] = "X"
elif positionX == 33:
    row3[2] = "X"

# Write your code above this row π

# π¨ Don't change the code below π
print(f"{row1}\n{row2}\n{row3}")

ΠΠ»ΠΈ

ΠΠΠ

