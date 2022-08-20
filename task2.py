from audioop import mul


def multiply(num_a, num_b):
    if num_a < num_b:
        return multiply(num_b, num_a)
    if num_a == 0 or num_b == 0:
        print("Return 0")
        return 0
    print(str(num_a) + " + multiply(" + str(num_a) + ", " + str(num_b-1) + ")")
    return num_a + multiply(num_a, num_b - 1)


print(multiply(500, 2000))
