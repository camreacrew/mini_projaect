from flask import Flask, render_template

todo2 = Flask(__name__)

todos = [{'tno': 1, 'title':'잠자기', 'date':'2025-03-12'},
         {'tno': 1, 'title':'미용실', 'date':'2025-03-12'}]
@todo2.route("/todo2/list")
def list():
    count = len(todos)
    return render_template("todo2/list.html", todos = todos, count = count)




todo2.run(debug=True)