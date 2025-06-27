Repository: apache/airflow
Language: Python
Stars: 40629
Forks: 15180
-----
We publish Apache Airflow as `apache-airflow` package in PyPI. Installing it however might be sometimes tricky
because Airflow is a bit of both a library and application. Libraries usually keep their dependencies open, and
applications usually pin them, but we should do neither and both simultaneously. We decided to keep
our dependencies as open as possible (in `pyproject.toml`) so users can install different versions of libraries
if needed. This means that `pip install apache-airflow` will not work from time to time or will
produce unusable Airflow installation.  
To have repeatable installation, however, we keep a set of "known-to-be-working" constraint
files in the orphan `constraints-main` and `constraints-2-0` branches. We keep those "known-to-be-working"
constraints files separately per major/minor Python version.
You can use them as constraint files when installing Airflow from PyPI. Note that you have to specify
correct Airflow tag/version/branch and Python versions in the URL.  
1. Installing just Airflow:  
> Note: Only `pip` installation is currently officially supported.  
While it is possible to install Airflow with tools like [Poetry](https://python-poetry.org) or
[pip-tools](https://pypi.org/project/pip-tools), they do not share the same workflow as
`pip` - especially when it comes to constraint vs. requirements management.
Installing via `Poetry` or `pip-tools` is not currently supported.  
There are known issues with ``bazel`` that might lead to circular dependencies when using it to install
Airflow. Please switch to ``pip`` if you encounter such problems. ``Bazel`` community works on fixing
the problem in `this PR <https://github.com/bazelbuild/rules_python/pull/1166>`_ so it might be that
newer versions of ``bazel`` will handle it.  
If you wish to install Airflow using those tools, you should use the constraint files and convert
them to the appropriate format and workflow that your tool requires.  
```bash
pip install 'apache-airflow==3.0.2' \
--constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.0.2/constraints-3.9.txt"
```  
2. Installing with extras (i.e., postgres, google)  
```bash
pip install 'apache-airflow[postgres,google]==3.0.2' \
--constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.0.2/constraints-3.9.txt"
```  
For information on installing provider distributions, check
[providers](http://airflow.apache.org/docs/apache-airflow-providers/index.html).  
<!-- END Installing from PyPI, please keep comment here to allow auto update of PyPI readme.md -->