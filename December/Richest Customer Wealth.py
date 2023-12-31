"""You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth."""

class Solution:
    def maximumWealth(acc):
        list_max_values = []
        for i in acc:
            list_max_values.append(sum(i))
        return max(list_max_values)

    def maximumWealthAlt(acc):
        ans = int()
        for i in acc:
            ans = max(sum(i), ans)
        return ans



    accounts = [[1, 2, 3], [3, 2, 1]]
    print(maximumWealth(accounts))
    print(maximumWealthAlt(accounts))