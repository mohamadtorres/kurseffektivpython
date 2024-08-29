def ytre_func():
    x = 5
    def inre_func():
        nonlocal x
        x = 10
    print(x)
    inre_func()
    print(x)


ytre_func()