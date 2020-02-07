'''
Name: Arrange Seat
Author: Tena Walcott
Email: tenawalcott@gmail.com
'''
a = []
with open("name.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        line = line.strip("\n")
        a.append(line)
b = []
with open("random_list.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    while line:
        b.append(line)
        line = f.readline()
c = {}
for i in range(1, len(a)):
    c[a[i]] = -1
boundary = [4, 9, 13, 18, 23]
for i in range(1, len(a)):
    if c[a[i]] == -1:
        c[a[i]] = int(b[i - 1])

# If A and B want to seat next to each other:
# if (a[i] == "A") & (int(b[i - 1]) % 3 != 0) & (int(b[i - 1]) != 28):
#	c["B"] = int(b[i - 1]) + 1

c = sorted(c.items(), key=lambda x: x[1])
print(" " * 7, end="")
print(c[0][0], end=" ")
print(c[1][0], end=" ")
print(c[2][0], end=" ")
print(c[3][0], end=" ")
print("\n")
for i in range(4, int(a[0]), 5):
    for j in range(0, 5):
        if (i + j != 28):
            print(c[i + j][0], end=" ")
    print("\n")
with open("seat.txt", "w", encoding="utf-8") as f:
    f.write(" " * 7)
    f.write(str(c[0][0]) + " ")
    f.write(str(c[1][0]) + " ")
    f.write(str(c[2][0]) + " ")
    f.write(str(c[3][0]) + " ")
    f.write("\n")
    for i in range(4, int(a[0]), 5):
        for j in range(0, 5):
            if (i + j != 28):
                f.write(str(c[i + j][0]) + " ")
        f.write("\n")
input()
