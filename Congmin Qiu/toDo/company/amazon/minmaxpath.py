input = [[8, 4, 7],
         [6, 3, 9],
         [1, 1, 10 ]]

def helper3(matrix):
    num_row = len(matrix)
    num_col = len(matrix[0])
    
    
    dp = [0] * num_col
    dp[0] = matrix[0][0]
    
    for i in range(1, num_col):
        dp[i] = min(dp[i-1],matrix[0][i])
    
    for i in range(1, num_row):
        dp[0] = min(dp[0], matrix[i][0])#
        
        for j in range(1, num_col):
            prevMax = max(dp[j-1], dp[j])
            dp[j] = min(prevMax, matrix[i][j])
    return dp[-1]
    pass

#%%

def helper2(matrix):
    num_row = len(matrix)
    num_col= len(matrix[0])
    
    dp = [[0]*num_col for _ in range(num_row)]
    dp[0][0] = matrix[0][0]
    
    for i in range(1, num_row):
        dp[i][0] = min(dp[i-1][0], matrix[i][0])
    
    for i in range(1, num_col):
        dp[0][i] = min(dp[0][i-1], matrix[0][i])
        
    for i in range(1, num_row):
        for j in range(1, num_col):
            
            prevMaxMin = max(dp[i-1][j], dp[i][j-1])
            dp[i][j] = min(matrix[i][j], prevMaxMin)
    return dp[-1][-1]
    pass

#%%


def helper(matrix):
    num_row = len(matrix)
    num_col = len(matrix[0])

    res = [0] * num_col
    res[0] = matrix[0][0]

    for i in range(1, num_col):
        res[i] = min(res[i - 1], matrix[0][i])

    # 8, 4, 4

    for i in range(1, num_row):
        res[0] = min(res[0], matrix[i][0])
        for j in range(1, num_col):
            if res[j] < matrix[i][j] and res[j - 1] < matrix[i][j]:
                res[j] = max(res[j - 1], res[j])
            else:
                res[j] = matrix[i][j]
    return res[-1]

    pass


# %%
res = helper3(input)
res
