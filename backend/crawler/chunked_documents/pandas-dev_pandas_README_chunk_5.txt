Repository: pandas-dev/pandas
Language: Python
Stars: 45747
Forks: 18598
-----
Here are just a few of the things that pandas does well:  
- Easy handling of [**missing data**][missing-data] (represented as
`NaN`, `NA`, or `NaT`) in floating point as well as non-floating point data
- Size mutability: columns can be [**inserted and
deleted**][insertion-deletion] from DataFrame and higher dimensional
objects
- Automatic and explicit [**data alignment**][alignment]: objects can
be explicitly aligned to a set of labels, or the user can simply
ignore the labels and let `Series`, `DataFrame`, etc. automatically
align the data for you in computations
- Powerful, flexible [**group by**][groupby] functionality to perform
split-apply-combine operations on data sets, for both aggregating
and transforming data
- Make it [**easy to convert**][conversion] ragged,
differently-indexed data in other Python and NumPy data structures
into DataFrame objects
- Intelligent label-based [**slicing**][slicing], [**fancy
indexing**][fancy-indexing], and [**subsetting**][subsetting] of
large data sets
- Intuitive [**merging**][merging] and [**joining**][joining] data
sets
- Flexible [**reshaping**][reshape] and [**pivoting**][pivot-table] of
data sets
- [**Hierarchical**][mi] labeling of axes (possible to have multiple
labels per tick)
- Robust IO tools for loading data from [**flat files**][flat-files]
(CSV and delimited), [**Excel files**][excel], [**databases**][db],
and saving/loading data from the ultrafast [**HDF5 format**][hdfstore]
- [**Time series**][timeseries]-specific functionality: date range
generation and frequency conversion, moving window statistics,
date shifting and lagging  
[missing-data]: https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html
[insertion-deletion]: https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#column-selection-addition-deletion
[alignment]: https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html?highlight=alignment#intro-to-data-structures
[groupby]: https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#group-by-split-apply-combine
[conversion]: https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#dataframe
[slicing]: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#slicing-ranges
[fancy-indexing]: https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#advanced
[subsetting]: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#boolean-indexing
[merging]: https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#database-style-dataframe-or-named-series-joining-merging
[joining]: https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#joining-on-index
[reshape]: https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html
[pivot-table]: https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html
[mi]: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#hierarchical-indexing-multiindex
[flat-files]: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#csv-text-files
[excel]: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#excel-files
[db]: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#sql-queries
[hdfstore]: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#hdf5-pytables
[timeseries]: https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#time-series-date-functionality