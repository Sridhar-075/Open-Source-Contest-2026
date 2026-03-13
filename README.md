# File Manager Application (Virtual File System)

# Overview

This project is a **command-line based File Manager Application** that simulates a file system hierarchy in memory.
Users can create, organize, view, rename, copy, move and delete files and folders without interacting with the real operating system file system.

The application follows a **tree-based data structure** to represent directories and files and provides a shell-like interface for user interaction.

---

# Folder Structure

```
OSW-CS00B0000
│
├── index.py        # Main application containing File Manager logic
├── README.md       # Project documentation
├── LICENSE
└── .gitignore
```

---

# Language Used

* **Python 3**
* Standard Libraries:

  * `time` → for file/folder creation timestamp
  * `random` → for assigning random file size

No external frameworks or third-party libraries are used.

---

# Features Implemented

# Folder Operations

* Create one or more folders in current directory

  ```
  app folders <name1> <name2>
  ```
* Create nested folders

  ```
  app folders <parent>, <child1> <child2>
  ```
* Navigate between directories

  ```
  app cd <folder>
  app cd ..
  ```
* Show directory tree representation

  ```
  app represent
  ```

# File Operations

* Create one or more files

  ```
  app files <name1> <name2>
  ```
* Display file metadata (creation date and size)

  ```
  app info <file>
  ```

# Directory Management

* List contents of current directory

  ```
  app list
  ```
* Show current working directory

  ```
  app pwd
  ```

 File System Modification

* Delete files or folders

  ```
  app delete <name>
  ```
* Rename files or folders

  ```
  app rename <old_name> <new_name>
  ```
* Copy files/folders using relative or absolute path

  ```
  app copy <source_path> <destination_path>
  ```
* Move files/folders

  ```
  app move <source_path> <destination_path>
  ```

 Tree Visualization

Displays hierarchical structure of the virtual file system similar to Linux `tree` command.

---

 Dependencies

This project uses only **Python standard library modules**:

* Python 3.x installed
* No additional packages required

---

## 🔧 How to Build / Setup

1. Clone the repository:

```
git clone <repository_url>
```

2. Navigate to project folder:

```
cd OSW-CS00B0000
```

3. Run the program:

```
python index.py
```

---

 How to Use

The application runs in an interactive command loop.

All commands must start with:

```
app
```

Example usage:

```
app folders docs
app cd docs
app files notes.txt
app pwd
app list
app represent
app rename notes.txt ideas.txt
app delete ideas.txt
```

To exit the application:

```
exit
```

---

 Design Approach

* File system is represented as a **Tree Data Structure**
* Each element is a **Node** with:

  * name
  * parent reference
* Folders maintain a dictionary of children for fast lookup
* Path resolution supports:

  * relative paths (`..`, `.`)
  * absolute paths (`/root/docs/file`)
* Commands are parsed and executed using a central **App controller class**

---



---

 License

This project is licensed under the MIT License.

---
