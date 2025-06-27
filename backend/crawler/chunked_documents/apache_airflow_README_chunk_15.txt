Repository: apache/airflow
Language: Python
Stars: 40629
Forks: 15180
-----
The Airflow Community provides conveniently packaged container images that are published whenever
we publish an Apache Airflow release. Those images contain:  
* Base OS with necessary packages to install Airflow (stable Debian OS)
* Base Python installation in versions supported at the time of release for the MINOR version of
Airflow released (so there could be different versions for 2.3 and 2.2 line for example)
* Libraries required to connect to supported Databases (again the set of databases supported depends
on the MINOR version of Airflow)
* Predefined set of popular providers (for details see the [Dockerfile](https://raw.githubusercontent.com/apache/airflow/main/Dockerfile)).
* Possibility of building your own, custom image where the user can choose their own set of providers
and libraries (see [Building the image](https://airflow.apache.org/docs/docker-stack/build.html))
* In the future Airflow might also support a "slim" version without providers nor database clients installed  
The version of the base OS image is the stable version of Debian. Airflow supports using all currently active
stable versions - as soon as all Airflow dependencies support building, and we set up the CI pipeline for
building and testing the OS version. Approximately 6 months before the end-of-regular support of a
previous stable version of the OS, Airflow switches the images released to use the latest supported
version of the OS.  
For example switch from ``Debian Bullseye`` to ``Debian Bookworm`` has been implemented
before 2.8.0 release in October 2023 and ``Debian Bookworm`` will be the only option supported as of
Airflow 2.10.0.  
Users will continue to be able to build their images using stable Debian releases until the end of regular
support and building and verifying of the images happens in our CI but no unit tests were executed using
this image in the `main` branch.