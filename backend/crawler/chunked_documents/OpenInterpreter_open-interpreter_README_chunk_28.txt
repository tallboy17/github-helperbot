Repository: OpenInterpreter/open-interpreter
Language: Python
Stars: 59703
Forks: 5081
-----
The full [documentation](https://docs.openinterpreter.com/) is accessible on-the-go without the need for an internet connection.  
[Node](https://nodejs.org/en) is a pre-requisite:  
- Version 18.17.0 or any later 18.x.x version.
- Version 20.3.0 or any later 20.x.x version.
- Any version starting from 21.0.0 onwards, with no upper limit specified.  
Install [Mintlify](https://mintlify.com/):  
```bash
npm i -g mintlify@latest
```  
Change into the docs directory and run the appropriate command:  
```bash
# Assuming you're at the project's root directory
cd ./docs

# Run the documentation server
mintlify dev
```  
A new browser window should open. The documentation will be available at [http://localhost:3000](http://localhost:3000) as long as the documentation server is running.