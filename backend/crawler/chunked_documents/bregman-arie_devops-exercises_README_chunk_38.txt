Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>What is Filebeat?</summary><br><b>  
Filebeat is used to monitor the logging directories inside of VMs or mounted as a sidecar if exporting logs from containers, and then forward these logs onward for further processing, usually to logstash.
</b></details>  
<details>
<summary>If one is using ELK, is it a must to also use filebeat? In what scenarios it's useful to use filebeat?</summary><br><b>  
Filebeat is a typical component of the ELK stack, since it was developed by Elastic to work with the other products (Logstash and Kibana). It's possible to send logs directly to logstash, though this often requires coding changes for the application. Particularly for legacy applications with little test coverage, it might be a better option to use filebeat, since you don't need to make any changes to the application code.
</b></details>  
<details>
<summary>What is a harvester?</summary><br><b>  
Read [here](https://www.elastic.co/guide/en/beats/filebeat/current/how-filebeat-works.html#harvester)
</b></details>  
<details>
<summary>True or False? a single harvester harvest multiple files, according to the limits set in filebeat.yml</summary><br><b>  
False. One harvester harvests one file.
</b></details>  
<details>
<summary>What are filebeat modules?</summary><br><b>  
These are pre-configured modules for specific types of logging locations (eg, Traefik, Fargate, HAProxy) to make it easy to configure forwarding logs using filebeat. They have different configurations based on where you're collecting logs from.
</b></details>