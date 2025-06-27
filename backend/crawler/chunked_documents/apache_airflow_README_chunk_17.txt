Repository: apache/airflow
Language: Python
Stars: 40629
Forks: 15180
-----
Those dependencies are maintained in ``pyproject.toml``.  
There are few dependencies that we decided are important enough to upper-bound them by default, as they are
known to follow predictable versioning scheme, and we know that new versions of those are very likely to
bring breaking changes. We commit to regularly review and attempt to upgrade to the newer versions of
the dependencies as they are released, but this is manual process.  
The important dependencies are:  
* `SQLAlchemy`: upper-bound to specific MINOR version (SQLAlchemy is known to remove deprecations and
introduce breaking changes especially that support for different Databases varies and changes at
various speed)
* `Alembic`: it is important to handle our migrations in predictable and performant way. It is developed
together with SQLAlchemy. Our experience with Alembic is that it very stable in MINOR version
* `Flask`: We are using Flask as the back-bone of our web UI and API. We know major version of Flask
are very likely to introduce breaking changes across those so limiting it to MAJOR version makes sense
* `werkzeug`: the library is known to cause problems in new versions. It is tightly coupled with Flask
libraries, and we should update them together
* `celery`: Celery is a crucial component of Airflow as it used for CeleryExecutor (and similar). Celery
[follows SemVer](https://docs.celeryq.dev/en/stable/contributing.html?highlight=semver#versions), so
we should upper-bound it to the next MAJOR version. Also, when we bump the upper version of the library,
we should make sure Celery Provider minimum Airflow version is updated.
* `kubernetes`: Kubernetes is a crucial component of Airflow as it is used for the KubernetesExecutor
(and similar). Kubernetes Python library [follows SemVer](https://github.com/kubernetes-client/python#compatibility),
so we should upper-bound it to the next MAJOR version. Also, when we bump the upper version of the library,
we should make sure Kubernetes Provider minimum Airflow version is updated.