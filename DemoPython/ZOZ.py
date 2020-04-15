t = int(input("Enter the number of testcases"))

for i in range(t):
    N, K = [int(x) for x in input().split()]
    lst = [int(x) for x in input().split()]
    # eval(input("Enter the Array size"))
    # K = eval(input("Enter the Additional number"))
    sumList = sum(lst)
    result = 0
    # for j in range(N):
    #     val = int(input())
    #     lst.append(val)
    #     sum = sum + val
    for m in range(len(lst)):
        if (lst[m] + K) > (sumList - lst[m]):
            result = result + 1

    print(result)
