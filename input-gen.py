import sys
import random, string

def generate(k, name):

    with open(name, "w") as file:
        file.write(f"{k}\n")
        inv = []
        inv_vals = []
        
        for x in range(k):
            new_char = random.choice(string.ascii_lowercase)
            while new_char in inv:
                new_char = random.choice(string.ascii_lowercase)
            inv.append(new_char)


            new_val = random.randint(0, 100)
            while new_val in inv_vals:
                new_val = random.randint(0, 100)
            inv_vals.append(new_val)

            file.write(f"{new_char} {new_val}\n")
        a = ''.join(random.sample(inv, k=len(inv)))
        b = ''.join(random.sample(inv, k=len(inv)))
        file.write(a)
        file.write('\n')
        file.write(b)

if __name__ == "__main__":
    generate(int(sys.argv[1]), sys.argv[2])
