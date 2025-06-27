Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
> Abstraction: hash table  
A key-value store generally allows for O(1) reads and writes and is often backed by memory or SSD.  Data stores can maintain keys in [lexicographic order](https://en.wikipedia.org/wiki/Lexicographical_order), allowing efficient retrieval of key ranges.  Key-value stores can allow for storing of metadata with a value.  
Key-value stores provide high performance and are often used for simple data models or for rapidly-changing data, such as an in-memory cache layer.  Since they offer only a limited set of operations, complexity is shifted to the application layer if additional operations are needed.  
A key-value store is the basis for more complex systems such as a document store, and in some cases, a graph database.