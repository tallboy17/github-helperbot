Repository: gradio-app/gradio
Language: Python
Stars: 38656
Forks: 2952
-----
You can run Gradio in your favorite code editor, Jupyter notebook, Google Colab, or anywhere else you write Python. Let's write your first Gradio app:  
```python
import gradio as gr

def greet(name, intensity):
return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
fn=greet,
inputs=["text", "slider"],
outputs=["text"],
)

demo.launch()
```  
> [!TIP]
> We shorten the imported name from <code>gradio</code> to <code>gr</code>. This is a widely adopted convention for better readability of code.  
Now, run your code. If you've written the Python code in a file named `app.py`, then you would run `python app.py` from the terminal.  
The demo below will open in a browser on [http://localhost:7860](http://localhost:7860) if running from a file. If you are running within a notebook, the demo will appear embedded within the notebook.  
![`hello_world_4` demo](demo/hello_world_4/screenshot.gif)  
Type your name in the textbox on the left, drag the slider, and then press the Submit button. You should see a friendly greeting on the right.  
> [!TIP]
> When developing locally, you can run your Gradio app in <strong>hot reload mode</strong>, which automatically reloads the Gradio app whenever you make changes to the file. To do this, simply type in <code>gradio</code> before the name of the file instead of <code>python</code>. In the example above, you would type: `gradio app.py` in your terminal. Learn more in the <a href="https://www.gradio.app/guides/developing-faster-with-reload-mode">Hot Reloading Guide</a>.  
**Understanding the `Interface` Class**  
You'll notice that in order to make your first demo, you created an instance of the `gr.Interface` class. The `Interface` class is designed to create demos for machine learning models which accept one or more inputs, and return one or more outputs.  
The `Interface` class has three core arguments:  
- `fn`: the function to wrap a user interface (UI) around
- `inputs`: the Gradio component(s) to use for the input. The number of components should match the number of arguments in your function.
- `outputs`: the Gradio component(s) to use for the output. The number of components should match the number of return values from your function.  
The `fn` argument is very flexible -- you can pass *any* Python function that you want to wrap with a UI. In the example above, we saw a relatively simple function, but the function could be anything from a music generator to a tax calculator to the prediction function of a pretrained machine learning model.  
The `inputs` and `outputs` arguments take one or more Gradio components. As we'll see, Gradio includes more than [30 built-in components](https://www.gradio.app/docs/gradio/introduction) (such as the `gr.Textbox()`, `gr.Image()`, and `gr.HTML()` components) that are designed for machine learning applications.  
> [!TIP]
> For the `inputs` and `outputs` arguments, you can pass in the name of these components as a string (`"textbox"`) or an instance of the class (`gr.Textbox()`).  
If your function accepts more than one argument, as is the case above, pass a list of input components to `inputs`, with each input component corresponding to one of the arguments of the function, in order. The same holds true if your function returns more than one value: simply pass in a list of components to `outputs`. This flexibility makes the `Interface` class a very powerful way to create demos.  
We'll dive deeper into the `gr.Interface` on our series on [building Interfaces](https://www.gradio.app/main/guides/the-interface-class).