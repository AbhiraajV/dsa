def getFib(n,memo):
    if(n<=1):
        return n
    if(n in memo.keys()):
        return memo[n]
    memo[n] = getFib(n-1,memo) + getFib(n-2,memo)
    print(memo)
    return memo[n];
print(getFib(100,{}))