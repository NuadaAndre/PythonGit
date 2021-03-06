# -*- coding: utf-8 -*-

class CountOnes:
    def countOnes(self, num):
        count = 0
        for i in range(32):
            if (num & (1 << i)) != 0:
                count += 1
                
        return count
    
    def countOnes0(self, num):
        if num < 0:
            # Python的整数是无限长的, -1在Java/C++的32位整数中为: 11...11111 (32个1)
            # 但是在Python中为: ...1111111111111 (无限个1)
            # 因此在遇到负数时要先截断为32位
            num &= (1 << 32)-1
        count = 0
        while num != 0:
            num &= num - 1
            count += 1
        return count