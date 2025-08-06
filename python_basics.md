# Python basics

Scope
- Determines where you can see and access a variable
- LEGB rule, find a variable or function in the following order
  - Local
  - Enclosing
  - Global
  - Built-in
```python
x = "GLOBAL"

def enclosing():
    x = "ENCLOSING"
    def inside():
        # There is no local
        print(x)
    inside()

enclosing()  # Should show enclosing
```
- Inside function, `global x` can grab `x` in a global scope, and can modify the global `x` inside function

OOP
- Class object attributes come before `__init__`. It exists regardless of class instances.
  - Doesn't need `self` when defining it inside class and outside class methods
  - Need `self` to access inside the class methods.
  - `object_name.class_object_attribute` to use it with object
- Special methods
  - `__str__` and `def __repr__(self):` (representation) are used for printing an object.
    - Use `return`
  - `def __len__(self):` returns output when `len(object)`.

Decorator
- On/off switch to quickly add functionality to a function
- Allow you to tack on extra functionality to an already existing function
- Use `@` operator and are then place on top of the original function
- Returning a function