"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.


Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
"""

# Implement hash function to map input to fixed size
# Insertion: Use function to find the block, insert on linked list
# Removal: Use hash function to find the block and remove from the linked list
# Search: Use hash function to find the block and search the key on the nodes

# Create node in linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyHashMap:


    def __init__(self):
        """
        Initialize your data structure here.
        """
        # hashmap of fixed size -1000
        self.hashmap = [None] * 1000

    # hash function to map the data
    def _hash(self, data):
        return hash(data) % 1000

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        # Find the block
        # if block has no nodes, create one
        # if block has nodes, traverse the list and if key exists on any node, replace the value
        # else add a node for key, value pair at the end of the linked list
        block = self._hash(key)
        if self.hashmap[block] is None:
            self.hashmap[block] = Node((key, value))
        else:
            current = self.hashmap[block]
            while current:
                k, v = current.data
                if k == key:
                    current.data = (key, value)
                    return
                if current.next is None:
                    current.next = Node((key, value))
                    break
                else:
                    current = current.next

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        # find the block
        # if block is empty or the key doesnt exist on any nodes, return -1
        # else return the value stored on the node for that key
        block = self._hash(key)
        if self.hashmap[block] is None:
            return -1
        current = self.hashmap[block]
        while current:

            k, v = current.data
            if k == key:
                return v
            current = current.next

        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        # find the block
        # traverse the list and remove the particular node corresponding to the key to be deleted
        block = self._hash(key)
        if self.hashmap[block] is None:
            return
        current = self.hashmap[block]
        prev = None

        while current:
            k, v = current.data
            if k == key:
                if prev == None:
                    self.hashmap[block] = current.next
                    return
                else:
                    prev.next = current.next
                    return
            prev = current
            current = current.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)