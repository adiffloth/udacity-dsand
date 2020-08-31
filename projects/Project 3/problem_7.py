# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, path_part, handler):
        # Insert the node as before
        self.children[path_part] = RouteTrieNode(handler)


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler=None, not_found_handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        # Not found handler is stored at this level since it is not specific to a node.
        self.root = RouteTrieNode(root_handler)
        self.not_found_handler = not_found_handler

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root

        for path_part in path:

            # Insert a new node to represent the directory, but don't give it a handler.
            if path_part not in current_node.children:
                current_node.insert(path_part, None)

            # Traverse down the Trie.
            current_node = current_node.children[path_part]

        # Now we're at the node where we're inserting a handler, so add it.
        current_node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        if path == ['']:
            return self.root.handler

        current_node = self.root

        # Iterate through path, following the Trie nodes until the node doesn't exist
        # or we exhaust the path. Return the handler of the last node, or not_found_handler
        # if there is no handler.
        for path_part in path:
            if path_part not in current_node.children:
                return self.not_found_handler
            current_node = current_node.children[path_part]

        if current_node.handler:
            return current_node.handler
        else:
            return self.not_found_handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(root_handler, not_found_handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_parts = self.split_path(path)
        self.route_trie.insert(path_parts, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        path_parts = self.split_path(path)
        return self.route_trie.find(path_parts)

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here

        path_parts = path.rstrip('/').split('/')
        return path_parts[1:]


# Here are some test cases and expected outputs you can use to test your implementation
# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler('/home/about/contact', 'contact handler')

assert router.lookup("/") == 'root handler'  # Root handler
assert router.lookup("/home") == 'not found handler'  # Intermediate 404
assert router.lookup("/home/about") == 'about handler'  # Valid handler
assert router.lookup("/home/about/") == 'about handler'  # Trailing /
assert router.lookup("/home/about/me") == 'not found handler'  # Terminal 404
assert router.lookup('/home/about/contact') == 'contact handler'
assert router.lookup('/home/about/cont') == 'not found handler'
assert router.lookup('') == 'root handler'

print('Tests passed')
