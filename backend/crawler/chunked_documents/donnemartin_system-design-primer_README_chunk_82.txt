Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
A relational database like SQL is a collection of data items organized in tables.  
**ACID** is a set of properties of relational database [transactions](https://en.wikipedia.org/wiki/Database_transaction).  
* **Atomicity** - Each transaction is all or nothing
* **Consistency** - Any transaction will bring the database from one valid state to another
* **Isolation** - Executing transactions concurrently has the same results as if the transactions were executed serially
* **Durability** - Once a transaction has been committed, it will remain so  
There are many techniques to scale a relational database: **master-slave replication**, **master-master replication**, **federation**, **sharding**, **denormalization**, and **SQL tuning**.