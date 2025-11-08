from collections import defaultdict

t = int(input())  # Read number of test cases (3)

for _ in range(t):
    n,k = map(int, input().split())  # Read array size (4, 5, 5)
    arr = list(map(int, input().split()))  # Read the array
    
    # Your solution here

    d = defaultdict(int)
    k_vals = 0

    for i in arr:
        if i==k:
            k_vals+=1

        else:
            d[i]+=1


    to_replace=0
    for i in range(k):
        if i not in d:
            to_replace+=1

    # print(to_replace,k_vals,d)

    if k_vals==0:
        print(to_replace)
        continue 

    print(to_replace+k_vals)
