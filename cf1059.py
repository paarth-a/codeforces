import sys

def mainA():
    t = int(input())  # Read number of test cases (3)

    for _ in range(t):
        n = int(input())  # Read array size (4, 5, 5)
        arr = list(map(int, input().split()))  # Read the array
        
        # Your solution here
        print(max(arr))


def mainB():
    t = int(input())  # Read number of test cases (3)

    for _ in range(t):
        n = int(input())  # Read array size (4, 5, 5)
        arr = list(map(int, input().split()))  # Read the array
        
        # Your solution here
        if arr==arr[::-1]:
            print(0)

            return





    






if __name__ == "__main__":
    mainA()