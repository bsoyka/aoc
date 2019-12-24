fac_a = 16_807
fac_b = 48_271
divisor = 2_147_483_647
with open("input.txt") as f:
    generators = [int(line.strip()[23:]) for line in f]


def fmt_bits(x):
    x = bin(x)[2:]
    x = '0' * (16 - len(x)) + x
    return x


final = 0
gen_a = generators[0]
gen_b = generators[1]
for i in range(5_000_000):
    gen_a = (gen_a * fac_a) % divisor
    while gen_a % 4:
        gen_a = (gen_a * fac_a) % divisor
    gen_b = (gen_b * fac_b) % divisor
    while gen_b % 8:
        gen_b = (gen_b * fac_b) % divisor
    if fmt_bits(gen_a)[-16:] == fmt_bits(gen_b)[-16:]:
        final += 1
    if not (i+1) % 100_000:
        print(f"{i+1} done")
print(final)