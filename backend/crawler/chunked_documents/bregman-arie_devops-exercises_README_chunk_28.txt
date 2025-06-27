Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>Can you describe Keystone service in detail?</summary><br><b>  
* You can't have OpenStack deployed without Keystone
* It Provides identity, policy and token services
* The authentication provided is for both users and services
* The authorization supported is token-based and user-based.
* There is a policy defined based on RBAC stored in a JSON file and each line in that file defines the level of access to apply
</b></details>  
<details>
<summary>Describe Keystone architecture</summary><br><b>  
* There is a service API and admin API through which Keystone gets requests
* Keystone has four backends:
* Token Backend - Temporary Tokens for users and services
* Policy Backend - Rules management and authorization
* Identity Backend - users and groups (either standalone DB, LDAP, ...)
* Catalog Backend - Endpoints
* It has pluggable environment where you can integrate with:
* LDAP
* KVS (Key Value Store)
* SQL
* PAM
* Memcached
</b></details>  
<details>
<summary>Describe the Keystone authentication process</summary><br><b>  
* Keystone gets a call/request and checks whether it's from an authorized user, using username, password and authURL
* Once confirmed, Keystone provides a token.
* A token contains a list of user's projects so there is no to authenticate every time and a token can submitted instead
</b></details>