Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
Overall availability decreases when two components with availability < 100% are in sequence:  
```
Availability (Total) = Availability (Foo) * Availability (Bar)
```  
If both `Foo` and `Bar` each had 99.9% availability, their total availability in sequence would be 99.8%.