# Astro Command

Astro component for static rendering of commands. This allows you build components in any language.

[Demo](https://github.com/trashhalo/astro-command/blob/main/src/components/Demo.astro)

## Usage

```astro
---
import { Command } from "astro-command";
---
<Command caller={import.meta.url} command="Component.py" message="from python!" />
```
Component.py
```python
#!/usr/bin/env python 

import sys, json

data = json.load(sys.stdin)
print(f'<h1> Hello {data["message"]} </h1>')
```

* caller: url of the caller so we can use it to look up relative paths
* command: name of the command to execute. relative path from the caller
* props: all props are passed to command as json via stdin
* html: generated html sent out via stdout embedded
