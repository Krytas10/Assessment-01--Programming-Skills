# Ex 10 ( Is it even )

def even_odd(number):
    if number % 2 == 0:
        return f"THE Number is even."
    else: 
        return f"The number is odd."

def main():

    entered_value = input("Enter a number: ")
    try:  
        number = int(entered_value)
    except ValueError:
        return
    
    result = even_odd(number)
    print(result)

if __name__ == "__main__":
    main()

