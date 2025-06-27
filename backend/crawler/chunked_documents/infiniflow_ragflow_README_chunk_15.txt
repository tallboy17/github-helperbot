Repository: infiniflow/ragflow
Language: Python
Stars: 57089
Forks: 5604
-----
When it comes to system configurations, you will need to manage the following files:  
- [.env](./docker/.env): Keeps the fundamental setups for the system, such as `SVR_HTTP_PORT`, `MYSQL_PASSWORD`, and
`MINIO_PASSWORD`.
- [service_conf.yaml.template](./docker/service_conf.yaml.template): Configures the back-end services. The environment variables in this file will be automatically populated when the Docker container starts. Any environment variables set within the Docker container will be available for use, allowing you to customize service behavior based on the deployment environment.
- [docker-compose.yml](./docker/docker-compose.yml): The system relies on [docker-compose.yml](./docker/docker-compose.yml) to start up.  
> The [./docker/README](./docker/README.md) file provides a detailed description of the environment settings and service
> configurations which can be used as `${ENV_VARS}` in the [service_conf.yaml.template](./docker/service_conf.yaml.template) file.  
To update the default HTTP serving port (80), go to [docker-compose.yml](./docker/docker-compose.yml) and change `80:80`
to `<YOUR_SERVING_PORT>:80`.  
Updates to the above configurations require a reboot of all containers to take effect:  
> ```bash
> $ docker compose -f docker-compose.yml up -d
> ```