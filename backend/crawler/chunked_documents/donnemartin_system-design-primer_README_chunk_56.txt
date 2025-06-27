Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
Overall availability increases when two components with availability < 100% are in parallel:  
```
Availability (Total) = 1 - (1 - Availability (Foo)) * (1 - Availability (Bar))
```  
If both `Foo` and `Bar` each had 99.9% availability, their total availability in parallel would be 99.9999%.