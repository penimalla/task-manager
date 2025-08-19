from flask import Flask, render_template, request, redirect, url_for

# Elastic Beanstalk looks for a WSGI callable named `application`
application = Flask(__name__)

# In-memory "DB" for demo purposes
tasks = []

@application.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@application.route("/add", methods=["POST"])
def add():
    task = request.form.get("task", "").strip()
    if task:
        tasks.append({"task": task, "done": False})
    return redirect(url_for("index"))

@application.route("/done/<int:task_id>")
def mark_done(task_id: int):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = True
    return redirect(url_for("index"))

@application.route("/delete/<int:task_id>")
def delete(task_id: int):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    # Local testing
    application.run(host="0.0.0.0", port=5000, debug=True)
