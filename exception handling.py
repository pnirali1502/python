def demo():
    try:
        print("Hello")
        print(10)
    except ZeroDivisionError:
        print("ZeroDivisionError")
        return 10
    finally:
        print("This Code will run")
        return 5
print(demo())
