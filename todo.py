import sqlite3
from bottle import Bottle
from bottle import Bottle, template

app = Bottle()

@app.route('/todo')
def todo_list():
    with sqlite3.connect('/home/user/todo.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, task, status FROM todo WHERE status LIKE '1'")
        # result = cursor.fetchall()
        # return str(result)

        result = cursor.fetchall()
        output = template('show_tasks', rows=result)
        return output

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
    #app.run(host='127.0.0.1', port=8080, reloader=True)




