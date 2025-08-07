# Basics

- `app = Flask(__name__)`
  - Flask uses `__name__` to determine the root path of application, which is helpful to locate resources like templates, static files, and configuration files.
  - While you could technically pass a hardcoded string, using `__name__` is the recommended and conventional approach
  - Dynamically adapts to how application is being run and ensure resource directory
- `app.run()` default is debug mode = False

Multiple pages
- `@app.route()` the string parameter passed into the decorator determines the URL extension that will link to that function
  - **View**.