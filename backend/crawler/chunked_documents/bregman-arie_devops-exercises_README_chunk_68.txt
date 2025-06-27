Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>What is Packer? What is it used for?</summary><br><b>  
In general, Packer automates machine images creation.
It allows you to focus on configuration prior to deployment while making the images. This allows you start the instances much faster in most cases.
</b></details>  
<details>
<summary>Packer follows a "configuration->deployment" model or "deployment->configuration"?</summary><br><b>  
A configuration->deployment which has some advantages like:  
1. Deployment Speed - you configure once prior to deployment instead of configuring every time you deploy. This allows you to start instances/services much quicker.
2. More immutable infrastructure - with configuration->deployment it's not likely to have very different deployments since most of the configuration is done prior to the deployment. Issues like dependencies errors are handled/discovered prior to deployment in this model.
</b></details>