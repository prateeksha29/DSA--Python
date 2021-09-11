"""
Count the number of prime numbers less than a non-negative number, n.



Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

# Approach: Sieve of Eratosthenes
# Same as iterating till square root of n
# Also simultaneously updating the multiples of the number as non-prime



# Using Dictionary
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        numbers = defaultdict(int)
        for i in range(2, int(sqrt(n))+1):
            if i not in numbers:
                new_dict = {k:1 for k in range(i*i, n, i)}
                numbers.update(new_dict)
        # numbers - non primes - (1 and 0)
        return n - len(numbers) - 2

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        numbers = defaultdict(int)
        for i in range(2, int(sqrt(n))+1):
            if i not in numbers:
                numbers.update(dict.fromkeys(list(range(i*i, n, i)), 1))
        # numbers - non primes - (1 and 0)
        return n - len(numbers) - 2




# Using Array (Faster due to indexing)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        prime = [1] * n

        for i in range(2, int(sqrt(n)) + 1):
            if prime[i] == 1:
                prime[i * i:n:i] = [0] * ((((n - 1) - i * i) // i) + 1)  # [0] * (end - start/n  + 1)

        # excluding 1 and 0 because the value was initially defaulted at 1 for all numbers
        return sum(prime) - 2