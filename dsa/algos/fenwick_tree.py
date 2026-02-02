class FenwickTree:
    def __init__(self, n):
        self.tree = [0]*(n+1)
    #index 0 is dummy as 0 & -0 = 0
    #so index n-1 of array is n here


    def update(self, i, delta):
        i += 1                          #increment by 1 as nth indexes value would be at n+1
        while i < len(self.tree):
            self.tree[i] += delta
            i += (i & -i)

    #E.g. i is 00111
    #next index to update is 01000
    #next is 10000, next is 100000 until it dont exceed array size

    #here one adds up at front

    def query(self, i):                  #sums from 0 to i
        i += 1
        sum_ = 0
        while i >= 1:
            sum_ += self.tree[i]
            i -= (i & -i)

        return sum_


    #E.g. i is 0111
    #next index to add is 0110
    #next is 0100,  next is  0000 , end!

    #here one from end disappears one by one

    def range_query(self, l, r):
        """Sum in range [l, r]"""
        return self.query(r) - self.query(l - 1)



#use-
# to calculate prefix sums of values, counting values

#update time is logn and so is query time

# https://youtu.be/uSFzHCZ4E-8?si=08GYCONrGJV96LTn