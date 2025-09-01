import sqlite3
from bottle import Bottle
from bottle import Bottle, template
from bottle import request


app = Bottle()

# @app.route('/todo')
# def todo_list():
#     with sqlite3.connect('/home/user/todo.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute("SELECT id, task, status FROM todo WHERE status LIKE '1'")
#         # result = cursor.fetchall()
#         # return str(result)
#
#         result = cursor.fetchall()
#         output = template('show_tasks', rows=result)
#         return output

@app.get('/todo')
def todo_list():
    show  = request.query.show or 'open'
    match show:
        case 'open':
            db_query = "SELECT id, task FROM todo WHERE status LIKE '1'"
        case 'closed':
            db_query = "SELECT id, task FROM todo WHERE status LIKE '0'"
        case 'all':
            db_query = "SELECT id, task FROM todo"
        case _:
            return template('message.tpl',
                message = 'Wrong query parameter: show must be either open, closed or all.')
    with sqlite3.connect('/home/user/todo.db') as connection:
        cursor = connection.cursor()
        cursor.execute(db_query)
        result = cursor.fetchall()
    output = template('show_tasks.tpl', rows=result)
    return output
# url to use :              http://127.0.0.1:8080/todo?show=all

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
    #app.run(host='127.0.0.1', port=8080, reloader=True)




