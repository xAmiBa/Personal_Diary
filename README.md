
# Diary and Task Manager

This Python program allows users to manage their diary entries and tasks in a convenient and organized manner. It employs classes, inheritance, and integration to achieve its functionalities.

## Table of Contents

- [Overview](#overview)
- [What I Learned](#what-i-learned)
- [Features](#features)
- [Usage](#usage)
- [Classes and Structure](#classes-and-structure)
- [Testing](#testing)
- [Contributing](#contributing)

## What I Learned

In the process of developing this program, I gained valuable experience and knowledge in the following areas:

- Working with object-oriented programming (OOP) concepts in Python, including classes, inheritance, and encapsulation.
- Integrating classes to build a cohesive and functional program.
- Implementing a simple command-line interface to interact with the program.
- Utilizing test-driven development (TDD) to ensure the correctness and robustness of the code.
- Applying error handling techniques to improve the program's reliability and user experience.

This project has enhanced my understanding of Python and OOP principles, enabling me to create more efficient and structured applications in the future.


## Overview

This program provides a simple command-line interface for users to interact with a diary and a task manager. Users can add diary entries, view them based on reading speed and available time, manage tasks, and view contacts mentioned in the diary entries.

## Features

- View diary entries
- Add new diary entries
- Read diary entries based on reading speed and available time
- View tasks (all, completed, incompleted)
- Add new tasks
- View contacts mentioned in diary entries

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your_username/diary-and-task-manager.git
cd diary-and-task-manager
```

2. Run the program:

```bash
python main.py
```

Follow the on-screen instructions to interact with the diary and task manager.

## Classes and Structure

The program is structured using the following classes:

- `Diary`: Manages diary entries and integrates with `TaskList` for task management.
- `DiaryEntry`: Represents a diary entry and provides functionality to format, count words, and calculate reading time.
- `TaskList`: Manages tasks using `TaskUnit` objects.
- `TaskUnit`: Represents a task with due date and completion status.

The classes use inheritance and encapsulation to achieve modularity and reusability.

## Testing

Unit tests for the classes can be found in the `tests` directory. To run the tests, use the following command:

```bash
pytest
```

Ensure you have `pytest` installed. If not, install it using `pip install pytest`.