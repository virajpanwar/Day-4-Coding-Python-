#treasure map
row1=["⬜","⬜","⬜"]
row2=["⬜","⬜","⬜"]
row3=["⬜","⬜","⬜"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("Where do you want to put the treasure? ")
hor=position[0]
ver=position[1]
map[int(ver)-1][int(hor)-1]="X"
print(f"{row1}\n{row2}\n{row3}")
