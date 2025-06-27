Repository: apache/airflow
Language: Python
Stars: 40629
Forks: 15180
-----
As of Airflow 2.0, we agreed to certain rules we follow for Python and Kubernetes support.
They are based on the official release schedule of Python and Kubernetes, nicely summarized in the
[Python Developer's Guide](https://devguide.python.org/#status-of-python-branches) and
[Kubernetes version skew policy](https://kubernetes.io/docs/setup/release/version-skew-policy/).  
1. We drop support for Python and Kubernetes versions when they reach EOL. Except for Kubernetes, a
version stays supported by Airflow if two major cloud providers still provide support for it. We drop
support for those EOL versions in main right after EOL date, and it is effectively removed when we release
the first new MINOR (Or MAJOR if there is no new MINOR version) of Airflow. For example, for Python 3.9 it
means that we will drop support in main right after 27.06.2023, and the first MAJOR or MINOR version of
Airflow released after will not have it.  
2. We support a new version of Python/Kubernetes in main after they are officially released, as soon as we
make them work in our CI pipeline (which might not be immediate due to dependencies catching up with
new versions of Python mostly) we release new images/support in Airflow based on the working CI setup.  
3. This policy is best-effort which means there may be situations where we might terminate support earlier
if circumstances require it.