Repository: charlax/professional-programming
Language: Python
Stars: 47703
Forks: 3794
-----
See also the Python-specific section in [charlax/python-education](https://github.com/charlax/python-education#deployment).  
- [Best Practices Around Production Ready Web Apps with Docker Compose](https://nickjanetakis.com/blog/best-practices-around-production-ready-web-apps-with-docker-compose)
- Avoiding 2 Compose Files for Dev and Prod with an Override File
- Reducing Service Duplication with Aliases and Anchors
- Defining your `HEALTHCHECK` in Docker Compose not your Dockerfile
- Making the most of environment variables
- Using Multi-stage builds to optimize image size
- Running your container as a non-root user
- [Docker Best Practices for Python Developers](https://testdriven.io/blog/docker-best-practices/)
- Use multi-stage builds
- Pay close attention to the order of your Dockerfile commands to leverage layer caching
- Smaller Docker images are more modular and secure (watch out for Alpine though)
- Minimize the number of layers (`RUN`, `COPY`, `ADD`)
- Use unprivileged containers
- Prefer `COPY` over `ADD`
- Cache python packages to the docker host
- Prefer array over string syntax
- Understand the difference between `ENTRYPOINT` and `CMD`
- Include a `HEALTHCHECK` instruction
- Whenever possible, avoid using the `latest` tag.
- Don't store secrets in images
- Use a `.dockerignore` file (include `**/.git`, etc.)
- Lint and Scan Your Dockerfiles and Images (e.g. with `hadolint`)
- Log to stdout or stderr
- [Docker Containers Security](https://tbhaxor.com/docker-containers-security/)