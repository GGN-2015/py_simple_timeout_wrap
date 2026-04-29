# py_simple_timeout_wrap
A simple function execution time limit tool based on `concurrent.futures`.

## Installation
```bash
pip install py_simple_timeout_wrap
```

## Usage

```python
from py_simple_timeout_wrap import time_limit
import time

# Set function max execution time to 1 second
@time_limit(1.0)
def task_1():
    time.sleep(0.5)
    return "task_1: done"

# Normal execution within time limit
print(task_1()) # Output: task_1: done

# Set function max execution time to 1 second
@time_limit(1.0)
def task_2():
    time.sleep(1.5)
    return "task_2: done"

# Exceed time limit, throw TimeoutError automatically
print(task_2()) # TimeoutError: function `task_2` time limit exceeded (1s)
```
