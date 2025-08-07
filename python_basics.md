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

Packages
- Adding `__init__.py` to a directory tells Python that it is a package.

`__name__` and `"__main__"`
- `__name__` allows you to see whether something is being imported or run directly
- Sometimes when you are importing from a module, you would like to know 
  - whether a modules function is being used as an import, 
  - or if you are using the original .py file of that module.
