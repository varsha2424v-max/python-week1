def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def check_prime(num):
    if num <= 1:
        return "Not Prime"
    
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            return "Not Prime"
        
    return "Prime"

def main():
    num = int(input("Enter a number: "))

    print("Number is", check_even_odd(num))
    print("Number is", check_prime(num))

main()