Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
See your data as an object, similar to what you do with your application code.  Have your application assemble the dataset from the database into a class instance or a data structure(s):  
* Remove the object from cache if its underlying data has changed
* Allows for asynchronous processing: workers assemble objects by consuming the latest cached object  
Suggestions of what to cache:  
* User sessions
* Fully rendered web pages
* Activity streams
* User graph data