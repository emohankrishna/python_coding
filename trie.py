class TrieNode:
    def __init__(self,value=None,isEndOfWord=False):
        self.count =0
        self.value = value
        self.isEndOfWord = isEndOfWord
        self.children = dict()
        self.parent = None

    def getValue(self):
        return self.value

    def display_children(self,current_node):
        temp = current_node
        child_list =[]
        for node in temp.children:
            if(node is not None):
                child_list.append(node.getValue())
        print(child_list)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_one(self, word):
        length = len(word)
        temp_node :TrieNode = self.root
        for i in range(length):
            char = word[i]
            if(temp_node.children.get(char) is None):
                trie_new_node = TrieNode(char)
                if i == length - 1:
                    trie_new_node.isEndOfWord = True
                    trie_new_node.count = 1
                trie_new_node.parent = temp_node
                temp_node.children[char]= trie_new_node
                temp_node = trie_new_node
            elif temp_node.children.get(char) is not None:
                temp_node = temp_node.children.get(char)
                if temp_node.count != 0 and i!= length-1:
                    temp_node.isEndOfWord = False
                elif temp_node.count !=0 and i==length -1:
                    temp_node.count = temp_node.count +1

    def add_many(self,add_list=[]):
        if add_list.__len__() == 0:
            return
        else:
            for word in add_list:
                self.add_one(word)


    def display(self,current_node:TrieNode,l=[]):
        pass

    def get_remaining_count(self,root:TrieNode,count =0):
        temp:TrieNode = root
        children : dict = temp.children
        if children.__len__() == 0:
            return count+temp.count
        else:
            if temp.count > 0 :
                count = count + temp.count
            for trie_node in children.values():
                count =  self.get_remaining_count(trie_node,count)
            else:
                return count



    def get_prefix_count(self,word):
        temp : TrieNode = self.root
        counter = 0
        for i in range(0,len(word)):
            if temp.children.get(word[i]) is None:
                return 0
            elif temp.children.get(word[i]):
                temp = temp.children.get(word[i])
                if temp.count > 0 and temp.isEndOfWord and len(word)-1 == i:
                    #given word is present in the Trie
                    counter = counter + 1
                    self.get_remaining_count(temp.children)







    def search_word(self,word):
        current_node : TrieNode = self.root
        f_count : int = 0
        for i in range(len(word)):
            if current_node.children.get(word[i]) is not None:
                if i != len(word)-1 and not current_node.children.get(word[i]).isEndOfWord:
                    current_node = current_node.children.get(word[i])
                elif i == len(word)-1 and current_node.children.get(word[i]).count > 0:
                    return True
            else:
                return False
        return False





trie = Trie()
trie.add_one("abc")
trie.add_one("abcde")
trie.add_many(['mohan','bhargav','sahith','sai','mohit'])
trie.add_one("moh")
# trie.add_many(['mohan','bhargav','sahith','sai','kanna'])
# trie.add_one("mohan")
# print("Ajith",trie.search_word("Ajith"))
# print('bhargav',trie.search_word("bhargav"))
# print('sathih',trie.search_word("sahith"))
# print('sai',trie.search_word("sai"))
# print('sahit',trie.search_word("sahit"))
print("Count : ",trie.get_remaining_count(trie.root))
