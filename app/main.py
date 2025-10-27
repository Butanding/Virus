from nicegui import ui

# Minimal NiceGUI hello world
ui.label('Hello, NiceGUI!')

# Use a multiprocessing-safe main guard so NiceGUI can start correctly
# (when multiprocessing spawns worker processes, __name__ can be "__mp_main__").
if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title='Hello World', port=8080)
