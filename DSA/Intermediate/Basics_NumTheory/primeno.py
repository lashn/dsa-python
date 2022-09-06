def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = int(input())
    prime = "YES"
    i = 2
    while (i < A):
        if A % i == 0:
            prime = "NO"
        i += 1
    print(prime)


if __name__ == '__main__':
    main()