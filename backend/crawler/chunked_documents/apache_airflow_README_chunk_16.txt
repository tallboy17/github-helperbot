Repository: apache/airflow
Language: Python
Stars: 40629
Forks: 15180
-----
Airflow has a lot of dependencies - direct and transitive, also Airflow is both - library and application,
therefore our policies to dependencies has to include both - stability of installation of application,
but also ability to install newer version of dependencies for those users who develop DAGs. We developed
the approach where `constraints` are used to make sure airflow can be installed in a repeatable way, while
we do not limit our users to upgrade most of the dependencies. As a result we decided not to upper-bound
version of Airflow dependencies by default, unless we have good reasons to believe upper-bounding them is
needed because of importance of the dependency as well as risk it involves to upgrade specific dependency.
We also upper-bound the dependencies that we know cause problems.  
The constraint mechanism of ours takes care about finding and upgrading all the non-upper bound dependencies
automatically (providing that all the tests pass). Our `main` build failures will indicate in case there
are versions of dependencies that break our tests - indicating that we should either upper-bind them or
that we should fix our code/tests to account for the upstream changes from those dependencies.  
Whenever we upper-bound such a dependency, we should always comment why we are doing it - i.e. we should have
a good reason why dependency is upper-bound. And we should also mention what is the condition to remove the
binding.