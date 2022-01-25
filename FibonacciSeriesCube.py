# apply the map function and a lambda expression to cube each fibonacci number and print the list.
cube = lambda x: x * x * x


def fibonacci(num):
    n1, n2 = 0, 1
    add = 0
    for i in range(0, num):
        # cubic.append(cube(n1))
        yield n1
        add = n1 + n2
        n1, n2 = n2, add


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
