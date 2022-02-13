class Solution():
    def toNumber(self,num):
        temp = []
        dic = {}
        num = str(num)
        for i in num:
            temp.append(int(i))
        temp.reverse()
        for i in range(0,len(temp)):
            if temp[i] in dic:
                dic[temp[i]] += 2**i
            elif temp[i] == 1:
                dic[temp[i]] = 2**i
        final = str(dic.get(1))
        return int(final)
num = 1110010 #114
obj = Solution()
print(obj.toNumber(num))