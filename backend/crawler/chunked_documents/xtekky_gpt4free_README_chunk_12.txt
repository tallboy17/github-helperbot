Repository: xtekky/gpt4free
Language: Python
Stars: 64472
Forks: 13656
-----
```python
from g4f.client import Client

client = Client()
response = client.images.generate(
model="flux",
prompt="a white siamese cat",
response_format="url"
)

print(f"Generated image URL: {response.data[0].url}")
```
[![Image with cat](https://g4f.dev/docs/images/cat.jpeg)](https://github.com/gpt4free/g4f.dev/blob/main/docs/client.md)