import sys
import random, string

def solve(filename):
    with open(filename, "r") as file:
        k = int(file.readline().strip())
        inv = {}
        for x in range(k):
            output = file.readline().strip().split(" ")
            inv[output[0]] = int(output[1])
        a = file.readline().strip()
        b = file.readline().strip()

    print(f"k: {k}")
    print(f"inv: {inv}")
    print(f"a: {a}")
    print(f"b: {b}")

if __name__ == "__main__":
    solve(sys.argv[1])

