class Node:
    def __init__(self):
        self.children = dict()
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    # O(n) - depends on the number of words
    def insert(self, word):
        # starts with the current node
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                # add the character in the current node
                curr_node.children[char] = Node()# key(char): node(value)

            curr_node = curr_node.children[char]
        curr_node.is_end_of_word = True

    # O(n)
    def delete(self, word):
        self._delete(self.root, word, 0)
    
    def _delete(self, curr_node, word, index):
        if index == len(word):
            if not curr_node.is_end_of_word:
                # because obviously we are not removing anything
                return False
            curr_node.is_end_of_word = False

            return len(curr_node.children) == 0
        char = word[index]
        node = curr_node.children.get(char)

        if node is None:
            return False
        
        delete_current_node = self._delete(node, word, index+1)

        if delete_current_node:
            del(curr_node.children[char])
            return len(curr_node.children) == 0 and not curr_node.is_end_of_word
        return False

    
    #O(n)
    def search(self, word):
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]

        curr_node.is_end_of_word = True

    def has_prefix(self, prefix):
        curr_node = self.root

        for char in prefix:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]

        return True

    def list_words(self):
        words = []

        def _dfs(curr_node, paths):
            if curr_node.is_end_of_word:
                words.append(''.join(paths))
            for c, child_nodes in curr_node.children.items():
                _dfs(child_nodes, paths+[c])
        
        _dfs(self.root, [])

        return words

    def starts_with(self, prefix):
        words = []
        curr_node = self.root

        for c in prefix:
            if c not in curr_node.children:
                return words
            curr_node = curr_node.children[c]

        def _dfs(curr_node, paths):
            if curr_node.is_end_of_word:
                words.append(''.join(paths))
            for c, child_nodes in curr_node.children.items():
                _dfs(child_nodes, paths+[c])

        _dfs(curr_node, list(prefix))
        return words

trie = Trie()

trie.insert("Omosh")
trie.insert("Christian")
trie.insert("Omolo")
trie.insert("Osama")
trie.insert("Olive")
trie.insert("Olivia")

print(trie.list_words())
print(trie.has_prefix('om'))

print(trie.has_prefix('Ol'))

trie.delete('Omosh')

print(trie.starts_with("Om"))
print(trie.search("Omolo"))
print(trie.search("Omosh"))

trie.insert("Sly")

print(trie.list_words())
