'''
Given a string licensePlate and an array of strings words, find the shortest completing word in words.

A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), 
and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".

Return the shortest completing word in words. It is guaranteed an answer exists. 
If there are multiple shortest completing words, return the first one that occurs in words.

Example 1:

Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
Output: "steps"
Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
"step" contains 't' and 'p', but only contains 1 's'.
"steps" contains 't', 'p', and both 's' characters.
"stripe" is missing an 's'.
"stepple" is missing an 's'.
Since "steps" is the only word containing all the letters, that is the answer.

Example 2:

Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
Output: "pest"
Explanation: licensePlate only contains the letter 's'. 
All the words contain 's', but among these "pest", "stew", and "show" are shortest. 
The answer is "pest" because it is the word that appears earliest of the 3.
'''

class Solution():

    def shortestWords(self,licensePlate,words):
        dict1 = {}
        dict2 = {}
        characters = ['a','b','c','d','e','f','g','h','i','j',
                    'k','l','m','n','o','p','q','r','s','t',
                    'u','v','w','x','y','z']
        numbers = ['1','2','3','4','5','6','7','8','9','0',' ']
        temp = list(licensePlate)
        for i in licensePlate:
            if i.lower() in dict1.keys() and i.lower() in characters:
                dict1[i.lower()] += 1
            elif i.lower() not in numbers:
                dict1[i.lower()] = 1
                continue
        dict1_val = dict1.values()
        total_val = sum(dict1_val)
        for i in range(len(temp)):
            if temp[i].lower() not in characters:
                temp[i] = ""
                continue
        while "" in temp:
            temp.remove("")
        # print(temp)
        words.sort()
        print(words)
        for i in words:
            for j in range(len(words)):
                if len(i) > len(words[j+1]) and j<len(words):
                    words[j] = ""
                    break
                else:
                    break
        while "" in words:
            words.remove("")
        # print(words)
        for i in words:
            for j in range(len(i)):
                if i[j] in dict2.keys():
                    dict2[i[j]] += 1
                elif i[j] not in dict2.keys() and i[j] in dict1.keys():
                    dict2[i[j]] = 1
                    continue
                else:
                    continue
            if dict1 == dict2:
                print(i) 
                break
            elif dict1 != dict2:
                dict2.clear()
                continue      
licensePlate = "1s3 PSt" 
words = ["step","steps","stripe","stepple"]
# licensePlate = "1s3 PSt" 
# words = ["step","steps","stripe","stepple"]
# licensePlate = "1s3 456"
# words = ["stew","looks","pest","show"]
ob1 = Solution()
ob1.shortestWords(licensePlate, words)
