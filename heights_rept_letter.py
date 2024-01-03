sentence = input("Please Enter a string: ")
freq_ltr = {}

for c in sentence:
    if c in freq_ltr:
        freq_ltr[c] += 1
    else:
        freq_ltr[c] = 1

print("freq letter:",freq_ltr)

highest_freq = 0
for k, v in freq_ltr.items():
    if v > highest_freq:
        highest_freq = v

for k, v in freq_ltr.items():
    if v == highest_freq:
        print(k)
