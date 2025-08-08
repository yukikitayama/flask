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
- 