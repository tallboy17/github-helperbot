Repository: apache/airflow
Language: Python
Stars: 40629
Forks: 15180
-----
Airflow works best with workflows that are mostly static and slowly changing. When the DAG structure is similar from one run to the next, it clarifies the unit of work and continuity. Other similar projects include [Luigi](https://github.com/spotify/luigi), [Oozie](https://oozie.apache.org/) and [Azkaban](https://azkaban.github.io/).  
Airflow is commonly used to process data, but has the opinion that tasks should ideally be idempotent (i.e., results of the task will be the same, and will not create duplicated data in a destination system), and should not pass large quantities of data from one task to the next (though tasks can pass metadata using Airflow's [XCom feature](https://airflow.apache.org/docs/apache-airflow/stable/concepts/xcoms.html)). For high-volume, data-intensive tasks, a best practice is to delegate to external services specializing in that type of work.  
Airflow is not a streaming solution, but it is often used to process real-time data, pulling data off streams in batches.