Repository: google-research/bert
Language: Python
Stars: 39243
Forks: 9676
-----
We will **not** be able to release the pre-processed datasets used in the paper.
For Wikipedia, the recommended pre-processing is to download
[the latest dump](https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2),
extract the text with
[`WikiExtractor.py`](https://github.com/attardi/wikiextractor), and then apply
any necessary cleanup to convert it into plain text.  
Unfortunately the researchers who collected the
[BookCorpus](http://yknzhu.wixsite.com/mbweb) no longer have it available for
public download. The
[Project Guttenberg Dataset](https://web.eecs.umich.edu/~lahiri/gutenberg_dataset.html)
is a somewhat smaller (200M word) collection of older books that are public
domain.  
[Common Crawl](http://commoncrawl.org/) is another very large collection of
text, but you will likely have to do substantial pre-processing and cleanup to
extract a usable corpus for pre-training BERT.