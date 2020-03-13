def fact(n) :
	if n <= 1 : return 1
	return n * fact(n - 1)

def fact_digits(n):
    sum = 0

    while n:
        sum += fact(n % 10)
        n //= 10
    
    return sum

def main():
    print(fact_digits(111))
    # Expected output : 3

    print(fact_digits(145))
    # Expected output : 145

    print(fact_digits(999))
    # Expected output : 1088640

if __name__ == '__main__':
    main()