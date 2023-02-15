def get_last_element(list):
    try:
        last = list[len(list)]
    except IndexError:
        last = list[-1]

    return last


def sqrt(n):
    if type(n) is str:
        raise TypeError("Cannot send a String to sqrt function")
    if n < 0:
        raise ValueError("Cannot send a negative value to sqrt function")

    x = n
    y = 1
    e = 0.0000001
    while(x-y > e):
        x = (x+y)/2
        y = n/x

    return x


def main(list, number):
    print(get_last_element(list))
    print(sqrt(number))


if __name__ == "__main__":
    main([1, 2, 3, 4, 5], 5)
