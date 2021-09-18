#!/usr/bin/env python 

import sys, json

data = json.load(sys.stdin)
print(f'<h1> Hello {data["message"]} </h1>')