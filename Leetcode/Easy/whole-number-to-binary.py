class Solution():
    def toBinary(self,num):
        temp = [num]
        final = []
        while num != 1: 
            num //= 2
            temp.append(num)
        temp.reverse()
        for i in temp:
            if i%2 == 0:
                final.append(0)
            else:
                final.append(1)
        #ans = ''.join([str(i) for i in final])
        ans = "".join(map(str,final))
        return ans
num = 13
obj = Solution()
print(obj.toBinary(num))