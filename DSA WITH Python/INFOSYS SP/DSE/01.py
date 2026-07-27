from collections import defaultdict

def count_pairs(arr, D, M):
    freq = defaultdict(int)
    count = 0

    for num in arr:
        # Current remainders
        rem_d = num % D
        rem_m = num % M

        # Required remainder for sum to be divisible by D
        required_d = (D - rem_d) % D

        # Count all previous numbers satisfying both conditions
        count += freq[(required_d, rem_m)]

        # Store current remainder pair
        freq[(rem_d, rem_m)] += 1

    return count


# Example
arr = [1,2,5,4,7]
D = 3
M = 2

print(count_pairs(arr, D, M))


# TC : O(n)