def fun_pemanis(func):
    def fun_dalam():
        print("Saya sudah dipermanis")
        func()
    return fun_dalam


def asli():
    print("Saya masih orisinil")


# asli()
# manis = fun_pemanis(asli)
# manis()
