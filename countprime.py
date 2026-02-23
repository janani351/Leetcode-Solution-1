class Solution:
    def countPrimes(self, n: int) -> int:
        """
        Count the number of prime numbers less than n using the Sieve of Eratosthenes algorithm.
      
        Args:
            n: Upper bound (exclusive) for counting primes
          
        Returns:
            Number of prime numbers less than n
        """
        # Edge case: no primes less than 2
        if n <= 2:
            return 0
      
        # Initialize a boolean array where True means the index is potentially prime
        # Index represents the number itself (0 to n-1)
        is_prime = [True] * n
      
        # 0 and 1 are not prime numbers
        is_prime[0] = is_prime[1] = False
      
        prime_count = 0
      
        # Iterate through all numbers from 2 to n-1
        for current_num in range(2, n):
            # If current_num hasn't been marked as composite
            if is_prime[current_num]:
                # Count this prime number
                prime_count += 1
              
                # Mark all multiples of current_num as composite (not prime)
                # Start from current_num * 2 and increment by current_num
                for multiple in range(current_num * 2, n, current_num):
                    is_prime[multiple] = False
      
        return prime_count
