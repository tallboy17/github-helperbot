Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>What is "cache"? In which cases would you use it?</summary><br><b>
</b></details>  
<details>
<summary>What is "distributed cache"?</summary><br><b>
</b></details>  
<details>
<summary>What is a "cache replacement policy"?</summary><br><b>  
Take a look [here](https://en.wikipedia.org/wiki/Cache_replacement_policies)
</b></details>  
<details>
<summary>Which cache replacement policies are you familiar with?</summary><br><b>  
You can find a list [here](https://en.wikipedia.org/wiki/Cache_replacement_policies)
</b></details>  
<details>
<summary>Explain the following cache policies:  
* FIFO
* LIFO
* LRU</summary><br><b>  
Read about it [here](https://en.wikipedia.org/wiki/Cache_replacement_policies)
</b></details>  
<details>
<summary>Why not writing everything to cache instead of a database/datastore?</summary><br><b>
Caching and databases serve different purposes and are optimized for different use cases.  
Caching is used to speed up read operations by storing frequently accessed data in memory or on a fast storage medium. By keeping data close to the application, caching reduces the latency and overhead of accessing data from a slower, more distant storage system such as a database or disk.  
On the other hand, databases are optimized for storing and managing persistent data. Databases are designed to handle concurrent read and write operations, enforce consistency and integrity constraints, and provide features such as indexing and querying.
</b></details>