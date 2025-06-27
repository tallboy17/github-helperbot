Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>Explain Elasticsearch query syntax (Booleans, Fields, Ranges)</summary><br><b>
</b></details>  
<details>
<summary>Explain what is Relevance Score</summary><br><b>
</b></details>  
<details>
<summary>Explain Query Context and Filter Context</summary><br><b>  
From the official docs:  
"In the query context, a query clause answers the question “How well does this document match this query clause?” Besides deciding whether or not the document matches, the query clause also calculates a relevance score in the _score meta-field."  
"In a filter context, a query clause answers the question “Does this document match this query clause?” The answer is a simple Yes or No—no scores are calculated. Filter context is mostly used for filtering structured data"
</b></details>  
<details>
<summary>Describe how would an architecture of production environment with large amounts of data would be different from a small-scale environment</summary><br><b>  
There are several possible answers for this question. One of them is as follows:  
A small-scale architecture of elastic will consist of the elastic stack as it is. This means we will have beats, logstash, elastcsearch and kibana.<br>
A production environment with large amounts of data can include some kind of buffering component (e.g. Reddis or RabbitMQ) and also security component such as Nginx.
</b></details>