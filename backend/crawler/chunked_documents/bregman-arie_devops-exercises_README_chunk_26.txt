Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>Can you describe the following concepts in regards to Keystone?  
- Role
- Tenant/Project
- Service
- Endpoint
- Token
</summary><br><b>  
- Role - A list of rights and privileges determining what a user or a project can perform
- Tenant/Project - Logical representation of a group of resources isolated from other groups of resources. It can be an account, organization, ...
- Service - An endpoint which the user can use for accessing different resources
- Endpoint - a network address which can be used to access a certain OpenStack service
- Token - Used for access resources while describing which resources can be accessed by using a scope
</b></details>  
<details>
<summary>What are the properties of a service? In other words, how a service is identified?</summary><br><b>  
Using:
- Name
- ID number
- Type
- Description
</b></details>  
<details>
<summary>Explain the following:
- PublicURL
- InternalURL
- AdminURL</summary><br><b>  
- PublicURL - Publicly accessible through public internet
- InternalURL - Used for communication between services
- AdminURL - Used for administrative management
</b></details>  
<details>
<summary>What is a service catalog?</summary><br><b>  
A list of services and their endpoints
</b></details>