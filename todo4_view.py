from flask import Flask, render_template

todo4 = Flask(__name__)

todos = [{'tno':1, 'title':'전투지옥', 'date':'2025-03-12'},
         {'tno':2, 'title':'미용실 방문문', 'date':'2025-03-12'}]
@todo4.route("/todo4/list")
def list():
    count = len(todos)
    return render_template("todo4/list.html", todos=todos, count=count)





todo4.run(debug=True)