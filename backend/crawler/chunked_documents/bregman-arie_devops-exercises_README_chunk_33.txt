Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>What is the Elastic Stack?</summary><br><b>  
The Elastic Stack consists of:  
* Elasticsearch
* Kibana
* Logstash
* Beats
* Elastic Hadoop
* APM Server  
Elasticsearch, Logstash and Kibana are also known as the ELK stack.
</b></details>  
<details>
<summary>Explain what is Elasticsearch</summary><br><b>  
From the official [docs](https://www.elastic.co/guide/en/elasticsearch/reference/current/documents-indices.html):  
"Elasticsearch is a distributed document store. Instead of storing information as rows of columnar data, Elasticsearch stores complex data structures that have been serialized as JSON documents"
</b></details>  
<details>
<summary>What is Logstash?</summary><br><b>  
From the [blog](https://logit.io/blog/post/the-top-50-elk-stack-and-elasticsearch-interview-questions):  
"Logstash is a powerful, flexible pipeline that collects, enriches and transports data. It works as an extract, transform & load (ETL) tool for collecting log messages."
</b></details>  
<details>
<summary>Explain what beats are</summary><br><b>  
Beats are lightweight data shippers. These data shippers installed on the client where the data resides.
Examples of beats: Filebeat, Metricbeat, Auditbeat. There are much more.<br>
</b></details>  
<details>
<summary>What is Kibana?</summary><br><b>  
From the official docs:  
"Kibana is an open source analytics and visualization platform designed to work with Elasticsearch. You use Kibana to search, view, and interact with data stored in Elasticsearch indices. You can easily perform advanced data analysis and visualize your data in a variety of charts, tables, and maps."
</b></details>  
<details>
<summary>Describe what happens from the moment an app logged some information until it's displayed to the user in a dashboard when the Elastic stack is used</summary><br><b>  
The process may vary based on the chosen architecture and the processing you may want to apply to the logs. One possible workflow is:  
1. The data logged by the application is picked by filebeat and sent to logstash
2. Logstash process the log based on the defined filters. Once done, the output is sent to Elasticsearch
2. Elasticsearch stores the document it got and the document is indexed for quick future access
4. The user creates visualizations in Kibana which based on the indexed data
5. The user creates a dashboard which composed out of the visualization created in the previous step
</b></details>