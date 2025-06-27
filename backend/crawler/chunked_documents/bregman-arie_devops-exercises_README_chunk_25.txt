Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>Explain Cinder in detail</summary><br><b>  
* Cinder is OpenStack Block Storage service
* It basically provides used with storage resources they can consume with other services such as Nova
* One of the most used implementations of storage supported by Cinder is LVM
* From user perspective this is transparent which means the user doesn't know where, behind the scenes, the storage is located or what type of storage is used
</b></details>  
<details>
<summary>Describe Cinder's components</summary><br><b>  
* cinder-api - receives API requests
* cinder-volume - manages attached block devices
* cinder-scheduler - responsible for storing volumes
</b></details>