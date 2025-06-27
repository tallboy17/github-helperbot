Repository: streamlit/streamlit
Language: Python
Stars: 39975
Forks: 3509
-----
Create a new file named `streamlit_app.py` in your project directory with the following code:
```python
import streamlit as st
x = st.slider("Select a value")
st.write(x, "squared is", x * x)
```  
Now run it to open the app!
```
$ streamlit run streamlit_app.py
```  
<img src="https://user-images.githubusercontent.com/7164864/215172915-cf087c56-e7ae-449a-83a4-b5fa0328d954.gif" width=300 alt="Little example"></img>