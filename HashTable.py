"""Basic Hash Table Implementation"""

class Container:
    """Represents a node in the linked list, containing a key-value pair and a pointer to the next node."""
    def __init__(self,key,value,):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    """Initializing a hash table data structure with fixed capacity."""

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _get_hash_index(self, key):
        """Calculate the hash index for the given key."""

        if len(key) == 0:
            return 0

        hash_value = 1
        prime_multiplier = 13

        for char in key:
            hash_value = (hash_value * prime_multiplier + ord(char)) % self.capacity
        return hash_value

    def insert_pair(self,key,value):
        """ Insert a key-value pair into the hash table."""

        index = self._get_hash_index(key)

        if self.table[index] is None: #if slot is empty
            self.table[index] = Container(key, value)
            self.size += 1
        else: #hanfling collisions
            current = self.table[index] #slot is not emppty
            while current:
                if current.key == key:
                    current.value = value #replacing the exiisting key-val pair with the new one if it's a duplivate
                    return
                if current.next is None:  # to handle end of the linked list
                    break
                current = current.next

            new_container = Container(key, value)
            new_container.next = self.table[index]
            self.table[index] = new_container
            self.size += 1

    def search(self, key):
        """ Search for a key in the hash table."""

        index = self._get_hash_index(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove_element(self, key):
        index = self._get_hash_index(key)
        previous = None
        current = self.table[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return True
            previous = current
            current = current.next
        raise KeyError(key)

    def __str__(self):
        """ Return a string representation of the hash table."""

        elements = []
        for i in range(self.capacity):
            current = self.table[i]
            while current:
                elements.append((current.key, current.value))
                current = current.next
        return str(elements)


if __name__ == "__main__":
    # Create a hash table instance
    hash_table = HashTable(20)

    # Space allocation
    hash_table.insert_pair('1', 5)
    hash_table.insert_pair('2', 15)
    hash_table.insert_pair('3', 20)
    hash_table.insert_pair('4', 7)

    print("Hash Table:")
    print(hash_table)

    # Search for a key and print its value
    if hash_table.search('4') != -1:
        print("Value of Key 4 =", hash_table.search('4'))
    else:
        print("Key 4 does not exist")

    # Delete a key
    if hash_table.remove_element('4') != -1:
        print("Node value of key 4 is deleted successfully")
    else:
        print("Key does not exist")

    print("Hash Table after Deletion:")
    print(hash_table)

    # Search for the deleted key again
    if hash_table.search('4') != -1:
        print("Value of Key 4 =", hash_table.search('4'))
    else:
        print("Key 4 does not exist")

    # Insert a new key-value pair
    hash_table.insert_pair('7', 8)



