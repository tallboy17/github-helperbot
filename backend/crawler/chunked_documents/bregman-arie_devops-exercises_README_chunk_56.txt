Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>Extract all the numbers</summary><br><b>  
- "\d+"
</b></details>  
<details>
<summary>Extract the first word of each line</summary><br><b>  
- "^\w+"
Bonus: extract the last word of each line  
- "\w+(?=\W*$)" (in most cases, depends on line formatting)
</b></details>  
<details>
<summary>Extract all the IP addresses</summary><br><b>  
- "\b(?:\d{1,3}\ .){3}\d{1,3}\b" IPV4:(This format looks for 1 to 3 digit sequence 3 times)
</b></details>  
<details>
<summary>Extract dates in the format of yyyy-mm-dd or yyyy-dd-mm</summary><br><b>
</b></details>  
<details>
<summary>Extract email addresses</summary><br><b>  
- "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\ .[A-Za-z]{2,}\b"
</b></details>