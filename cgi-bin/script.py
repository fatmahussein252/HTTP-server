#!/usr/bin/env python3

import os
print(f"{os.environ.get('SERVER_PROTOCOL')} 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body><h1>Hello, {os.environ.get('QUERY_STRING')}!</h1></body></html>")


