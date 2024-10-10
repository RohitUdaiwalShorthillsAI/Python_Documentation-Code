def main():
    try:
        a = int(input("Hey, Enter a number : "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("Hey I am inside of finally")

main()

# Python offers a 'finally' clause which ensures execution of a piece of code inspective of the exception.