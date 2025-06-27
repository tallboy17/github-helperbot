Repository: xtekky/gpt4free
Language: Python
Stars: 64472
Forks: 13656
-----
```python
from g4f.client import Client

client = Client()
response = client.chat.completions.create(
model="gpt-4o-mini",
messages=[{"role": "user", "content": "Hello"}],
web_search=False
)
print(response.choices[0].message.content)
```
```
Hello! How can I assist you today?
```