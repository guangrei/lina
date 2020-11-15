with this starter you can:

- use mustache template engine with  `backtrick` delimiter in  `.rive` files.
- send contexts from  `bot.reply` 
```python
mycontext = {"Foo":"bar"}
bot.reply("localuser", msg, context=mycontext)
```
- invoke  `extensions`, just write normal python package in  `extensions`  dir and call    `arg | extension `  or  `_ | extension`  (invoke without arg)  in  `.rive` files.

- etc.

### usage

clone/fork this repo > add/edit anything except  `core files`  > install dependency > run!

or with poetry:
``` 
$ poetry run python3 -u app.py
```

### core files

-  **Arjawinangun.py**: logic less template engine/mustache implement forked from https://github.com/lotabout/pymustache
(redesigned to work with dynamic extension system)

-  **Lina.py**: rivescript interpreter extends https://github.com/aichaos/rivescript-python

have issues or question? feel free to open issues.