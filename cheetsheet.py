
name = "Mark"

if name == "Mark":
    print("Hello")

Main differences:

# No semicolons
# No curly braces
# Indentation matters
# Types are usually inferred

# 2. Variables and types

name = "Mark"       # str
age = 35            # int
active = True       # bool
price = 12.5        # float

Python common types:

str       # text
int       # whole number
float     # decimal
bool      # True / False
None      # like null
list      # like ArrayList
dict      # like HashMap
set       # unique values
tuple     # immutable ordered values

# 3. `null` vs `None`

name = None     # null

if name is None:
    print("No name")

is None
is not None

Not:
name == None  # works, but not preferred

String name = "Mark";
String message = "Hello " + name;
```

## Python

```python
name = "Mark"
message = "Hello " + name
```

Better Python style:

```python
message = f"Hello {name}"
```

Useful string methods:

```python
text = " hello world "

text.strip()        # remove whitespace
text.upper()
text.lower()
text.replace("world", "Mark")
text.startswith("hello")
text.endswith("world")
"hello" in text
```

Convert to string:

```python
age = 35
text = str(age)
```

---

# 5. Printing

## Java

```java
System.out.println("Hello");
```

## Python

```python
print("Hello")
```

With variables:

```python
name = "Mark"
print(f"Hello {name}")
```

---

# 6. If statements

## Java

```java
if (age >= 18) {
    System.out.println("Adult");
} else if (age >= 13) {
    System.out.println("Teen");
} else {
    System.out.println("Child");
}
```

## Python

```python
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")
```

Boolean operators:

| Java | Python |   |      |
| ---- | ------ | - | ---- |
| `&&` | `and`  |   |      |
| `    |        | ` | `or` |
| `!`  | `not`  |   |      |

Example:

```python
if age > 18 and active:
    print("Allowed")
```

---

# 7. Lists — like `ArrayList`

## Java

```java
List<String> names = new ArrayList<>();
names.add("Mark");
names.add("Sarah");
```

## Python

```python
names = []
names.append("Mark")
names.append("Sarah")
```

Or:

```python
names = ["Mark", "Sarah", "Tom"]
```

Useful list operations:

```python
names[0]             # first item
names[-1]            # last item
len(names)           # size
names.append("Amy")  # add
names.remove("Tom")  # remove by value
names.pop()          # remove last
"Mark" in names      # contains
```

Loop through list:

```python
for name in names:
    print(name)
```

With index:

```python
for index, name in enumerate(names):
    print(index, name)
```

---

# 8. Dictionaries — like `HashMap`

## Java

```java
Map<String, Integer> ages = new HashMap<>();
ages.put("Mark", 35);
int age = ages.get("Mark");
```

## Python

```python
ages = {
    "Mark": 35,
    "Sarah": 30
}

age = ages["Mark"]
```

Safer lookup:

```python
age = ages.get("Mark")
age = ages.get("Unknown", 0)
```

Add/update:

```python
ages["Tom"] = 40
```

Loop keys and values:

```python
for name, age in ages.items():
    print(name, age)
```

Check key exists:

```python
if "Mark" in ages:
    print("Found")
```

---

# 9. Sets — unique values

## Java

```java
Set<String> names = new HashSet<>();
names.add("Mark");
```

## Python

```python
names = {"Mark", "Sarah"}
names.add("Tom")
```

Useful:

```python
"Mark" in names
names.remove("Mark")
```

Empty set:

```python
names = set()
```

Important:

```python
{}  # empty dict, not empty set
```

---

# 10. Tuples — immutable small records

```python
point = (10, 20)

x = point[0]
y = point[1]
```

Tuple unpacking:

```python
x, y = point
```

Useful for returning multiple values:

```python
def get_name_and_age():
    return "Mark", 35

name, age = get_name_and_age()
```

---

# 11. Loops

## Java for-loop

```java
for (int i = 0; i < 10; i++) {
    System.out.println(i);
}
```

## Python

```python
for i in range(10):
    print(i)
```

Range examples:

```python
range(5)        # 0,1,2,3,4
range(1, 5)     # 1,2,3,4
range(1, 10, 2) # 1,3,5,7,9
```

While loop:

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

---

# 12. Functions

## Java

```java
public int add(int a, int b) {
    return a + b;
}
```

## Python

```python
def add(a, b):
    return a + b
```

With type hints:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Default argument:

```python
def greet(name: str = "World") -> str:
    return f"Hello {name}"
```

Call:

```python
greet("Mark")
greet()
```

---

# 13. Classes

## Java

```java
public class Person {
    private String name;

    public Person(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}
```

## Python

```python
class Person:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name
```

Use it:

```python
person = Person("Mark")
print(person.get_name())
print(person.name)
```

Important:

```python
self
```

is like Java’s:

```java
this
```

---

# 14. Dataclasses — like simple Java POJOs/records

Very common in clean Python.

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
```

Use:

```python
person = Person(name="Mark", age=35)
print(person.name)
```

Good for DTO-style objects.

---

# 15. Exceptions

## Java

```java
try {
    riskyMethod();
} catch (Exception e) {
    System.out.println(e.getMessage());
}
```

## Python

```python
try:
    risky_method()
except Exception as e:
    print(e)
```

Raise exception:

```python
raise ValueError("Invalid value")
```

Specific exception:

```python
try:
    number = int("abc")
except ValueError:
    print("Not a valid number")
```

---

# 16. Imports

## Java

```java
import java.util.List;
```

## Python

```python
import os
import json
```

Specific import:

```python
from pathlib import Path
```

Alias:

```python
import pandas as pd
```

Project import example:

```python
from services.user_service import UserService
```

---

# 17. Main method equivalent

## Java

```java
public static void main(String[] args) {
    System.out.println("Hello");
}
```

## Python

```python
def main():
    print("Hello")

if __name__ == "__main__":
    main()
```

This means: only run `main()` when this file is executed directly.

---

# 18. File handling

Read file:

```python
from pathlib import Path

text = Path("example.txt").read_text()
```

Write file:

```python
Path("output.txt").write_text("Hello")
```

Line by line:

```python
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
```

`with` automatically closes the file.

---

# 19. JSON

## Java would often use Jackson/ObjectMapper.

## Python

```python
import json

data = {
    "name": "Mark",
    "age": 35
}

json_text = json.dumps(data)
parsed = json.loads(json_text)
```

Read JSON file:

```python
from pathlib import Path
import json

data = json.loads(Path("data.json").read_text())
```

Write JSON file:

```python
Path("data.json").write_text(json.dumps(data, indent=2))
```

---

# 20. List comprehensions

Very Pythonic.

## Java-ish idea

```java
List<String> upperNames = names.stream()
    .map(String::toUpperCase)
    .toList();
```

## Python

```python
upper_names = [name.upper() for name in names]
```

Filter:

```python
adults = [person for person in people if person.age >= 18]
```

Map-like transform:

```python
lengths = [len(name) for name in names]
```

---

# 21. Lambdas

## Java

```java
x -> x * 2
```

## Python

```python
lambda x: x * 2
```

Example:

```python
numbers = [3, 1, 2]
sorted_numbers = sorted(numbers)
```

Sort objects/dicts:

```python
people = [
    {"name": "Mark", "age": 35},
    {"name": "Sarah", "age": 30}
]

people_sorted = sorted(people, key=lambda person: person["age"])
```

---

# 22. Truthiness

Python lets values behave like booleans.

These are falsey:

```python
None
False
0
""
[]
{}
set()
```

Example:

```python
names = []

if not names:
    print("No names")
```

Equivalent Java-ish meaning:

```java
if (names == null || names.isEmpty()) { }
```

---

# 23. Equality

## Java

```java
name.equals("Mark")
```

## Python

```python
name == "Mark"
```

Identity check:

```python
x is None
```

Use:

```python
==      # value equality
is      # same object / identity
```

Common Python style:

```python
if value is None:
    ...
```

---

# 24. Private fields / methods

Python does not enforce privacy like Java.

Convention:

```python
class UserService:
    def __init__(self):
        self._repository = None

    def _helper_method(self):
        pass
```

Single underscore means:

```python
_internal_use
```

Double underscore exists but is less commonly needed:

```python
self.__secret
```

---

# 25. Type hints

Python is dynamically typed, but type hints are common in professional code.

```python
def get_user(user_id: int) -> dict:
    return {"id": user_id}
```

Better:

```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Mark"
    return None
```

Common typing:

```python
list[str]
dict[str, int]
set[str]
tuple[str, int]
str | None
```

Example:

```python
def get_names() -> list[str]:
    return ["Mark", "Sarah"]
```

---

# 26. Interfaces / abstract classes

Java interface:

```java
public interface UserRepository {
    User findById(Long id);
}
```

Python usually uses duck typing:

```python
class UserService:
    def __init__(self, repository):
        self.repository = repository
```

More formal Python abstract class:

```python
from abc import ABC, abstractmethod

class UserRepository(ABC):
    @abstractmethod
    def find_by_id(self, user_id: int):
        pass
```

---

# 27. Static methods

## Java

```java
public static int add(int a, int b) {
    return a + b;
}
```

## Python

```python
class Calculator:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b
```

Call:

```python
Calculator.add(1, 2)
```

---

# 28. Constants

## Java

```java
public static final int MAX_SIZE = 10;
```

## Python

```python
MAX_SIZE = 10
```

Python convention: uppercase means constant.

---

# 29. Naming conventions

| Java            | Python            |
| --------------- | ----------------- |
| `UserService`   | `UserService`     |
| `getUserName()` | `get_user_name()` |
| `userName`      | `user_name`       |
| `MAX_SIZE`      | `MAX_SIZE`        |

Python uses:

```python
snake_case
```

Java uses:

```java
camelCase
```

---

# 30. Package/project structure

Simple Python project:

```text
project/
  app/
    __init__.py
    main.py
    services/
      __init__.py
      user_service.py
    repositories/
      __init__.py
      user_repository.py
  tests/
    test_user_service.py
  requirements.txt
```

`__init__.py` means the folder is a Python package.

---

# 31. Virtual environment

Equivalent to isolating dependencies for a project.

Create:

```bash
python -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

Install package:

```bash
pip install requests
```

Freeze dependencies:

```bash
pip freeze > requirements.txt
```

Install from requirements:

```bash
pip install -r requirements.txt
```

---

# 32. Testing

Common modern Python test tool: `pytest`.

Install:

```bash
pip install pytest
```

Example test:

```python
def add(a: int, b: int) -> int:
    return a + b


def test_add():
    assert add(1, 2) == 3
```

Run:

```bash
pytest
```

Exception test:

```python
import pytest

def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

---

# 33. Logging

Do not just use `print()` in production code.

```python
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)

logger.info("Application started")
logger.warning("Something might be wrong")
logger.error("Something failed")
```

---

# 34. HTTP requests

Java might use `RestTemplate`, `WebClient`, `HttpClient`.

Python commonly uses:

```bash
pip install requests
```

```python
import requests

response = requests.get("https://example.com")
print(response.status_code)
print(response.text)
```

JSON response:

```python
data = response.json()
```

Post JSON:

```python
response = requests.post(
    "https://example.com/users",
    json={"name": "Mark"}
)
```

---

# 35. Environment variables

```python
import os

db_url = os.getenv("DB_URL")
```

With default:

```python
db_url = os.getenv("DB_URL", "localhost")
```

---

# 36. Useful built-ins

```python
len(items)
sum(numbers)
min(numbers)
max(numbers)
sorted(items)
type(value)
isinstance(value, str)
range(10)
enumerate(items)
zip(list1, list2)
```

Example:

```python
if isinstance(name, str):
    print(name.upper())
```

---

# 37. Common Python gotchas for Java devs

## 1. Indentation is syntax

```python
if True:
    print("inside")
print("outside")
```

## 2. No braces

Python uses indentation instead of `{}`.

## 3. `None`, not `null`

```python
value = None
```

## 4. `True` / `False`, not `true` / `false`

```python
active = True
```

## 5. `and`, `or`, `not`, not `&&`, `||`, `!`

```python
if active and age > 18:
    ...
```

## 6. Lists are flexible

```python
items = [1, "hello", True]
```

Allowed, though not always good style.

## 7. Mutable default arguments are dangerous

Avoid this:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

Use this:

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

## 8. Integer division

```python
5 / 2   # 2.5
5 // 2  # 2
```

## 9. No method overloading in the Java sense

This does not work like Java:

```python
def add(a):
    ...

def add(a, b):
    ...
```

The second one replaces the first.

---

# 38. Java → Python quick mapping

| Java                   | Python                                    |
| ---------------------- | ----------------------------------------- |
| `String`               | `str`                                     |
| `int`, `long`          | `int`                                     |
| `double`, `float`      | `float`                                   |
| `boolean`              | `bool`                                    |
| `null`                 | `None`                                    |
| `ArrayList`            | `list`                                    |
| `HashMap`              | `dict`                                    |
| `HashSet`              | `set`                                     |
| `System.out.println()` | `print()`                                 |
| `this`                 | `self`                                    |
| `public/private`       | convention: `_internal`                   |
| `try/catch`            | `try/except`                              |
| `throw new`            | `raise`                                   |
| `import x.y.Class`     | `from x.y import Class`                   |
| `main()`               | `if __name__ == "__main__"`               |
| Maven/Gradle deps      | `pip`, `requirements.txt`, Poetry, Pipenv |
| JUnit                  | pytest / unittest                         |
| Jackson JSON           | `json` module / Pydantic                  |
| POJO/record            | dataclass / Pydantic model                |

---

# 39. Most important Python fluency patterns

Learn these first:

```python
# for-in loop
for item in items:
    print(item)

# dict loop
for key, value in data.items():
    print(key, value)


# here

message = f"the user's {name} is {age}"


# list comprehension
names = [user.name for user in users]


if value is None:


try:
    ...
except ValueError as e:
    ...


from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str


class UserRepository:
    def __init__(self):
        self.users = {
            1: User(id=1, name="Mark")
        }

    def find_by_id(self, user_id: int) -> User | None:
        return self.users.get(user_id)


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_user_name(self, user_id: int) -> str:
        user = self.repository.find_by_id(user_id)

        if user is None:
            raise ValueError("User not found")

        return user.name


def main():
    repository = UserRepository()
    service = UserService(repository)

    print(service.get_user_name(1))


if __name__ == "__main__":
    main()


# 41. What I may have missed / worth checking later

For onboarding to a real HMLR Python/Java project, the only things not covered deeply here are:

1. **Python web framework specifics** — Flask, FastAPI, or Django.
2. **Dependency tool used by the project** — `pip`, Poetry, Pipenv, or Docker-based setup.
3. **Linting/formatting** — `black`, `ruff`, `flake8`, `mypy`.
4. **Pydantic models** — very common with FastAPI and typed DTO-style validation.
5. **Async Python** — `async`, `await`, `asyncio`, if the project uses it.
6. **Database access** — SQLAlchemy, Django ORM, raw SQL, psycopg, etc.
7. **Mocking in tests** — `unittest.mock`, pytest fixtures.
8. **Packaging/import edge cases** — relative imports, module path issues.
9. **Java/Python integration patterns** — APIs, queues, shared schemas, generated clients.
10. **Project-specific conventions** — HMLR/GDS/public-sector style, CI/CD, Docker, environment config.

The core language fluency you need first is: **`str`, `list`, `dict`, `for in`, `def`, `class`, `None`, exceptions, imports, pytest, and virtual environments.**

