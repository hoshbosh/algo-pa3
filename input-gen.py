import sys
import random, string

def add_answer(answer, chars, length):
    padding_needed = length - len(answer)

    slots = len(answer) + 1
    pad_counts = [0] * slots
    for _ in range(padding_needed):
        pad_counts[random.randint(0, slots -1)] += 1
    
    result = []

    for i, ch in enumerate(answer):
        result.extend(random.choice(chars) for _ in range(pad_counts[i]))
        result.append(ch)
    result.extend(random.choice(chars) for _ in range(pad_counts[-1]))

    return ''.join(result)

def generate(k, string_length, name):

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

        core_len = random.randint(string_length // 4, string_length // 2)        
        core = [random.choice(inv) for _ in range(core_len)]

        a = add_answer(core, inv, string_length)
        b = add_answer(core, inv, string_length)

        file.write(a)
        file.write('\n')
        file.write(b)

if __name__ == "__main__":
    generate(int(sys.argv[1]),int(sys.argv[2]), sys.argv[3])
