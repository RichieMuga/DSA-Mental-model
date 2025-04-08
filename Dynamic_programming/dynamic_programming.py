'''
The question we'll be solving is fibbonacci numbers of a given number n
'''

# step 1: Solve the problem naively
class NaiveSolution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return self.fib(n-2)+self.fib(n-1)

# step 2: Top down approach(memoization)
class TopDownSolution:
    def fib(self, n: int) -> int:
        memo = {0:0,1:1}

        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x - 1) + f(x -2)
                return memo[x]
        return f(n)

# step 3: Bottom up solution(tabulation)
class BottomUpSolution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]


# step 4: Bottom Up with constant space
class BottomUpConstantSolution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        dp = [0] * (n + 1)

        prev,cur = 0,1

        for i in range(2, n+1):
            prev,cur = cur, prev+cur
        
        return cur


