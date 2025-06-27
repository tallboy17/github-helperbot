Repository: apache/airflow
Language: Python
Stars: 40629
Forks: 15180
-----
There are other ways of installing and using Airflow. Those are "convenience" methods - they are
not "official releases" as stated by the `ASF Release Policy`, but they can be used by the users
who do not want to build the software themselves.  
Those are - in the order of most common ways people install Airflow:  
- [PyPI releases](https://pypi.org/project/apache-airflow/) to install Airflow using standard `pip` tool
- [Docker Images](https://hub.docker.com/r/apache/airflow) to install airflow via
`docker` tool, use them in Kubernetes, Helm Charts, `docker-compose`, `docker swarm`, etc. You can
read more about using, customizing, and extending the images in the
[Latest docs](https://airflow.apache.org/docs/docker-stack/index.html), and
learn details on the internals in the [images](https://airflow.apache.org/docs/docker-stack/index.html) document.
- [Tags in GitHub](https://github.com/apache/airflow/tags) to retrieve the git project sources that
were used to generate official source packages via git  
All those artifacts are not official releases, but they are prepared using officially released sources.
Some of those artifacts are "development" or "pre-release" ones, and they are clearly marked as such
following the ASF Policy.