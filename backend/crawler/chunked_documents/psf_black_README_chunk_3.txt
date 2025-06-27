Repository: psf/black
Language: Python
Stars: 40386
Forks: 2591
-----
To get started right away with sensible defaults:  
```sh
black {source_file_or_directory}
```  
You can run _Black_ as a package if running it as a script doesn't work:  
```sh
python -m black {source_file_or_directory}
```  
Further information can be found in our docs:  
- [Usage and Configuration](https://black.readthedocs.io/en/stable/usage_and_configuration/index.html)  
_Black_ is already [successfully used](https://github.com/psf/black#used-by) by many
projects, small and big. _Black_ has a comprehensive test suite, with efficient parallel
tests, and our own auto formatting and parallel Continuous Integration runner. Now that
we have become stable, you should not expect large formatting changes in the future.
Stylistic changes will mostly be responses to bug reports and support for new Python
syntax. For more information please refer to
[The Black Code Style](https://black.readthedocs.io/en/stable/the_black_code_style/index.html).  
Also, as a safety measure which slows down processing, _Black_ will check that the
reformatted code still produces a valid AST that is effectively equivalent to the
original (see the
[Pragmatism](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html#ast-before-and-after-formatting)
section for details). If you're feeling confident, use `--fast`.