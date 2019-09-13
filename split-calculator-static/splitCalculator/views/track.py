"""
SplitCalculator track view.

URLs include:
/project/<project_id>/track/<track_id>/
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

@splitCalculator.app.route('/project/<project_id>/track/<track_id>/', methods=['GET','POST'])
def show_track(project_id, track_id):
    """Display / route."""
    cur = get_db().cursor()
    # logname = flask.session.get('logname')
    context = {}
    project = {}
    logname = flask.session.get('logname')
    if logname is None:
        return flask.redirect(flask.url_for('show_login'))

    if flask.request.method == "GET":
        query_title = "SELECT title FROM projects WHERE projectid = ?"
        data_title = (project_id,)
        cur.execute(query_title, data_title,)
        title = cur.fetchone()
        project['title'] = title['title']
        project['slug'] = project_id
        context["project"] = project

        query_earnings = "SELECT amount FROM earnings WHERE trackid = ?"
        data_earnings = (track_id,)
        cur.execute(query_earnings, data_earnings,)
        total_earnings = cur.fetchone()

        query_share = "SELECT * FROM tracks WHERE trackid = ?"
        data_share = (track_id,)
        cur.execute(query_share, data_share,)
        track_tmp = cur.fetchone()
        share = 0.00
        if logname == track_tmp["owner0"]:
            share = track_tmp["ownership0"]
        elif logname == track_tmp["owner1"]:
            share = track_tmp["ownership1"]
        elif logname == track_tmp["owner2"]:
            share = track_tmp["ownership2"]
        elif logname == track_tmp["owner3"]:
            share = track_tmp["ownership3"]
        elif logname == track_tmp["owner4"]:
            share = track_tmp["ownership4"]


        query_track = "SELECT * FROM tracks WHERE trackid = ?"
        data_track = (track_id,)
        cur.execute(query_track, data_track,)
        track = cur.fetchone()
        context["track"] = {
            "slug": track_id,
            "title": track["title"],
            "upc": track["upc"],
            "isrc": track["isrc"],
            "total_earnings": total_earnings["amount"],
            "your_earnings": share * total_earnings["amount"]
        }
        query_pay_period_selected = "SELECT payperiodstart FROM payperiods WHERE selected = 1"
        cur.execute(query_pay_period_selected, )
        pay_period_selected = cur.fetchone()
        context["pay_period_selected"] = pay_period_selected["payperiodstart"] # MIGHT NEED TO PUT A TABLE IN THE DATABASE FOR PAY PERIODS BASED ON UPLOADED CSVS

        query_pay_periods = "SELECT payperiodstart FROM payperiods"
        cur.execute(query_pay_periods, )
        pay_periods = cur.fetchall()
        context["pay_periods"] = [pay_period_to_range_dict[i["payperiodstart"]] for i in pay_periods]
        context["logname"] = logname
    return flask.render_template("track.html", **context)
