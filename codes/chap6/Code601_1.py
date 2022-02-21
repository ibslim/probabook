# Code601_1.py

# algo MT19937
def algo_MT19937(seed=0):
    # coefficients for MT19937
    (w, n, m, r) = (32, 624, 397, 31)
    a = 0x9908B0DF
    (u, d) = (11, 0xFFFFFFFF)
    (s, b) = ( 7, 0x9D2C5680)
    (t, c) = (15, 0xEFC60000)
    (l, f) = (18, 1812433253)
    (lower_mask, upper_mask)= (0xFFFFFFFF, 0x00000000)

    # The state of the generator array of n elements
    MT = [0 for i in range(n)]
    index = n+1

    # initialize the generator from a seed
    def initialize_mt(seed):
        MT[0] = seed
        for i in range(1, n):
            MT[i]  = (f * (MT[i-1] ^ (MT[i-1] >> (w-2))) + i)  & 0xffffffff

    # Generate a random number
    def generate_number():
        # do a twist on every n numbers
        nonlocal index
        if index >= n:
            for i in range(0, n):
                x = (MT[i] & upper_mask) + (MT[(i + 1) % n] & lower_mask)
                xA = x >> 1 if (x % 2) == 0 else (x >> 1) ^ a
                MT[i] = MT[(i + m) % n] ^ xA
            index = 0

        # Extract a tempered value based on MT[index]
        y = MT[index]
        y = y ^ ((y >> u) & d)
        y = y ^ ((y << s) & b)
        y = y ^ ((y << t) & c)
        y = y ^ (y >> l)

        index += 1
        return y & 0xffffffff

    # Generator core
    initialize_mt(seed)
    while True:
        yield generate_number()

# generate 10 random numbers
if __name__ == '__main__':
    g_MT= algo_MT19937()
    for _ in range(10): print(next(g_MT))

# =====================================================================
2357136044
2546248239
3071714933
3626093760
3729171009
3684848379
3480577985
2632805477
679261451
3685339089
