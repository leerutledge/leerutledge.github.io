"""
Insta485 index (main) view.

URLs include:
/
"""
import hashlib
import flask
import splitCalculator
from splitCalculator.model import get_db


@splitCalculator.app.route('/accounts/login/', methods=['GET', 'POST'])
def show_login():
    """Display /accounts/login route."""
    if 'logname' in flask.session:
        return flask.redirect(flask.url_for('show_index'))
    if flask.request.method == 'POST':
        database = get_db().cursor()
        all_users = database.execute('SELECT * FROM users').fetchall()

        for user in all_users:
            if flask.request.form['username'] == user['username']:
                password_array = user['password'].split('$')
                salt = password_array[1]
                algorithm = 'sha512'
                hash_obj = hashlib.new(algorithm)
                password_salted = salt + flask.request.form['password']
                hash_obj.update(password_salted.encode('utf-8'))
                password_hash = hash_obj.hexdigest()
                password_db_string = "$".join([algorithm, salt, password_hash])
                if password_db_string == user['password']:
                    flask.session['logname'] = user['username']
                    return flask.redirect(flask.url_for('show_index'))

                flask.abort(409)
    context = {}
    return flask.render_template("login.html", **context)
