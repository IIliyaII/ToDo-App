# GUI Todo List

A simple desktop Todo List application built with Python and FreeSimpleGUI.

## Features

* Add new tasks
* Edit existing tasks
* Delete tasks
* Save tasks automatically in a CSV file
* Simple graphical user interface
* Welcome and goodbye sound effects
* Standalone Windows executable available in the `dist` folder

---

## Project Structure

### main.py

Frontend of the application and graphical user interface.

### Backend.py

Handles task management operations such as:

* Creating tasks
* Editing tasks
* Deleting tasks
* Saving and loading task data

### csvwr.py

Responsible for reading and writing task data to CSV files.

### welcomesound.py

Handles welcome and goodbye sound playback.

---

## Technologies Used

* Python
* FreeSimpleGUI
* Pygame
* CSV
* OS
* Time

---

## Required Python Modules

```python
import welcomesound
import os
import csv
import FreeSimpleGUI as gui
import Backend
import pygame
import time
```

Install external dependencies:

```bash
pip install FreeSimpleGUI pygame
```

---

## Running From Source

```bash
python main.py
```

---

## Data Storage

Tasks are stored in a CSV file and are automatically loaded when the application starts.

---

## Author

Personal project created for learning Python GUI development, file management, and modular application design.
