Repository: gradio-app/gradio
Language: Python
Stars: 38656
Forks: 2952
-----
What good is a beautiful demo if you can't share it? Gradio lets you easily share a machine learning demo without having to worry about the hassle of hosting on a web server. Simply set `share=True` in `launch()`, and a publicly accessible URL will be created for your demo. Let's revisit our example demo,  but change the last line as follows:  
```python
import gradio as gr

def greet(name):
return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="textbox", outputs="textbox")

demo.launch(share=True)  # Share your demo with just 1 extra parameter 🚀
```  
When you run this code, a public URL will be generated for your demo in a matter of seconds, something like:  
👉 &nbsp; `https://a23dsf231adb.gradio.live`  
Now, anyone around the world can try your Gradio demo from their browser, while the machine learning model and all computation continues to run locally on your computer.  
To learn more about sharing your demo, read our dedicated guide on [sharing your Gradio application](https://www.gradio.app/guides/sharing-your-app).