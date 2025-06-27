Repository: pytorch/pytorch
Language: Python
Stars: 90893
Forks: 24473
-----
To build documentation in various formats, you will need [Sphinx](http://www.sphinx-doc.org)
and the pytorch_sphinx_theme2.  
Before you build the documentation locally, ensure `torch` is
installed in your environment. For small fixes, you can install the
nightly version as described in [Getting Started](https://pytorch.org/get-started/locally/).  
For more complex fixes, such as adding a new module and docstrings for
the new module, you might need to install torch [from source](#from-source).
See [Docstring Guidelines](https://github.com/pytorch/pytorch/wiki/Docstring-Guidelines)
for docstring conventions.  
```bash
cd docs/
pip install -r requirements.txt
make html
make serve
```  
Run `make` to get a list of all available output formats.  
If you get a katex error run `npm install katex`.  If it persists, try
`npm install -g katex`  
> [!NOTE]
> If you installed `nodejs` with a different package manager (e.g.,
> `conda`) then `npm` will probably install a version of `katex` that is not
> compatible with your version of `nodejs` and doc builds will fail.
> A combination of versions that is known to work is `node@6.13.1` and
> `katex@0.13.18`. To install the latter with `npm` you can run
> ```npm install -g katex@0.13.18```  
> [!NOTE]
> If you see a numpy incompatibility error, run:
> ```
> pip install 'numpy<2'
> ```  
When you make changes to the dependencies run by CI, edit the
`.ci/docker/requirements-docs.txt` file.