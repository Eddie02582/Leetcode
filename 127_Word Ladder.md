#  Word Ladder


## 原題目:
```
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
    Input:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]

    Output: 5

    Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
    return its length 5.

Example 2:
    Input:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]

    Output: 0

    Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
```

## 思路dfs
dfs 會TLE

## Code



#### Python

```python
class Solution:    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in  wordList:
            return 0
        visited = [False] * len(wordList)
        
        self.ans = float('inf') 
        def backtracking(word,count):
            if word == endWord:
                self.ans = min(count,self.ans)               
                return
            for i in range(len(wordList)):
                if not visited[i] and self.canChange(word,wordList[i]):
                    visited[i] = True
                    backtracking(wordList[i],count + 1)
                    visited[i] = False
                    
        backtracking(beginWord,1)       
        
        return  0 if self.ans == float('inf') else self.ans
        
        
    def canChange(self,word1,word2):
        diffCount = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diffCount += 1
            if diffCount >1:
                return False           
        return True
        
```

## 思路BFS


#### Python
```python
class Solution:    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:   
        if endWord not in  wordList:
            return 0           
            
        visited = [False] * len(wordList) 
        queue = [beginWord]   
        count = 0            
        while queue:
            length = len(queue)
            count += 1            
            for i in range(length):
                word = queue.pop(0)                 
                if word == endWord:
                    return count 
                for i in range(len(wordList)):
                    if not visited[i] and self.canChange(word,wordList[i]):
                        queue.append(wordList[i]) 
                        visited[i] = True
        
        return  0 
        
        
    def canChange(self,word1,word2):
        if word1 == word2:
            return False
            
        diffCount = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diffCount += 1
            if diffCount >1:
                return False           
        return True
        
```


bfs

```
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queue for BFS
        queue = deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()      
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0
```



