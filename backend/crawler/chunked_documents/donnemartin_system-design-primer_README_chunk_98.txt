Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
SQL tuning is a broad topic and many [books](https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=sql+tuning) have been written as reference.  
It's important to **benchmark** and **profile** to simulate and uncover bottlenecks.  
* **Benchmark** - Simulate high-load situations with tools such as [ab](http://httpd.apache.org/docs/2.2/programs/ab.html).
* **Profile** - Enable tools such as the [slow query log](http://dev.mysql.com/doc/refman/5.7/en/slow-query-log.html) to help track performance issues.  
Benchmarking and profiling might point you to the following optimizations.