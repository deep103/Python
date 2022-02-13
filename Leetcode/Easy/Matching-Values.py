class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        count=0
        val=0
        if ruleKey=="type":
            val=0
        elif ruleKey=="color":
            val=1
        elif ruleKey=="name":
            val=2
        for item in items:
            if item[val]==ruleValue:
                count+=1
        return count
items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]] 
ruleKey = "color" 
ruleValue = "silver"
obj = Solution()
print(obj.countMatches(items,ruleKey,ruleValue))