#!/usr/bin/env python3
"""
NiceGUI Hello World Example
A simple web application demonstrating NiceGUI framework.
"""

from nicegui import ui


@ui.page('/')
def index():
    """Main page with hello world content."""
    ui.label('Hello World!').classes('text-h2')
    ui.label('Welcome to NiceGUI - A Python Web Framework').classes('text-subtitle1')
    
    with ui.card().classes('w-full max-w-md'):
        ui.label('This is a simple example application')
        ui.button('Click me!', on_click=lambda: ui.notify('Hello from NiceGUI!'))


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(host='0.0.0.0', port=8080, reload=False, show=False)
