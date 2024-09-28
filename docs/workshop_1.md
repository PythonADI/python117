# Workshop 1
Prerequisites:
- [Python](https://www.python.org/)
- IDE (Integrated Development Environment) or Text Editor (e.g. [Visual Studio Code](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/pycharm/), [Sublime Text](https://www.sublimetext.com/), [Atom](https://atom.io/), [Notepad++](https://notepad-plus-plus.org/))

What will you learn in this workshop?
- [How does computer work?](#how-does-computer-work)
- [What is programming?](#what-is-programming)
- [What is Python?](#what-is-python)
- [Basic Python syntax](#basic-python-syntax)
- [Variables](#variables)
- [Data types](#data-types)
- [Why data types are important?](#why-data-types-are-important)
- [Type casting](#type-casting)
- [Arithmetic and comparison operators](#arithmetic-and-comparison-operators)


## How does computer work?

### Hardware 
Hardware is the physical components of a computer. It includes:
- CPU (Central Processing Unit)
- RAM (Random Access Memory)
- Storage (HDD, SSD)
- Input/Output devices (Keyboard, Mouse, Monitor, Printer)
- Motherboard
- Power Supply
- Cooling system
- Case
- [More about computer hardware](https://en.wikipedia.org/wiki/Computer_hardware)

### Software
Software is a collection of instructions that tell the computer how to work. It includes:
- Operating System (Windows, macOS, Linux)
- Applications (Word, Excel, Chrome, etc.)
- Drivers
- [More about computer software](https://en.wikipedia.org/wiki/Software)

### How does computer work?
The computer works by executing a series of instructions. It includes:
1. The CPU fetches the instruction from the memory.
2. The CPU decodes the instruction.
3. The CPU executes the instruction.
4. Repeat the process until the program is finished.
5. The CPU sends the result to the output device.
6. The CPU waits for the next instruction.

[Detailed explanation](https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:computers/xcae6f4a7ff015e7d:computer-components/a/central-processing-unit-cpu#:~:text=The%20CPU%20is%20the%20brain,run%20programs%20on%20a%20computer.)

### What is instruction?
An instruction is a command that tells the computer what to do. It includes:
- Arithmetic operations (add, subtract, multiply, divide)
- Logical operations (AND, OR, NOT)
- Data transfer (move data from one place to another)
- Control flow (if, else, while, for)
- [More about computer instruction](https://en.wikipedia.org/wiki/Instruction_set_architecture)

### What does decoding mean?
Decoding is the process of translating the instruction into a series of signals that the CPU can understand. It includes:
- Reading the instruction from the memory.
- Identifying the operation to be performed.
- Fetching the data from the memory.
- Performing the operation.
- Storing the result back to the memory.
- [More about computer decoding](https://en.wikipedia.org/wiki/Instruction_cycle)

### What is memory?
Memory is a storage device that stores data and instructions. It includes:
- RAM (Random Access Memory)
- ROM (Read-Only Memory)
- Cache
- [More about computer memory](https://en.wikipedia.org/wiki/Computer_memory)

[Memory Hierarchy](https://runestone.academy/ns/books/published/welcomecs/ComputerArchitecture/MemoryHeirarchy.html)


## What is programming?
Programming is the process of creating a set of instructions that tell the computer how to perform a task. It includes:
- Writing code
- Testing code
- Debugging code
- [More about programming](https://en.wikipedia.org/wiki/Computer_programming)

### Why do we need programming?
- To automate repetitive tasks
- To solve complex problems
- To create software applications
- To build websites
- To develop games
- etc.

### What is code?
Code is a set of instructions written in a programming language. It includes:
- Variables
- Data types
- Operators
- Control structures
- Functions
- Classes
- etc.

### What is programming language?
A programming language is a formal language that specifies a set of instructions that can be used to produce various kinds of output. It includes:
- Python
- C/C++
- C#
- Rust
- Java
- JavaScript
- etc.

### What is Python?
Python is a high-level, interpreted, interactive, and object-oriented scripting language. It includes:
- Easy to learn
- Easy to read
- Easy to maintain
- Portable
- Extensible

### Basic Python syntax
Python syntax is the set of rules that defines how a Python program will be written and interpreted.
Syntax is like the grammar of a programming language.

Following code will print "Hello, World!" to the console.
```python
# This is a comment
print("Hello, World!")
```

### What is console?
Console is a text-based interface that allows users to interact with the computer. It includes:
- Command Prompt (Windows)
- Terminal (macOS, Linux)
- Python Shell (IDLE)
- [More about console](https://en.wikipedia.org/wiki/Computer_terminal)

### CLI vs GUI
CLI (Command Line Interface) is a text-based interface that allows users to interact with the computer using commands.

GUI (Graphical User Interface) is a visual interface that allows users to interact with the computer using graphical elements.

### Variables
Variables are used to store data in a computer program.
RAM only holds values as 8-bit binary numbers (0s and 1s).

| address | value (binary) | real value |
|---------|----------------|------------|
| 100     | 00001010       | 10         |
| 101     | 00010100       | 20         |
| 102     | 00011110       | 30         |


```python
# Assigning values to variables
a = 10 # address 100
b = 20 # address 101
c = 30 # address 102

# Printing variables
print(a)
print(b)
print(c)
```

Output:
```
10
20
30
```

### Data types
Variables should be declared with a data type in some programming languages. Python is a dynamically typed language, so you don't have to declare the data type of a variable.
However behind the scenes, Python does assign a data type to the variable. 

| Data type | Description           | Example         |
|-----------|-----------------------|-----------------|
| int       | Integer               | 10              |
| float     | Floating-point number | 10.5            |
| str       | String                | "Hello, World!" |
| bool      | Boolean               | True, False     |


RAM

| address | value (binary) | real value      | Variable |
|---------|----------------|-----------------|----------|
| 100     | 00001010       | 10              | a        |
| 101     | 00000001       | True            | d        |

floats and string are stored in a different way in memory.
and require more than 8 bits to store.
[Floating-point number representation](https://developer.arm.com/documentation/101655/0961/Cx51-User-s-Guide/Advanced-Programming/Data-Storage-Formats/Floating-point-Numbers)

Strings are stored as a sequence of characters in memory.
characters are stored as [ASCII](https://en.wikipedia.org/wiki/ASCII) values in memory.
characters are stored as 8-bit binary numbers (0s and 1s).

| address | value (binary) | real value | Variable |
|---------|----------------|------------|----------|
| 200     | 01001000       | H          | c        |
| 201     | 01100101       | e          |          |
| 202     | 01101100       | l          |          |
| 203     | 01101100       | l          |          |
| 204     | 01101111       | o          |          |
| 205     | 00101100       | ,          |          |
| 206     | 00100000       |            |          |
| 207     | 01010111       | W          |          |
| 208     | 01101111       | o          |          |
| 209     | 01110010       | r          |          |
| 210     | 01101100       | l          |          |
| 211     | 01100100       | d          |          |
| 212     | 00100001       | !          |          |


```python
# Assigning values to variables
a = 10 # int
b = 10.5 # float
c = "Hello, World!" # str
d = True # bool

# Printing variables
print(a)
print(b)
print(c)
print(d)
```

Output:
```
10
10.5
Hello, World!
True
```

### Why data types are important?
Data types are important because they tell the computer how to interpret the data stored in the memory.
As we saw in memory, the computer stores data in binary format (0s and 1s).

If we try to add an integer and a string, the computer will not be able to perform the operation because it doesn't know how to interpret the data.

```python
a = 10
b = "20"
print(a + b)
```

Output:
```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

### Type casting
Type casting is the process of converting one data type to another data type.
It allows us to perform operations on different data types.

```python
a = 10
b = "20"
print(a + int(b))
```

Output:
```
30
```

### Arithmetic and comparison operators
Operators are used to perform operations on variables and values.

```python
# Arithmetic operators
a = 10
b = 20
print('a + b =', a + b) # Addition
print('a - b =', a - b) # Subtraction
print('a * b =', a * b) # Multiplication
print('a / b =', a / b) # Division
print('a % b =', a % b) # Modulus
print('a ** b =', a ** b) # Exponentiation
print('a // b =', a // b) # Floor division

# Comparison operators
print('a == b:', a == b) # Equal
print('a != b:', a != b) # Not equal
print('a > b:', a > b) # Greater than
print('a < b:', a < b) # Less than
print('a >= b:', a >= b) # Greater than or equal to
print('a <= b:', a <= b) # Less than or equal to
```

Output:
```
a + b = 30
a - b = -10
a * b = 200
a / b = 0.5
a % b = 10
a ** b = 100000000000000000000
a // b = 0
a == b: False
a != b: True
a > b: False
a < b: True
a >= b: False
a <= b: True
```



