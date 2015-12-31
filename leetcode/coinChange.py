__author__ = 'joe'
# -*- coding: utf-8 -*-


class Solution(object):
    def coinChange(self, coins, amount):

        if len(coins) == 0:
            return -1

        INF = 0x7fffffff
        #INF = float('inf')
        dp = [INF] * (amount+1)
        dp[0] = 0

        for ind in xrange(amount+1):
            for c in coins:
                if ind+c<=amount:
                   dp[ind+c] = min(dp[ind+c], dp[ind]+1)

        return dp[-1] if dp[-1]!=INF else -1
