def outerFunction(text):
    print(text)
    def innerFunction():
        print(" World")

    innerFunction()

outerFunction("Hellow")
