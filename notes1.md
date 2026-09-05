# Python Basics

## 1. Data Types

### Definition

A **data type** tells Python what kind of value a variable contains.

Python has several built-in data types.

### Common Python Data Types

| Data Type | Description                           | Example             |
| --------- | ------------------------------------- | ------------------- |
| `int`     | Whole numbers                         | `10`, `-5`, `100`   |
| `float`   | Decimal numbers                       | `10.5`, `3.14`      |
| `str`     | Text/string                           | `"Hello"`           |
| `bool`    | True or False                         | `True`, `False`     |
| `list`    | Collection of values                  | `[1, 2, 3]`         |
| `tuple`   | Ordered, immutable collection         | `(1, 2, 3)`         |
| `set`     | Unordered collection of unique values | `{1, 2, 3}`         |
| `dict`    | Key-value pairs                       | `{"name": "Rahul"}` |

### Examples

```python
# Integer
age = 20
print(age)
print(type(age))

# Float
price = 99.50
print(price)
print(type(price))

# String
name = "Rahul"
print(name)
print(type(name))

# Boolean
is_student = True
print(is_student)
print(type(is_student))

# List
numbers = [10, 20, 30]
print(numbers)
print(type(numbers))

# Tuple
marks = (80, 90, 85)
print(marks)
print(type(marks))

# Set
colors = {"red", "blue", "green"}
print(colors)
print(type(colors))

# Dictionary
student = {
    "name": "Rahul",
    "age": 20
}

print(student)
print(type(student))
```

---

# 2. Variables

## Definition

A **variable** is a name used to store a value in a program.

Python does not require us to specify the data type while creating a variable.

### Syntax

```python
variable_name = value
```

### Examples

```python
name = "Rahul"
age = 20
height = 5.8
is_student = True

print(name)
print(age)
print(height)
print(is_student)
```

### Multiple Variables

```python
name, age, city = "Rahul", 20, "Jabalpur"

print(name)
print(age)
print(city)
```

### Changing a Variable

A variable's value can be changed.

```python
age = 20
print(age)

age = 21
print(age)
```

Output:

```text
20
21
```

### Variable Naming Rules

Valid variable names:

```python
name = "Rahul"
student_age = 20
marks1 = 90
_my_variable = 10
```

Invalid variable names:

```python
# 1name = "Rahul"       # Cannot start with a number
# student-age = 20     # Hyphen is not allowed
# class = 10           # Python keyword cannot be used
```

### Good Naming Practice

Use meaningful variable names:

```python
student_name = "Rahul"
student_age = 20
student_marks = 85
```

Instead of:

```python
x = "Rahul"
a = 20
m = 85
```

---

# 3. `input()`

## Definition

The `input()` function is used to take input from the user.

### Syntax

```python
input("message")
```

### Example

```python
name = input("Enter your name: ")

print("Hello", name)
```

Example output:

```text
Enter your name: Rahul
Hello Rahul
```

## Important Point

The `input()` function **always returns a string**.

For example:

```python
age = input("Enter your age: ")

print(age)
print(type(age))
```

If the user enters:

```text
20
```

The type will still be:

```text
<class 'str'>
```

---

# 4. Taking Numbers as Input

Since `input()` returns a string, we need **type casting** to convert it into a number.

### Integer Input

```python
age = int(input("Enter your age: "))

print(age)
print(type(age))
```

### Float Input

```python
price = float(input("Enter price: "))

print(price)
print(type(price))
```

### Example: Add Two Numbers

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 + num2

print("Sum =", result)
```

---

# 5. Type Casting

## Definition

**Type casting** means converting one data type into another data type.

Python provides functions such as:

```python
int()
float()
str()
bool()
```

---

## `int()`

Converts a value into an integer.

```python
x = "10"

y = int(x)

print(y)
print(type(y))
```

Output:

```text
10
<class 'int'>
```

Another example:

```python
x = 10.8

y = int(x)

print(y)
```

Output:

```text
10
```

The decimal portion is removed.

---

## `float()`

Converts a value into a floating-point number.

```python
x = "10.5"

y = float(x)

print(y)
print(type(y))
```

Output:

```text
10.5
<class 'float'>
```

---

## `str()`

Converts a value into a string.

```python
age = 20

age_text = str(age)

print(age_text)
print(type(age_text))
```

---

## `bool()`

Converts a value into a Boolean value.

```python
print(bool(1))
print(bool(0))
```

Output:

```text
True
False
```

Some examples:

```python
print(bool("Hello"))  # True
print(bool(""))       # False
print(bool(10))       # True
print(bool(0))        # False
```

---

# 6. Combining Input and Type Casting

### Example 1: Student Information

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

print("Name:", name)
print("Age:", age)
print("Marks:", marks)
```

### Example 2: Calculate Area of Rectangle

```python
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area =", area)
```

### Example 3: Calculate Average

```python
marks1 = float(input("Enter marks 1: "))
marks2 = float(input("Enter marks 2: "))
marks3 = float(input("Enter marks 3: "))

average = (marks1 + marks2 + marks3) / 3

print("Average =", average)
```

---

# 7. Practice Problems

## Problem 1: Personal Information

Take the following input from the user:

* Name
* Age
* City

Print all the information.

### Solution

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print("Name:", name)
print("Age:", age)
print("City:", city)
```

---

## Problem 2: Add Two Numbers

Take two integers from the user and print their sum.

### Solution

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2

print("Sum =", sum)
```

---

## Problem 3: Basic Calculator

Take two numbers and print:

* Addition
* Subtraction
* Multiplication
* Division

### Solution

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)
```

---

## Problem 4: Area of a Circle

Take the radius from the user and calculate the area.

Formula:

```text
Area = π × radius²
```

### Solution

```python
radius = float(input("Enter radius: "))

area = 3.14 * radius * radius

print("Area of circle =", area)
```

---

## Problem 5: Convert Celsius to Fahrenheit

Formula:

```text
Fahrenheit = (Celsius × 9/5) + 32
```

### Solution

```python
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit =", fahrenheit)
```

---

## Problem 6: Calculate Simple Interest

Formula:

```text
Simple Interest = (P × R × T) / 100
```

Where:

* `P` = Principal
* `R` = Rate
* `T` = Time

### Solution

```python
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

si = (p * r * t) / 100

print("Simple Interest =", si)
```

---

## Problem 7: Swap Two Variables

Take two numbers and swap their values.

### Solution

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))

a, b = b, a

print("a =", a)
print("b =", b)
```

---

## Problem 8: Convert Minutes into Hours

Take minutes as input and convert them into hours and remaining minutes.

### Solution

```python
minutes = int(input("Enter minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print("Hours =", hours)
print("Remaining minutes =", remaining_minutes)
```

---

# 8. Quick Revision

### Data Type

Defines what kind of value is stored.

```python
age = 20
```

Here, `age` is an `int`.

### Variable

A name used to store a value.

```python
name = "Rahul"
```

### `input()`

Takes input from the user.

```python
name = input("Enter name: ")
```

Remember: `input()` returns a **string**.

### Type Casting

Converts one data type into another.

```python
age = int(input("Enter age: "))
```

Common functions:

```python
int()
float()
str()
bool()
```

---

# 9. Mini Practice Set

Try solving these without looking at the solutions:

1. Take two numbers and find their product.
2. Take a student's name and five subject marks and calculate the total.
3. Take length and breadth and calculate the perimeter of a rectangle.
4. Take a number and calculate its square and cube.
5. Convert kilometers into meters.
6. Convert rupees into paise.
7. Take a person's age and calculate their age after 10 years.
8. Take three numbers and calculate their average.
9. Take the side of a square and calculate its area and perimeter.
10. Take a number as a string, convert it to an integer, and print its type.

---

# 10. One Complete Example

```python
# Student Marks Calculator

name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))

total = maths + science + english
average = total / 3

print("\n--- Student Report ---")
print("Name:", name)
print("Total Marks:", total)
print("Average:", average)
```

This example combines:

* Variables
* `input()`
* Strings
* Integers/Floats
* Type casting
* Arithmetic operators
* `print()`
