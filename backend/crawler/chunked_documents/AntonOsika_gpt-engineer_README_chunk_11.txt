Repository: AntonOsika/gpt-engineer
Language: Python
Stars: 54354
Forks: 7174
-----
By default, gpt-engineer expects text input via a `prompt` file. It can also accept image inputs for vision-capable models. This can be useful for adding UX or architecture diagrams as additional context for GPT Engineer. You can do this by specifying an image directory with the `—-image_directory` flag and setting a vision-capable model in the second CLI argument.  
E.g. `gpte projects/example-vision gpt-4-vision-preview --prompt_file prompt/text --image_directory prompt/images -i`