Repository: apache/airflow
Language: Python
Stars: 40629
Forks: 15180
-----
| Badges     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| License    | [![License](https://img.shields.io/:license-Apache%202-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0.txt)                                                                                                                                                                                                                                                                                                                                               |
| PyPI       | [![PyPI version](https://badge.fury.io/py/apache-airflow.svg)](https://badge.fury.io/py/apache-airflow) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/apache-airflow.svg)](https://pypi.org/project/apache-airflow/) [![PyPI - Downloads](https://img.shields.io/pypi/dm/apache-airflow)](https://pypi.org/project/apache-airflow/)                                                                                                           |
| Containers | [![Docker Pulls](https://img.shields.io/docker/pulls/apache/airflow.svg)](https://hub.docker.com/r/apache/airflow) [![Docker Stars](https://img.shields.io/docker/stars/apache/airflow.svg)](https://hub.docker.com/r/apache/airflow) [![Artifact HUB](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/apache-airflow)](https://artifacthub.io/packages/search?repo=apache-airflow)                                                  |
| Community  | [![Contributors](https://img.shields.io/github/contributors/apache/airflow)](https://github.com/apache/airflow/graphs/contributors) [![Slack Status](https://img.shields.io/badge/slack-join_chat-white.svg?logo=slack&style=social)](https://s.apache.org/airflow-slack) ![Commit Activity](https://img.shields.io/github/commit-activity/m/apache/airflow) [![OSSRank](https://shields.io/endpoint?url=https://ossrank.com/shield/6)](https://ossrank.com/p/6) |  
| Version | Build Status                                                                                                                                                                                                                                                                                                            |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Main    | [![GitHub Build main](https://github.com/apache/airflow/actions/workflows/ci-amd.yml/badge.svg)](https://github.com/apache/airflow/actions) [![GitHub Build main](https://github.com/apache/airflow/actions/workflows/ci-arm.yml/badge.svg)](https://github.com/apache/airflow/actions)                                 |
| 3.x     | [![GitHub Build 3.0](https://github.com/apache/airflow/actions/workflows/ci-amd.yml/badge.svg?branch=v3-0-test)](https://github.com/apache/airflow/actions) [![GitHub Build 3.0](https://github.com/apache/airflow/actions/workflows/ci-arm.yml/badge.svg?branch=v3-0-test)](https://github.com/apache/airflow/actions) |
| 2.x     | [![GitHub Build 2.11](https://github.com/apache/airflow/actions/workflows/ci.yml/badge.svg?branch=v2-11-test)](https://github.com/apache/airflow/actions)                                                                                                                                                               |  
<picture width="500">
<img
src="https://github.com/apache/airflow/blob/19ebcac2395ef9a6b6ded3a2faa29dc960c1e635/docs/apache-airflow/img/logos/wordmark_1.png?raw=true"
alt="Apache Airflow logo"
/>
</picture>  
[Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/) (or simply Airflow) is a platform to programmatically author, schedule, and monitor workflows.  
When workflows are defined as code, they become more maintainable, versionable, testable, and collaborative.  
Use Airflow to author workflows as directed acyclic graphs (DAGs) of tasks. The Airflow scheduler executes your tasks on an array of workers while following the specified dependencies. Rich command line utilities make performing complex surgeries on DAGs a snap. The rich user interface makes it easy to visualize pipelines running in production, monitor progress, and troubleshoot issues when needed.  
<!-- END Apache Airflow, please keep comment here to allow auto update of PyPI readme.md -->
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of contents**  
- [Project Focus](#project-focus)
- [Principles](#principles)
- [Requirements](#requirements)
- [Getting started](#getting-started)
- [Installing from PyPI](#installing-from-pypi)
- [Installation](#installation)
- [Official source code](#official-source-code)
- [Convenience packages](#convenience-packages)
- [User Interface](#user-interface)
- [Semantic versioning](#semantic-versioning)
- [Version Life Cycle](#version-life-cycle)
- [Support for Python and Kubernetes versions](#support-for-python-and-kubernetes-versions)
- [Base OS support for reference Airflow images](#base-os-support-for-reference-airflow-images)
- [Approach to dependencies of Airflow](#approach-to-dependencies-of-airflow)
- [Contributing](#contributing)
- [Voting Policy](#voting-policy)
- [Who uses Apache Airflow?](#who-uses-apache-airflow)
- [Who maintains Apache Airflow?](#who-maintains-apache-airflow)
- [What goes into the next release?](#what-goes-into-the-next-release)
- [Can I use the Apache Airflow logo in my presentation?](#can-i-use-the-apache-airflow-logo-in-my-presentation)
- [Links](#links)
- [Sponsors](#sponsors)  
<!-- END doctoc generated TOC please keep comment here to allow auto update -->