Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>What is "virtual memory" and what purpose does serve?</summary><br><b>  
Virtual memory combines your computer's RAM with temporary space on your hard disk. When RAM runs low, virtual memory helps to move data from RAM to a space called a paging file. Moving data to paging file can free up the RAM, so your computer can complete its work. In general, the more RAM your computer has, the faster the programs run.
https://www.minitool.com/lib/virtual-memory.html
</b></details>  
<details>
<summary>What is demand paging?</summary><br><b>  
Demand paging is a memory management technique where pages are loaded into physical memory only when accessed by a process. It optimizes memory usage by loading pages on demand, reducing startup latency and space overhead. However, it introduces some latency when accessing pages for the first time. Overall, it’s a cost-effective approach for managing memory resources in operating systems.
</b></details>  
<details>
<summary>What is copy-on-write?</summary><br><b>
Copy-on-write (COW) is a resource management concept, with the goal to reduce unnecessary copying of information. It is a concept, which is implemented for instance within the POSIX fork syscall, which creates a duplicate process of the calling process.  
The idea:
1. If resources are shared between 2 or more entities (for example shared memory segments between 2 processes), the resources don't need to be copied for every entity, but rather every entity has a READ operation access permission on the shared resource. (the shared segments are marked as read-only)
(Think of every entity having a pointer to the location of the shared resource, which can be dereferenced to read its value)
2. If one entity would perform a WRITE operation on a shared resource, a problem would arise, since the resource also would be permanently changed for ALL other entities sharing it.
(Think of a process modifying some variables on the stack, or allocatingy some data dynamically on the heap, these changes to the shared resource would also apply for ALL other processes, this is definitely an undesirable behaviour)
3. As a solution only, if a WRITE operation is about to be performed on a shared resource, this resource gets COPIED first and then the changes are applied.
</b></details>  
<details>
<summary>What is a kernel, and what does it do?</summary><br><b>  
The kernel is part of the operating system and is responsible for tasks like:  
* Allocating memory
* Schedule processes
* Control CPU
</b></details>  
<details>
<summary>True or False? Some pieces of the code in the kernel are loaded into protected areas of the memory so applications can't overwrite them.</summary><br><b>  
True
</b></details>  
<details>
<summary>What is POSIX?</summary><br><b>  
POSIX (Portable Operating System Interface) is a set of standards that define the interface between a Unix-like operating system and application programs.
</b></details>  
<details>
<summary>Explain what is Semaphore and what its role in operating systems.</summary><br><b>  
A semaphore is a synchronization primitive used in operating systems and concurrent programming to control access to shared resources. It's a variable or abstract data type that acts as a counter or a signaling mechanism for managing access to resources by multiple processes or threads.
</b></details>  
<details>
<summary>What is cache? What is buffer?</summary><br><b>  
Cache: Cache is usually used when processes are reading and writing to the disk to make the process faster, by making similar data used by different programs easily accessible.
Buffer: Reserved place in RAM, which is used to hold data for temporary purposes.
</b></details>