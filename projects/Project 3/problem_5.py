#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[1]:


## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        
        # Start at the root
        current_node = self.root
        
        # Iterate through every char, inserting into the Trie
        for char in word:
            if char not in current_node.children:
                current_node.insert(char)

            # Follow the Trie
            current_node = current_node.children[char]

        # After iterating through the word, set is_word on the last node.
        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        
        # Start at the root
        current_node = self.root

        # Iterate through the input prefix
        for char in prefix:
            
            # Return None if the next char is not part of the Trie
            if char not in current_node.children:
                return None
            
            # Otherwise, follow the Trie
            current_node = current_node.children[char]

        return current_node


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[2]:


class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
       
    def suffixes(self, prefix=''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        if self.children:
            for char, node in self.children.items():
                if node.is_word:  # The sequence so far is a complete word, so add it to the results
                    results.add(prefix + char)
                node.suffixes(prefix + char)  # Recurse on the next level down the Trie

        # Sort the results on the length of the word, just to make the display
        # look nicer and more stable.
        result_list = list(results)
        result_list.sort(key=len)
        return result_list


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[3]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod", 'trickle'
]
for word in wordList:
    MyTrie.insert(word)


# In[4]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    results.clear()  # Clear previous results to handle backspace scenario
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

results = set()  # Make this a set to get rid of duplicate hits
interact(f,prefix='');


# In[ ]:




