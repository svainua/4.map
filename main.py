# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

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

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

Или

ИЛИ

