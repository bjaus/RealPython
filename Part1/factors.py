def factor(num):
    try:
        num = int(num)
    except ValueError:
        print('Please enter a number')
    else:
        for n in range(1,num):
            if num % n == 0:
                print("\n{} is a divisor of {}".format(n, num))

def main():
    user_num = input("\nEnter a positive integer: ")
    factor(user_num)

if __name__ == '__main__':
    main()


