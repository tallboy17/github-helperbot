Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
* Data is duplicated.
* Constraints can help redundant copies of information stay in sync, which increases complexity of the database design.
* A denormalized database under heavy write load might perform worse than its normalized counterpart.