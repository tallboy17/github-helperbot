Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
With multiple copies of the same data, we are faced with options on how to synchronize them so clients have a consistent view of the data.  Recall the definition of consistency from the [CAP theorem](#cap-theorem) - Every read receives the most recent write or an error.