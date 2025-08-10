from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    # name = "Jose"
    # letters = list(name)
    # pup_dictionary = {"pup_name": "Sammy", "a": "b"}
    # return render_template(
    #     "basic.html",
    #     name=name,
    #     letters=letters,
    #     pup_dictionary=pup_dictionary
    # )

    # mylist = [1, 2, 3, 4, 5]
    # puppies = ["Fluffy", "Rufus", "Spike"]
    # user_logged_in = True
    user_logged_in = False
    return render_template("control.html", user_logged_in=user_logged_in)


if __name__ == "__main__":
    app.run(debug=True)