Repository: ytdl-org/youtube-dl
Language: Python
Stars: 136117
Forks: 10373
-----
That's actually the output from your shell. Since ampersand is one of the special shell characters it's interpreted by the shell preventing you from passing the whole URL to youtube-dl. To disable your shell from interpreting the ampersands (or any other special characters) you have to either put the whole URL in quotes or escape them with a backslash (which approach will work depends on your shell).  
For example if your URL is https://www.youtube.com/watch?t=4&v=BaW_jenozKc you should end up with following command:  
```youtube-dl 'https://www.youtube.com/watch?t=4&v=BaW_jenozKc'```  
or  
```youtube-dl https://www.youtube.com/watch?t=4\&v=BaW_jenozKc```  
For Windows you have to use the double quotes:  
```youtube-dl "https://www.youtube.com/watch?t=4&v=BaW_jenozKc"```