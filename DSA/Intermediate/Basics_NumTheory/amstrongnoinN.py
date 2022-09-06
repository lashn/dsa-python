def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())

    c = 1
    while (c < N):
        n = []
        temp=c
        while (temp > 0):
            n.append(temp % 10) #remainder
            temp = temp // 10 #quotient

        sum = 0
        for i in n:
            sum += i ** 3

        if sum == c:
            print(c)
        c += 1

    return 0


if __name__ == '__main__':
    main()