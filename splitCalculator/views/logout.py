"""Logout URL."""
import flask
import splitCalculator


@splitCalculator.app.route('/accounts/logout/')
def show_logout():
    """Logout and redirect to login page."""
    flask.session.clear()
    return flask.redirect('/accounts/login/')
