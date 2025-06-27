Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>Explain what is Hadoop</summary><br><b>  
[Apache Hadoop - Wikipedia](https://en.wikipedia.org/wiki/Apache_Hadoop)
</b></details>  
<details>
<summary>Explain Hadoop YARN</summary><br><b>  
Responsible for managing the compute resources in clusters and scheduling users' applications
</b></details>  
<details>
<summary>Explain Hadoop MapReduce</summary><br><b>  
A programming model for large-scale data processing
</b></details>  
<details>
<summary>Explain Hadoop Distributed File Systems (HDFS)</summary><br><b>  
* Distributed file system providing high aggregate bandwidth across the cluster.
* For a user it looks like a regular file system structure but behind the scenes it's distributed across multiple machines in a cluster
* Typical file size is TB and it can scale and supports millions of files
* It's fault tolerant which means it provides automatic recovery from faults
* It's best suited for running long batch operations rather than live analysis
</b></details>  
<details>
<summary>What do you know about HDFS architecture?</summary><br><b>  
[HDFS Architecture](http://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html)  
* Master-slave architecture
* Namenode - master, Datanodes - slaves
* Files split into blocks
* Blocks stored on datanodes
* Namenode controls all metadata
</b></details>