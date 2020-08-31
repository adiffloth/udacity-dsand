## Request Routing with a Trie

The solution to this problem is implemented as a Trie where the directory structure of the website is represented as nodes in a Trie. Each node also carries a handler to process requests to a particular URL string.

The Router class handles parsing requests, adding handlers as nodes to the Trie and looking up handlers in the Trie.

The RouterTrie is the Trie itself and manages the nodes, insertions and searches among the nodes.

The RouteTrieNode has a dictionary to hold URL path parts and the corresponding children nodes, as well as the name of the handler for that node.

### Time complexity: 
- RouteTrieNode.insert(): This is implemented as a set() on a Python dictionary, which is O(1).
- RouteTrie.insert(): The insert on the Trie has to traverse the Trie for the length of the URL path, possibly inserting Nodes at each level. This would perform O(1) operations O(h) times, where h is the height of the Trie, resulting in O(h) complexity overall.
- RouteTrie.find(): This method traverses the height of the Trie once, resulting in O(h) time complexity.
- Router.add_handler(): This method calls Router.split_path(), which is O(p), where p is the length of the request path. Then it calls RouteTrie.insert() which is O(h), where h is the height of the Trie. Both p and h will be bounded by the complexity of the website, but it's hard to say which will dominate. Worst case would be a website with a very deep directory structure, so we'll go with O(p) time complexity.
- Router.lookup(): The worst case for lookup is O(p) where p is the depth of the longest valid path.
- Router.split_path(): This is O(p) where p is the longest valid path.

### Space complexity: 
- RouteTrieNode.insert(): This is O(1) for additional space. We're adding a new node, but that is constant.
- RouteTrie.insert(): The worst case is a very long path where every subdir is new and needs to be added. This would be O(p) where p is the longest possible path on the website.
- RouteTrie.find(): This is O(1). We're not creating any new lists.
- Router.add_handler(): This calls Router.split_path(), then RouteTrie.insert(). Those are O(p) and O(p) respectively, so O(p) overall where p is the length of the longest possible path.
- Router.lookup(): The worst case is O(n) where n is the number of pages in the site, if the site is completely flat, with only single pages under the root.
- Router.split_path(): This creates a new list made up of parts of the input string and is therefore O(p) space complexity where p is the length of longest possible path.