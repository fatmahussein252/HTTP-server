#!/usr/bin/env python3
import os
import platform
import cgi
import cgitb

response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body><ul>"

# Function to generate an HTML page
def generate_html(title, body):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>{title}</title>
    </head>
    <body style="font-family: Arial, sans-serif;">
        {body}
    </body>
    </html>
    """

# Parse query string
query_string = os.environ.get('QUERY_STRING') # Default to 'Guest' if no name provided
if query_string == "": 
	name = "Guest"
else: 
	name = query_string.split('=')[1] 

if name.lower() == "info":  # Special command to display system info
    body_content = f"""
    <h1>System Information</h1>
    <p><strong>OS:</strong> {platform.system()} {platform.release()}</p>
    <p><strong>Python Version:</strong> {platform.python_version()}</p>
    <p><strong>Architecture:</strong> {platform.architecture()[0]}</p>
    <p><strong>Hostname:</strong> {platform.node()}</p>
    <a href="/cgi-bin/info.py">Back</a>
    """
else:  # Greet the user
    body_content = f"""
    <h1>Hello, {name}!</h1>
    <p>Welcome to my CGI script demo.</p>
    <p>Try adding <code>?name=info</code> to the URL for system information.</p>
    <p>Example: <a href="/cgi-bin/info.py?name=info">Click Here</a></p>
    """

# Generate and print the HTML
response += generate_html("Welcome Page", body_content)
print(response)

