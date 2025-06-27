Repository: localstack/localstack
Language: Python
Stars: 59344
Forks: 4174
-----
LocalStack is developed using Python. To install the LocalStack CLI using `pip`, run the following command:  
```bash
python3 -m pip install localstack
```  
The `localstack-cli` installation enables you to run the Docker image containing the LocalStack runtime. To interact with the local AWS services, you need to install the `awslocal` CLI separately. For installation guidelines, refer to the [`awslocal` documentation](https://docs.localstack.cloud/user-guide/integrations/aws-cli/#localstack-aws-cli-awslocal).  
> **Important**: Do not use `sudo` or run as `root` user. LocalStack must be installed and started entirely under a local non-root user. If you have problems with permissions in macOS High Sierra, install with `pip install --user localstack`