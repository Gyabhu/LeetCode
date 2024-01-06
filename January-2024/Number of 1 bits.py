"""
    Write a function that takes the binary representation of an unsigned
    integer and returns the number of '1' bits it has (also known as the Hamming weight).

"""


class Solution:
    def hammingWeight(n):

        # bin = bin(n)
        # print(bin)
        binary = format(int(n), 'b')
        return binary.count("1")


    print(hammingWeight(7))
