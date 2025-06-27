Repository: pytorch/pytorch
Language: Python
Stars: 90893
Forks: 24473
-----
To compile a PDF of all PyTorch documentation, ensure you have
`texlive` and LaTeX installed. On macOS, you can install them using:  
```
brew install --cask mactex
```  
To create the PDF:  
1. Run:  
```
make latexpdf
```  
This will generate the necessary files in the `build/latex` directory.  
2. Navigate to this directory and execute:  
```
make LATEXOPTS="-interaction=nonstopmode"
```  
This will produce a `pytorch.pdf` with the desired content. Run this
command one more time so that it generates the correct table
of contents and index.  
> [!NOTE]
> To view the Table of Contents, switch to the **Table of Contents**
> view in your PDF viewer.