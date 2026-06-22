# GUI Todo List

A desktop Todo List application built with Python and FreeSimpleGUI.

The application allows users to create, edit, delete, and manage tasks through a simple graphical interface. Tasks are automatically stored in a CSV file and restored when the application starts.

## Features

* Add new tasks
* Edit existing tasks
* Delete tasks
* Automatic CSV data storage
* Graphical user interface
* Welcome and goodbye sound effects
* Standalone Windows executable included

## Project Structure

### main.py

Frontend and graphical user interface.

### Backend.py

Handles task management logic:

* Create tasks
* Edit tasks
* Delete tasks
* Save and load task data

### csvwr.py

Handles CSV file reading and writing operations.

### welcomesound.py

Plays welcome and exit sound effects.

## Technologies Used

* Python
* FreeSimpleGUI
* Pygame
* CSV
* OS
* Time

## Installation

Install required packages:

```bash
pip install FreeSimpleGUI pygame
```

## Run From Source

```bash
python main.py
```

## Windows Executable

The precompiled executable is available in:

```text
dist/
```

No Python installation is required to run the executable version.

## Data Storage

Task data is stored in CSV format and automatically loaded when the application starts.

## Screenshots

Add screenshots of the application here.

## License

This project is released for educational and personal use.

## Author

Developed as a personal project for learning:

* GUI development
* Modular programming
* CSV file management
* Python application packaging

Screenshot of App
<img width="648" height="469" alt="image" src="https://github.com/user-attachments/assets/84c8348d-9055-4c18-951c-362d9fc57aa2" />

