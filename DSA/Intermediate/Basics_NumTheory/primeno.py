def main():
    num = int(input())


    # brute force
    if num<1:
        print(False)
    prime = True
    i = 2
    while (i <= num/2):
        if num % i == 0:
            prime = False
            break
        i += 1
    print(prime)


if __name__ == '__main__':
    main()