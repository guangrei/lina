with this starter you can:

- send contexts from  `bot.reply` 
```python
mycontext = {"Foo":"bar"}
bot.reply("localuser", msg, context=mycontext)
```
- invoke  `extensions`.

- etc.

### usage

clone/fork this repo > add/edit anything except  `core files`  > install dependency > run!

### core files

-  **Arjawinangun.py**: logic less template engine/mustache implement forked from https://github.com/lotabout/pymustache
(redesigned to work with dynamic extension system)

-  **Lina.py**: rivescript interpreter extends https://github.com/aichaos/rivescript-python

have issues or question? feel free to open issues ??