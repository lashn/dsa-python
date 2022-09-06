import math

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())

    A = []
    for i in range(N):
        A.append(int(input()))

    for i in range(N):
        c = []
        for j in range(1,math.ceil(A[i]/2)):
            if A[i] % j == 0:
                c.append(j)
        print(c)
        if A[i] == sum(c):
            print("YES")
        else:
            print("NO")


    return 0


if __name__ == '__main__':
    main()