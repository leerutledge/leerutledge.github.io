"""
SplitCalculator index (main) view.

URLs include:
/
"""
import flask
import splitCalculator
import os
import shutil
import tempfile
import arrow
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

def filenamehash(filename):
    """Return sha256 hash of file content, similar to UNIX filenamehash."""
    content = open(filename, 'rb').read()
    sha256_obj = hashlib.sha256(content)
    return sha256_obj.hexdigest()



@splitCalculator.app.route('/')
def show_index():
    """Display / route."""
    cur = get_db().cursor()
    # logname = flask.session.get('logname')
    context = {}
    logname = flask.session.get('logname')
    if logname is None:
        return flask.redirect(flask.url_for('show_login'))

    if flask.request.method == "GET":
        query_projects = "SELECT * FROM projects WHERE projectid IN " + \
                         "(SELECT projectid FROM tracks WHERE " + \
                         "(owner0 = ? OR owner1 = ? OR owner2 = ? OR owner3 = ? OR owner4 = ?)) " + \
                         "ORDER BY created DESC"
        cur.execute(query_projects, (logname, logname, logname, logname, logname, ))
        rows = cur.fetchall()

        for project in rows:
            # DO ME, REFERENCE OTHER INDEX.PY
            project_id = project['projectid']
            query_release_date = "SELECT releasedate FROM projects WHERE projectid = ?"
            data_release_date = (project_id,)
            cur.execute(query_release_date, data_release_date,)
            release_date = cur.fetchone()
            project['releasedate'] = release_date['releasedate']
            query_title = "SELECT title FROM projects WHERE projectid = ?"
            data_title = (project_id,)
            cur.execute(query_title, data_title,)
            title = cur.fetchone()
            project['title'] = title['title']
            query_cover_art = "SELECT coverart FROM projects WHERE projectid = ?"
            data_cover_art = (project_id,)
            cur.execute(query_cover_art, data_cover_art,)
            cover_art = cur.fetchone()
            project['coverart'] = cover_art['coverart']
            print(title)
            project['slug'] = project["projectid"]


        query_pay_period_selected = "SELECT payperiodstart FROM payperiods WHERE selected = 1"
        cur.execute(query_pay_period_selected, )
        pay_period_selected = cur.fetchone()
        context["pay_period_selected"] = pay_period_selected["payperiodstart"] # MIGHT NEED TO PUT A TABLE IN THE DATABASE FOR PAY PERIODS BASED ON UPLOADED CSVS

        query_pay_periods = "SELECT payperiodstart FROM payperiods"
        cur.execute(query_pay_periods, )
        pay_periods = cur.fetchall()
        context["pay_periods"] = [pay_period_to_range_dict[i["payperiodstart"]] for i in pay_periods]
        context["logname"] = logname
        context["projects"] = rows
        return flask.render_template("index.html", **context)

    if flask.request.method == "POST":
        post_data = flask.request.form.to_dict()
        # ADD ANOTHER IF FOR THE SELECTED VALUE AND MAKE SURE ONLY ONE IS 1 AT A TIME
        if 'upload_file' in post_data and 'file' not in post_data:
            # Save POST request's file object to a temp file
            dummy, temp_filename = tempfile.mkstemp()
            file = flask.request.files["file"]
            dummy, suffix = os.path.splitext(file.filename)
            if suffix.split('.')[1] \
                    in splitCalculator.app.config['ALLOWED_EXTENSIONS']:
                file.save(temp_filename)

                # Compute filename
                hash_txt = filenamehash(temp_filename)
                hash_filename_basename = hash_txt + suffix
                hash_filename = os.path.join(
                    splitCalculator.app.config["UPLOAD_FOLDER"],
                    hash_filename_basename)

                # Move temp file to permanent location
                shutil.move(temp_filename, hash_filename)

                # Add to database FIXME: MODIFY FOR SPLIT CALC
                # cur.execute("SELECT MAX(postid) AS max FROM posts")
                # new_index = int(cur.fetchone()['max']) + 1
                # cur.execute("INSERT INTO posts (postid,filename,owner) \
                #             VALUES (?,?,?)",
                #             (new_index, hash_filename_basename, logname))

    return flask.render_template("index.html", **context)
