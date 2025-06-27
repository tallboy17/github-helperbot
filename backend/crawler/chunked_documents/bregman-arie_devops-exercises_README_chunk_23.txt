Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>Explain Glance in detail</summary><br><b>  
* Glance is the OpenStack image service
* It handles requests related to instances disks and images
* Glance also used for creating snapshots for quick instances backups
* Users can use Glance to create new images or upload existing ones
</b></details>  
<details>
<summary>Describe Glance architecture</summary><br><b>  
* glance-api - responsible for handling image API calls such as retrieval and storage. It consists of two APIs: 1. registry-api - responsible for internal requests 2. user API - can be accessed publicly
* glance-registry - responsible for handling image metadata requests (e.g. size, type, etc). This component is private which means it's not available publicly
* metadata definition service - API for custom metadata
* database - for storing images metadata
* image repository - for storing images. This can be a filesystem, swift object storage, HTTP, etc.
</b></details>