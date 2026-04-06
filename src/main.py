import sys
import time

def load_file(filename):
    with open(f"output/{filename}", "r") as file:
        k = int(file.readline().strip())
        inv = {}
        for x in range(k):
            output = file.readline().strip().split(" ")
            inv[output[0]] = int(output[1])
        a = file.readline().strip()
        b = file.readline().strip()

    return [
        inv,
        a, 
        b 
    ]

def solve(filename):
    [inv, a, b] = load_file(filename)

    len_a = len(a)
    len_b = len(b)
    
    dp_table = [[0] * (len_b + 1) for _ in range(len_a + 1)]

    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            if a[i-1] == b[j-1]:
                dp_table[i][j] = dp_table[i-1][j-1] + inv[a[i-1]]
            else:
                dp_table[i][j] = max(dp_table[i-1][j], dp_table[i][j-1])

    result = ""
    i = len_a
    j = len_b
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            result = a[i-1] + result
            i -= 1
            j -= 1
        elif dp_table[i-1][j] >= dp_table[i][j-1]:
            i -= 1
        else:
            j -= 1
    print(dp_table[len_a][len_b])
    print(result)

if __name__ == "__main__":
    start = time.time()
    solve(sys.argv[1])
    elapsed = time.time() - start
    print(f"Time: {elapsed:.4f}s")
