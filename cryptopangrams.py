t = int(input())
inputs = [[input().split(" "), input().split(" ")] for _ in range(t)]

my_values = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
             "V", "W", "X", "Y", "Z"]


def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)


for i in range(t):
    length = int(inputs[i][0][1])
    products = list(map(int, inputs[i][1]))

    numbers = []
    count = 0
    while True:
        if products[count] != products[count + 1]:
            numbers.append(hcf(products[count], products[count + 1]))
            break
        count += 1

    [numbers.insert(0, products[count - j] // numbers[0]) for j in range(count + 1)]
    [numbers.append(products[j] // numbers[len(numbers) - 1]) for j in range(count + 1, length)]

    my_keys = sorted(set(numbers))
    my_dict = dict(zip(my_keys, my_values))
    text = "".join([my_dict[j] for j in numbers])

    print("Case #" + str(i + 1) + ": " + text)
