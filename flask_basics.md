# Basics

- `app = Flask(__name__)`
  - Flask uses `__name__` to determine the root path of application, which is helpful to locate resources like templates, static files, and configuration files.
  - While you could technically pass a hardcoded string, using `__name__` is the recommended and conventional approach
  - Dynamically adapts to how application is being run and ensure resource directory
- `app.run()` default is debug mode = False

Multiple pages
- `@app.route()` the string parameter passed into the decorator determines the URL extension that will link to that function
  - **View**.

Dynamic route
- A variable in the route `<variable>`
- A parameter passed in to the function
  - `app.route("<something>")`, `def func(something):`

Debug mode
- `app.run(debug=True)` helps us catch errors
- Gives us access to a console in the browser
- When an error happens, an error in the terminal can appear inside browser.
- There will be terminal icon in the error logs inthe browser.
  - Copy **Debugger PIN** from the original terminal which is running Flask app
  - Use the PIN and check run time variables in the small terminal on the browser.
- Don't use `debug=True` when you are deploying to the production.

Template
- Connect a view function to render HTML template (HTML files we've already created for a page)
- Flask automatically look for HTML templates in the `template` directory
- `from flask import render_template`, `render_tamplete("name.html")` automatically search `name.html` that should exist in `templates` folder at the same level directory
- Using the **render_template** function, we can directly render an HTML file with our Flask web app.
- **Jinja** templating will let us directly insert variables from our Python code to the HTML file.
  - `{{some_variable}}`
- Set parameters in `render_template` function and then use the `{{}}` syntax to insert them in the tamplate.
- Use `{% %}` to control flow syntax such as for loops and if statements.
```
<ul>
  {% for item in mylist %}
  <li>{{item}}</li>
  {% endfor %}
</ul>
```

Template inheritance
- Usually pages across a web application share a lot of features (e.g. navigation bar, footer)
- Set up a base.html template file with the re-usable aspects of the site
- Use `{% extend "base.html" %}` and `{% block %}` statements to extend the re-usable aspects to other pages.

Filter
- `{{ variable | filter }}`
- `{{ name | capitalize }}`

url_for
- Connects other template pages or files within template
- `{{ url_for("app-route-function-name") }}` navigates to other pages
- `{{ url_for('static', filename='image.png')` can show image file in the static folder.

Flask form
- Use `flask_wtf` and `wtforms` to create forms
- Configure a secret key for security
- Create a WTForm class
- Set up a view function
- Every possible HTML form field has a corresponding wtforms class
  - wtforms has validators
- Use Flask's `session` object to grab the information provided in the form abd pass it to another template
  - Temporarily saved in a server

Flashing messages
- Flash a message to a user that we don't need to save or fix permanently to the template page

Database
- To connect Python, Flask, and SQL, we need an **ORM (Object Relational Mapper)**.
- ORM allows us to use Python instead of SQL syntax to create, edit, update, delete from database
- **SQL Alchemy** is the most common ORM for Python.
- `Flask-SQLAlchemy` is an extension for an easy connection between Flask and SQLAlchemy
- Set up SQLite Database in a Flask App
- Create a model in Flask app
  - Model is just a table in a SQL database.
- Perform CRUD on our model
- `app.app_context().push()`
  - https://flask-sqlalchemy.palletsprojects.com/en/stable/contexts/