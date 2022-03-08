import time
from os.path import dirname, join
import os
from math import sqrt, floor


def get_first_primes(lim: int):
    ca = 3
    ca_inc_at = 9
    ret = [2, 3, 5]
    for num in range(7, lim + 1, 2):
        if num >= ca_inc_at:
            ca += 1
            ca_inc_at = (ca + 1) ** 2

        for nu in ret:
            if nu > ca:
                ret.append(num)
                break
            if num % nu == 0:
                break
        else:
            ret.append(num)
    return ret


primes_dir = join(dirname(__file__), "prime_files")

current_file_num = 1
start: int = int(input("start >> "))
limit: int = int(input("limit >> "))
make_files = ""
while make_files.lower() not in ["y", "n"]:
    make_files = input("Y/N add all the primes to files >> ")

make_files = make_files.lower() == "y"
if make_files:
    for f in os.listdir(primes_dir):
        os.remove(join(primes_dir, f))
        print(f"deleted `{f}`")
start_time = time.time()
last_time = start_time
primes = []
needed = floor(sqrt(limit)) + 1000
first_primes = get_first_primes(needed)
print(f"{len(first_primes):,}")
current_len = 0


if start <= 3:
    start = 4
    primes.append(2)
    primes.append(3)
    current_len = 2
    start = 5

if start % 2 == 0:
    start += 1

cap = floor(sqrt(start))
cap_inc_at = (cap+1)**2

for number in range(start, limit + 1, 2):
    if number >= cap_inc_at:
        cap += 1
        cap_inc_at = (cap+1)**2

    for n in first_primes:
        if n > cap:
            primes.append(number)
            current_len += 1
            break
        if number % n == 0:
            break

    if make_files and current_len >= 200000:
        with open(join(primes_dir, f"primes {current_file_num}.txt"), "w") as f:
            f.write("\n".join(map(str, primes)))
        primes = []
        current_len = 0
        current_file_num += 1
        time_taken = time.time() - last_time
        print(f"currently at {number:,}, time taken {'--- %s seconds ---' % time_taken}")
        last_time = time.time()
        with open("data", "a") as f:
            f.write(f"{number} {time_taken}\n")
    elif current_len >= 200000:
        primes = []
        current_len = 0
        time_taken = time.time() - last_time
        with open("data", "a") as f:
            f.write(f"{number} {time_taken}\n")
        print(f"Added to data file, currently at: {number:,}\nTook {time_taken} seconds")

if make_files:
    with open(join(primes_dir, f"primes {current_file_num}.txt"), "w") as f:
        f.write("\n".join(map(str, primes)))
input("--- %s seconds ---" % (time.time() - start_time))
