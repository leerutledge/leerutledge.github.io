"""
SplitCalculator project view.

URLs include:
/project/<project_id>/
"""
import os
import tempfile
import shutil
import hashlib
import flask
import splitCalculator
from splitCalculator.model import get_db

pay_period_to_range_dict = {
    "Jan": "Jan - Feb",
    "Feb": "Feb - Mar",
    "Mar": "Mar - Apr",
    "Apr": "Apr - May",
    "May": "May - Jun",
    "Jun": "Jun - Jul",
    "Jul": "Jul - Aug",
    "Aug": "Aug - Sep",
    "Sep": "Sep - Oct",
    "Oct": "Oct - Nov",
    "Nov": "Nov - Dec",
    "Dec": "Dec - Jan",
}

@splitCalculator.app.route('/project/<project_id>/', methods=['GET','POST'])
def show_project(project_id):
    """Display / route."""
    cur = get_db().cursor()
    # logname = flask.session.get('logname')
    context = {}
    logname = flask.session.get('logname')
    if logname is None:
        return flask.redirect(flask.url_for('show_login'))

    if flask.request.method == "GET":
        query_projects = "SELECT * FROM projects WHERE projectid = ?"
        data_projects = ( project_id, )
        cur.execute( query_projects, data_projects, )
        project = cur.fetchone()
        project["slug"] = project_id
        print(project)
        context["project"] = project

        query_tracks = "SELECT * FROM tracks WHERE projectid = ? and " + \
                       "(owner0 = ? OR owner1 = ? OR owner2 = ? OR owner3 = ? OR owner4 = ?)"
        data_tracks = ( project_id, logname, logname, logname, logname, logname, )
        cur.execute( query_tracks, data_tracks, )
        rows = cur.fetchall()
        for track in rows:
            track_id = track["trackid"]
            query_number = "SELECT tracknumber FROM tracks WHERE trackid = ?"
            data_number = (track_id,)
            cur.execute(query_number, data_number,)
            number = cur.fetchone()
            track['number'] = number['tracknumber']
            query_title = "SELECT title FROM tracks WHERE trackid = ?"
            data_title = (track_id,)
            cur.execute(query_title, data_title,)
            title = cur.fetchone()
            track['title'] = title['title']
            query_earnings = "SELECT amount FROM earnings WHERE trackid = ?"
            data_earnings = (track_id,)
            cur.execute(query_earnings, data_earnings,)
            earnings = cur.fetchone()
            track['earnings'] = earnings['amount']
            track['slug'] = track_id

        context["tracks"] = rows
        context["logname"] = logname

        query_pay_period_selected = "SELECT payperiodstart FROM payperiods WHERE selected = 1"
        cur.execute(query_pay_period_selected, )
        pay_period_selected = cur.fetchone()
        context["pay_period_selected"] = pay_period_selected["payperiodstart"] # MIGHT NEED TO PUT A TABLE IN THE DATABASE FOR PAY PERIODS BASED ON UPLOADED CSVS

        query_pay_periods = "SELECT payperiodstart FROM payperiods"
        cur.execute(query_pay_periods, )
        pay_periods = cur.fetchall()
        context["pay_periods"] = [pay_period_to_range_dict[i["payperiodstart"]] for i in pay_periods]

    return flask.render_template("project.html", **context)
