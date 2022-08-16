t = int(input())
np = [[int(input()), input()] for _ in range(t)]

for i in range(t):
    text = ""
    for j in range(len(np[i][1])):
        if np[i][1][j] == "E":
            text += "S"
        else:
            text += "E"
    print("Case #" + str(i + 1) + ": " + text)
