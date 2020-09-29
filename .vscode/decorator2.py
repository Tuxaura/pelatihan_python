def pembagi(func):
    def fun_internal(a, b):
        print("Saya akan membagi", a, "dan", b)
        if b == 0:
            print("Duh tidak bisa dibagi")
            return

        return func(a, b)
    return fun_internal


@pembagi
def bagi(a, b):
    print(a/b)


bagi(2, 5)
bagi(2, 0)
