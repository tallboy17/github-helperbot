Repository: psf/black
Language: Python
Stars: 40386
Forks: 2591
-----
_Black_ is able to read project-specific default values for its command line options
from a `pyproject.toml` file. This is especially useful for specifying custom
`--include` and `--exclude`/`--force-exclude`/`--extend-exclude` patterns for your
project.  
You can find more details in our documentation:  
- [The basics: Configuration via a file](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#configuration-via-a-file)  
And if you're looking for more general configuration documentation:  
- [Usage and Configuration](https://black.readthedocs.io/en/stable/usage_and_configuration/index.html)  
**Pro-tip**: If you're asking yourself "Do I need to configure anything?" the answer is
"No". _Black_ is all about sensible defaults. Applying those defaults will have your
code in compliance with many other _Black_ formatted projects.