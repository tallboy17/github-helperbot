Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>Can you explain what is a process?</summary><br><b>  
A process is a running program. A program is one or more instructions and the program (or process) is executed by the operating system.
</b></details>  
<details>
<summary>If you had to design an API for processes in an operating system, what would this API look like?</summary><br><b>  
It would support the following:  
* Create - allow to create new processes
* Delete - allow to remove/destroy processes
* State - allow to check the state of the process, whether it's running, stopped, waiting, etc.
* Stop - allow to stop a running process
</b></details>  
<details>
<summary>How a process is created?</summary><br><b>  
* The OS is reading program's code and any additional relevant data
* Program's code is loaded into the memory or more specifically, into the address space of the process.
* Memory is allocated for program's stack (aka run-time stack). The stack also initialized by the OS with data like argv, argc and parameters to main()
* Memory is allocated for program's heap which is required for dynamically allocated data like the data structures linked lists and hash tables
* I/O initialization tasks are performed, like in Unix/Linux based systems, where each process has 3 file descriptors (input, output and error)
* OS is running the program, starting from main()
</b></details>  
<details>
<summary>True or False? The loading of the program into the memory is done eagerly (all at once)</summary><br><b>  
False. It was true in the past but today's operating systems perform lazy loading, which means only the relevant pieces required for the process to run are loaded first.
</b></details>  
<details>
<summary>What are different states of a process?</summary><br><b>  
* Running - it's executing instructions
* Ready - it's ready to run, but for different reasons it's on hold
* Blocked - it's waiting for some operation to complete, for example I/O disk request
</b></details>  
<details>
<summary>What are some reasons for a process to become blocked?</summary><br><b>  
- I/O operations (e.g. Reading from a disk)
- Waiting for a packet from a network
</b></details>  
<details>
<summary>What is Inter Process Communication (IPC)?</summary><br><b>  
Inter-process communication (IPC) refers to the mechanisms provided by an operating system that allow processes to manage shared data.
</b></details>  
<details>
<summary>What is "time sharing"?</summary><br><b>  
Even when using a system with one physical CPU, it's possible to allow multiple users to work on it and run programs. This is possible with time sharing, where computing resources are shared in a way it seems to the user, the system has multiple CPUs, but in fact it's simply one CPU shared by applying multiprogramming and multi-tasking.
</b></details>  
<details>
<summary>What is "space sharing"?</summary><br><b>  
Somewhat the opposite of time sharing. While in time sharing a resource is used for a while by one entity and then the same resource can be used by another resource, in space sharing the space is shared by multiple entities but in a way where it's not being transferred between them.<br>
It's used by one entity, until this entity decides to get rid of it. Take for example storage. In storage, a file is yours, until you decide to delete it.
</b></details>  
<details>
<summary>What component determines which process runs at a given moment in time?</summary><br><b>  
CPU scheduler
</b></details>