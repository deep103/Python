'''
Given an array of strings words, return the words that can be typed using letters 
of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:

Input: words = ["omk"]
Output: []

Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]

Constraints:

1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] consists of English letters (both lowercase and uppercase). 
'''

def findWords(words):
    rows = [['q','w','e','r','t','y','u','i','o','p'],
            ['a','s','d','f','g','h','j','k','l'],
            ['z','x','c','v','b','n','m']]
    ans = []
    for word in words: #initializing 'word' with the first value in the 'words' for 1st iteration i.e. 'Alaska'
        k = 0 # constant
        for i in range(len(rows)): # i from 0 to lenght of 'rows' i.e. 0,3. That means it will go up to 2 index
            if word[0].lower() in rows[i]: 
                '''word[0].lower() lowercases the word value i.e. Alaska->alaska for current iteration, and 
                then checks it in the list 'rows' ith value i.e. 0 for this iteration, which checks the
                set(['q','w','e','r','t','y','u','i','o','p']) and since 'a' isn't present in rows[0]
                it will come out of the if condition and for loop will increment to 1 and for 1,
                i surely do not need to explain as u might have guessed it already''' 
                k = i
                break
            '''To sum up the above if condition, it just checks whether the index 0 
            of the first value of the word is present in the particular row. if it is present,
            value of k = i and the if condition breaks there.'''
        for c in word:
            '''this particular for loop is used for indexing every index of the word i.e. 'alaska' 
            in our case and checks A,l,a,s,k,a is present or not in that row i.e. k = 1.
                '''
            if c.lower() not in rows[k]:
                '''every index value is first lowercased and then is checked if it is present
                or not in that row and since 'alaska' is present in that rows[k] i.e. rows[1],
                the condition does not break but comes out of this condition and moves to the else condition
                '''
                break
        else:
            '''the else condition is simply used to append that 'word' that is completely present in the
            particular iteration of that row; to the 'ans' variable of list type'''
            ans.append(word)
    return(ans)
words = ["Alaska", "words", "Dad"]
findWords(words)
