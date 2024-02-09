# Task Management System

The Task Management System this project provides a simple and efficient solution for managing tasks effectively. Whether you're an individual looking to stay organized or part of a team collaborating on multiple projects, this system offers the tools you need to streamline your workflow.


## Task Class

The `Task` class represents a task with attributes such as `title`, `description`, and `category`. It provides a string representation of the task using the `__str__` method.

## Utility Functions

### `edit_task(task, new_title=None, new_description=None, new_category=None)`

This function is used to edit the properties of a given task. It takes a task object and optional new values for `title`, `description`, and `category`, and updates the task accordingly.

### `create_task(title, description, category=None)`

This function creates a new task object with the provided `title`, `description`, and optional `category`, and returns it.

### `categorize_task(task, new_category)`

This function is used to change the category of a given task to a new category.

## Usage

To use the Task Management System:

1. Import the `Task` class and utility functions into your project.
2. Create tasks using the `create_task` function, providing the `title`, `description`, and optional `category`.
3. Edit task properties using the `edit_task` function as needed.
4. Categorize tasks using the `categorize_task` function.
5. Use the `__str__` method of the `Task` class to display task details.

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or feature requests, please open an issue or submit a pull request. Let's work together to improve the Task Management System.


