import os
from nicegui import ui

# Minimal NiceGUI hello world
ui.label('Hello, NiceGUI!')

# Bind to 0.0.0.0 and respect PORT env var for container deployment
PORT = int(os.environ.get('PORT', 8080))

# Use a multiprocessing-safe main guard so NiceGUI can start correctly
# (when multiprocessing spawns worker processes, __name__ can be "__mp_main__").
if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title='Hello World', port=PORT, host='0.0.0.0')
