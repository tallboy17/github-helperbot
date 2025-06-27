Repository: Textualize/rich
Language: Python
Stars: 52460
Forks: 1845
-----
Rich contains a number of builtin _renderables_ you can use to create elegant output in your CLI and help you debug your code.  
Click the following headings for details:  
<details>
<summary>Log</summary>  
The Console object has a `log()` method which has a similar interface to `print()`, but also renders a column for the current time and the file and line which made the call. By default Rich will do syntax highlighting for Python structures and for repr strings. If you log a collection (i.e. a dict or a list) Rich will pretty print it so that it fits in the available space. Here's an example of some of these features.  
```python
from rich.console import Console
console = Console()

test_data = [
{"jsonrpc": "2.0", "method": "sum", "params": [None, 1, 2, 4, False, True], "id": "1",},
{"jsonrpc": "2.0", "method": "notify_hello", "params": [7]},
{"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": "2"},
]

def test_log():
enabled = False
context = {
"foo": "bar",
}
movies = ["Deadpool", "Rise of the Skywalker"]
console.log("Hello from", console, "!")
console.log(test_data, log_locals=True)


test_log()
```  
The above produces the following output:  
![Log](https://github.com/textualize/rich/raw/master/imgs/log.png)  
Note the `log_locals` argument, which outputs a table containing the local variables where the log method was called.  
The log method could be used for logging to the terminal for long running applications such as servers, but is also a very nice debugging aid.  
</details>
<details>
<summary>Logging Handler</summary>  
You can also use the builtin [Handler class](https://rich.readthedocs.io/en/latest/logging.html) to format and colorize output from Python's logging module. Here's an example of the output:  
![Logging](https://github.com/textualize/rich/raw/master/imgs/logging.png)  
</details>  
<details>
<summary>Emoji</summary>  
To insert an emoji in to console output place the name between two colons. Here's an example:  
```python
>>> console.print(":smiley: :vampire: :pile_of_poo: :thumbs_up: :raccoon:")
😃 🧛 💩 👍 🦝
```  
Please use this feature wisely.  
</details>  
<details>
<summary>Tables</summary>  
Rich can render flexible [tables](https://rich.readthedocs.io/en/latest/tables.html) with unicode box characters. There is a large variety of formatting options for borders, styles, cell alignment etc.  
![table movie](https://github.com/textualize/rich/raw/master/imgs/table_movie.gif)  
The animation above was generated with [table_movie.py](https://github.com/textualize/rich/blob/master/examples/table_movie.py) in the examples directory.  
Here's a simpler table example:  
```python
from rich.console import Console
from rich.table import Table

console = Console()

table = Table(show_header=True, header_style="bold magenta")
table.add_column("Date", style="dim", width=12)
table.add_column("Title")
table.add_column("Production Budget", justify="right")
table.add_column("Box Office", justify="right")
table.add_row(
"Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$275,000,000", "$375,126,118"
)
table.add_row(
"May 25, 2018",
"[red]Solo[/red]: A Star Wars Story",
"$275,000,000",
"$393,151,347",
)
table.add_row(
"Dec 15, 2017",
"Star Wars Ep. VIII: The Last Jedi",
"$262,000,000",
"[bold]$1,332,539,889[/bold]",
)

console.print(table)
```  
This produces the following output:  
![table](https://github.com/textualize/rich/raw/master/imgs/table.png)  
Note that console markup is rendered in the same way as `print()` and `log()`. In fact, anything that is renderable by Rich may be included in the headers / rows (even other tables).  
The `Table` class is smart enough to resize columns to fit the available width of the terminal, wrapping text as required. Here's the same example, with the terminal made smaller than the table above:  
![table2](https://github.com/textualize/rich/raw/master/imgs/table2.png)  
</details>  
<details>
<summary>Progress Bars</summary>  
Rich can render multiple flicker-free [progress](https://rich.readthedocs.io/en/latest/progress.html) bars to track long-running tasks.  
For basic usage, wrap any sequence in the `track` function and iterate over the result. Here's an example:  
```python
from rich.progress import track

for step in track(range(100)):
do_step(step)
```  
It's not much harder to add multiple progress bars. Here's an example taken from the docs:  
![progress](https://github.com/textualize/rich/raw/master/imgs/progress.gif)  
The columns may be configured to show any details you want. Built-in columns include percentage complete, file size, file speed, and time remaining. Here's another example showing a download in progress:  
![progress](https://github.com/textualize/rich/raw/master/imgs/downloader.gif)  
To try this out yourself, see [examples/downloader.py](https://github.com/textualize/rich/blob/master/examples/downloader.py) which can download multiple URLs simultaneously while displaying progress.  
</details>  
<details>
<summary>Status</summary>  
For situations where it is hard to calculate progress, you can use the [status](https://rich.readthedocs.io/en/latest/reference/console.html#rich.console.Console.status) method which will display a 'spinner' animation and message. The animation won't prevent you from using the console as normal. Here's an example:  
```python
from time import sleep
from rich.console import Console

console = Console()
tasks = [f"task {n}" for n in range(1, 11)]

with console.status("[bold green]Working on tasks...") as status:
while tasks:
task = tasks.pop(0)
sleep(1)
console.log(f"{task} complete")
```  
This generates the following output in the terminal.  
![status](https://github.com/textualize/rich/raw/master/imgs/status.gif)  
The spinner animations were borrowed from [cli-spinners](https://www.npmjs.com/package/cli-spinners). You can select a spinner by specifying the `spinner` parameter. Run the following command to see the available values:  
```
python -m rich.spinner
```  
The above command generates the following output in the terminal:  
![spinners](https://github.com/textualize/rich/raw/master/imgs/spinners.gif)  
</details>  
<details>
<summary>Tree</summary>  
Rich can render a [tree](https://rich.readthedocs.io/en/latest/tree.html) with guide lines. A tree is ideal for displaying a file structure, or any other hierarchical data.  
The labels of the tree can be simple text or anything else Rich can render. Run the following for a demonstration:  
```
python -m rich.tree
```  
This generates the following output:  
![markdown](https://github.com/textualize/rich/raw/master/imgs/tree.png)  
See the [tree.py](https://github.com/textualize/rich/blob/master/examples/tree.py) example for a script that displays a tree view of any directory, similar to the linux `tree` command.  
</details>  
<details>
<summary>Columns</summary>  
Rich can render content in neat [columns](https://rich.readthedocs.io/en/latest/columns.html) with equal or optimal width. Here's a very basic clone of the (MacOS / Linux) `ls` command which displays a directory listing in columns:  
```python
import os
import sys

from rich import print
from rich.columns import Columns

directory = os.listdir(sys.argv[1])
print(Columns(directory))
```  
The following screenshot is the output from the [columns example](https://github.com/textualize/rich/blob/master/examples/columns.py) which displays data pulled from an API in columns:  
![columns](https://github.com/textualize/rich/raw/master/imgs/columns.png)  
</details>  
<details>
<summary>Markdown</summary>  
Rich can render [markdown](https://rich.readthedocs.io/en/latest/markdown.html) and does a reasonable job of translating the formatting to the terminal.  
To render markdown import the `Markdown` class and construct it with a string containing markdown code. Then print it to the console. Here's an example:  
```python
from rich.console import Console
from rich.markdown import Markdown

console = Console()
with open("README.md") as readme:
markdown = Markdown(readme.read())
console.print(markdown)
```  
This will produce output something like the following:  
![markdown](https://github.com/textualize/rich/raw/master/imgs/markdown.png)  
</details>  
<details>
<summary>Syntax Highlighting</summary>  
Rich uses the [pygments](https://pygments.org/) library to implement [syntax highlighting](https://rich.readthedocs.io/en/latest/syntax.html). Usage is similar to rendering markdown; construct a `Syntax` object and print it to the console. Here's an example:  
```python
from rich.console import Console
from rich.syntax import Syntax

my_code = '''
def iter_first_last(values: Iterable[T]) -> Iterable[Tuple[bool, bool, T]]:
"""Iterate and generate a tuple with a flag for first and last value."""
iter_values = iter(values)
try:
previous_value = next(iter_values)
except StopIteration:
return
first = True
for value in iter_values:
yield first, False, previous_value
first = False
previous_value = value
yield first, True, previous_value
'''
syntax = Syntax(my_code, "python", theme="monokai", line_numbers=True)
console = Console()
console.print(syntax)
```  
This will produce the following output:  
![syntax](https://github.com/textualize/rich/raw/master/imgs/syntax.png)  
</details>  
<details>
<summary>Tracebacks</summary>  
Rich can render [beautiful tracebacks](https://rich.readthedocs.io/en/latest/traceback.html) which are easier to read and show more code than standard Python tracebacks. You can set Rich as the default traceback handler so all uncaught exceptions will be rendered by Rich.  
Here's what it looks like on OSX (similar on Linux):  
![traceback](https://github.com/textualize/rich/raw/master/imgs/traceback.png)  
</details>  
All Rich renderables make use of the [Console Protocol](https://rich.readthedocs.io/en/latest/protocol.html), which you can also use to implement your own Rich content.