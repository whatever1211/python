# -------------------------------------------------------------------------------------------------------------------
# Trie (Insert and Search)
# Python program for insert and search
# operation in a Trie

class TrieNode:
	
	# Trie node class
	def __init__(self):
		self.children = [None]*26

		# isEndOfWord is True if node represent the end of the word
		self.isEndOfWord = False

class Trie:
	
	# Trie data structure class
	def __init__(self):
		self.root = self.getNode()

	def getNode(self):
	
		# Returns new trie node (initialized to NULLs)
		return TrieNode()

	def _charToIndex(self,ch):
		
		# private helper function
		# Converts key current character into index
		# use only 'a' through 'z' and lower case
		
		return ord(ch)-ord('a')


	def insert(self,key):
		
		# If not present, inserts key into trie
		# If the key is prefix of trie node,
		# just marks leaf node
		pCrawl = self.root
		length = len(key)
		for level in range(length):
			index = self._charToIndex(key[level])

			# if current character is not present
			if not pCrawl.children[index]:
				pCrawl.children[index] = self.getNode()
			pCrawl = pCrawl.children[index]

		# mark last node as leaf
		pCrawl.isEndOfWord = True

	def search(self, key):
		
		# Search key in the trie
		# Returns true if key presents
		# in trie, else false
		pCrawl = self.root
		length = len(key)
		for level in range(length):
			index = self._charToIndex(key[level])
			if not pCrawl.children[index]:
				return False
			pCrawl = pCrawl.children[index]

		return pCrawl.isEndOfWord

# driver function
def main():

	# Input keys (use only 'a' through 'z' and lower case)
	keys = ["the","a","there","anaswe","any",
			"by","their"]
	output = ["Not present in trie",
			"Present in trie"]

	# Trie object
	t = Trie()

	# Construct trie
	for key in keys:
		t.insert(key)

	# Search for different keys
	print("{} ---- {}".format("the",output[t.search("the")]))
	print("{} ---- {}".format("these",output[t.search("these")]))
	print("{} ---- {}".format("their",output[t.search("their")]))
	print("{} ---- {}".format("thaw",output[t.search("thaw")]))

if __name__ == '__main__':
	main()

# This code is contributed by Atul Kumar (www.facebook.com/atul.kr.007)

# -------------------------------------------------------------------------------------------------------------------
# Trie (Insert and Search and Delete)
class TrieNode:
	def __init__(self):
		self.children = [None] * 26
		self.isEndOfWord = False

def getNode():
	pNode = TrieNode()
	pNode.isEndOfWord = False
	return pNode

def insert(root, key):
	pCrawl = root
	for i in range(len(key)):
		index = ord(key[i]) - ord('a')
		if not pCrawl.children[index]:
			pCrawl.children[index] = getNode()
		pCrawl = pCrawl.children[index]
	pCrawl.isEndOfWord = True

def search(root, key):
	pCrawl = root
	for i in range(len(key)):
		index = ord(key[i]) - ord('a')
		if not pCrawl.children[index]:
			return False
		pCrawl = pCrawl.children[index]
	return pCrawl and pCrawl.isEndOfWord

def isEmpty(root):
	for i in range(26):
		if root.children[i]:
			return False
	return True

def remove(root, key, depth = 0):
	if not root:
		return None

	if depth == len(key):
		if root.isEndOfWord:
			root.isEndOfWord = False
		if isEmpty(root):
			del root
			root = None
		return root

	index = ord(key[depth]) - ord('a')
	root.children[index] = remove(root.children[index], key, depth + 1)

	if isEmpty(root) and not root.isEndOfWord:
		del root
		root = None
	return root

if __name__ == '__main__':
	keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "hero", "heroplane"]
	root = getNode()
	for i in range(len(keys)):
		insert(root, keys[i])
	if search(root, "the"):
		print("Yes")
	else:
		print("No")
	if search(root, "these"):
		print("Yes")
	else:
		print("No")
	root = remove(root, "heroplane")
	if search(root, "hero"):
		print("Yes")
	else:
		print("No")

# -------------------------------------------------------------------------------------------------------------------
# Trie (Insert and Search and Delete and Display)
##Display words in a trie (recursive approach)
class TrieNode:
	def __init__(self):
		self.children=[None]*26
		self.isEndOfWord=False
		
class Trie:
	def __init__(self):
		self.root=self.getNode()
		
	def getNode(self):
		return TrieNode()
	
	def _charToIndex(self,ch):
		return ord(ch)-ord('a')
	
	def search(self,key):
		pCrawl=self.root
		length=len(key)
		for level in range(length):
			index=self._charToIndex(key[level])
			if not pCrawl.children[index]:
				return False
			pCrawl=pCrawl.children[index]
			
		return pCrawl.isEndOfWord
	
	def insert(self,key):
		pCrawl=self.root
		length=len(key)
		for level in range(length):
			index=self._charToIndex(key[level])
			if not pCrawl.children[index]:
				pCrawl.children[index]=self.getNode()
				
			pCrawl=pCrawl.children[index]
			
		pCrawl.isEndOfWord=True
		
	def delete(self,key):
		queue=[]
		pCrawl=self.root
		prev=self.root
		length=len(key)
		for level in range(length):
			index=self._charToIndex(key[level])
			if not pCrawl.children[index]:
				return
			if pCrawl.isEndOfWord:
				queue.append([pCrawl,level])
				
			pCrawl=pCrawl.children[index]
			
		if pCrawl.isEndOfWord == False:
			return
		##If is a prefix of another tree, just change leaf
		flag=False
		for i in range(26):
			if pCrawl.children[index]:
				flag=True
		if flag:
			pCrawl.isEndOfWord==False
			return
		##If not a prefix but a tree longer than others, delete until isEndOfWord == True again/reach root(a unique trie)
		if len(queue)==0:
			index=self._charToIndex(key[0])
			self.root.children[index]=None
			return
		pCrawl,level=queue.pop()
		index=self._charToIndex(key[level])
		pCrawl.children[index]=None
		
	def haschild(self,node):
		for i in range(26):
			if node.children[i]:
				return True
		return False
	
	def displayUtil(self,visited,node,str):
		index=0
		while index<26:
			if node.children[index]:
				str+=chr(97+index)
				#print(2,str)
				if node.children[index].isEndOfWord == False:
					self.displayUtil(visited,node.children[index],str)
					str=str[0 : (len(str)-1)]
				else:
					if str not in visited:
						visited.append(str)
					if self.haschild(node.children[index]):
						self.displayUtil(visited,node.children[index],str)
						str=str[0 : (len(str)-1)]
					
			index+=1
	
	def display(self):
		visited=[]
		str=''
		self.displayUtil(visited,self.root,str)
		print("Content of Trie:")
		for i in range(len(visited)):
			print(visited[i])
		
					
keys = ["the","a","there","bye","any",
			"by","their","answer"]
output = ["Not present in trie","Present in trie"]
t=Trie()
for key in keys:
	t.insert(key)

t.display()

#This code is contributed by Zhaoxin Ban
