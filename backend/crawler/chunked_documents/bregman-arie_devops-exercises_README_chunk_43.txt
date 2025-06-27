Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>What is YAML?</summary><br><b>  
Data serialization language used by many technologies today like Kubernetes, Ansible, etc.
</b></details>  
<details>
<summary>True or False? Any valid JSON file is also a valid YAML file</summary><br><b>  
True. Because YAML is superset of JSON.
</b></details>  
<details>
<summary>What is the format of the following data?  
```
{
applications: [
{
name: "my_app",
language: "python",
version: 20.17
}
]
}
```
</summary><br><b>
JSON
</b></details>  
<details>
<summary>What is the format of the following data?  
```
applications:
- app: "my_app"
language: "python"
version: 20.17
```
</summary><br><b>
YAML
</b></details>  
<details>
<summary>How to write a multi-line string with YAML? What use cases is it good for?</summary><br><b>  
```
someMultiLineString: |
look mama
I can write a multi-line string
I love YAML
```  
It's good for use cases like writing a shell script where each line of the script is a different command.
</b></details>  
<details>
<summary>What is the difference between <code>someMultiLineString: |</code> to <code>someMultiLineString: ></code>?</summary><br><b>  
using `>` will make the multi-line string to fold into a single line  
```
someMultiLineString: >
This is actually
a single line
do not let appearances fool you
```
</b></details>  
<details>
<summary>What are placeholders in YAML?</summary><br><b>  
They allow you reference values instead of directly writing them and it is used like this:  
```
username: {{ my.user_name }}
```
</b></details>  
<details>
<summary>How can you define multiple YAML components in one file?</summary><br><b>  
Using this: `---`
For Examples:  
```
document_number: 1
---
document_number: 2
```
</b></details>