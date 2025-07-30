# HTML

- The main components of a site are defined by HTML elements.
- HTML elements have corresponding tags inside an .html file
- Divs and Spans allow us to segment portions of our HTML.
- Some element tags have attributes that you can manipulate.
  - Adding a link, adding a source image.

Form basics
- Use `<form>` tags to set up a form
- Then add special `<input>` tags to accept user information.
- Every major form element already has a corresponding input tag attribute.
- At the end, provide a submit input type to add a button for form submission.
  - `<input type="email">`, `<input type="password">`
  - `<input type="submit">`
- Label the input, use `for` and `id` to connect.
  - `<label for="input-id">Label</label>`
  - `<input id="input-id" type="email" name="" value="">`
- `<form action="" method="get">`, `action` tells you the next action when submit
  - input values will appear as query to the next URL for the action.