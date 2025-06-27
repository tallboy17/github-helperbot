Repository: apache/airflow
Language: Python
Stars: 40629
Forks: 15180
-----
The main part of the Airflow is the Airflow Core, but the power of Airflow also comes from a number of
providers that extend the core functionality and are released separately, even if we keep them (for now)
in the same monorepo for convenience. You can read more about the providers in the
[Providers documentation](https://airflow.apache.org/docs/apache-airflow-providers/index.html). We also
have set of policies implemented for maintaining and releasing community-managed providers as well
as the approach for community vs. 3rd party providers in the [providers](https://github.com/apache/airflow/blob/main/PROVIDERS.rst) document.  
Those `extras` and `providers` dependencies are maintained in `provider.yaml` of each provider.  
By default, we should not upper-bound dependencies for providers, however each provider's maintainer
might decide to add additional limits (and justify them with comment).  
<!-- START Contributing, please keep comment here to allow auto update of PyPI readme.md -->