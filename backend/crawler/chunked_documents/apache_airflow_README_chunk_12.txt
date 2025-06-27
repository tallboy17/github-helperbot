Repository: apache/airflow
Language: Python
Stars: 40629
Forks: 15180
-----
As of Airflow 2.0.0, we support a strict [SemVer](https://semver.org/) approach for all packages released.  
There are few specific rules that we agreed to that define details of versioning of the different
packages:  
* **Airflow**: SemVer rules apply to core airflow only (excludes any changes to providers).
Changing limits for versions of Airflow dependencies is not a breaking change on its own.
* **Airflow Providers**: SemVer rules apply to changes in the particular provider's code only.
SemVer MAJOR and MINOR versions for the packages are independent of the Airflow version.
For example, `google 4.1.0` and `amazon 3.0.3` providers can happily be installed
with `Airflow 2.1.2`. If there are limits of cross-dependencies between providers and Airflow packages,
they are present in providers as `install_requires` limitations. We aim to keep backwards
compatibility of providers with all previously released Airflow 2 versions but
there will sometimes be breaking changes that might make some, or all
providers, have minimum Airflow version specified.
* **Airflow Helm Chart**: SemVer rules apply to changes in the chart only. SemVer MAJOR and MINOR
versions for the chart are independent of the Airflow version. We aim to keep backwards
compatibility of the Helm Chart with all released Airflow 2 versions, but some new features might
only work starting from specific Airflow releases. We might however limit the Helm
Chart to depend on minimal Airflow version.
* **Airflow API clients**: Their versioning is independent from Airflow versions. They follow their own
SemVer rules for breaking changes and new features - which for example allows to change the way we generate
the clients.