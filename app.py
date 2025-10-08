from flask import Flask, render_template, session, request
from flask_session import Session

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'super secret key'

Session(app)

# 添加一个路由为xmcx开发组工作站节点的页面
@app.route('/xmcx')
def xmcx():
    return render_template('xmcxgongzuozhan.html')

@app.route('/EnTh')
def EnTh():
    return render_template('EnTh.html')


@app.route('/Enshouquan', methods=['POST'])
def acc1ept():
        if request.form.get("password") == "EPasswda":
            session["erbuyanzheng"] = "YES"
            return render_template("ysq.html")
        elif request.form.get("password") == None:
            return render_template("Login.html")
        else:
            return render_template("Not.html")

@app.route('/ETZD')
def ETZD():
    return render_template("ETZD.html")


@app.route('/')
def index():
    if session.get('yijingyouzhanghu') == None:
        session['yijingyouzhanghu'] = "hh"
        return render_template('hy.html')
    else:
        return render_template('index.html')


@app.route('/xiaomingchaxun')
def xmindex():
    if session.get('XMGLY') == None or session.get('erbuyanzheng') == None:
        return render_template('xyguanliyuan.html')
    else:
        return render_template('xmcx.html')

@app.route('/jieshou')
def chaxun():
    if session.get('XMGLY') == None or session.get('erbuyanzheng') == None:
        return render_template('xyguanliyuan.html')
    else:
        return render_template('chaxun.html')

@app.route('/find')
def chaxun2():
    if session.get('XMGLY') == None or session.get('erbuyanzheng') == None:
        return render_template('xyguanliyuan.html')
    else:
        return render_template('zhaodao.html')

@app.route('/sessionxmcx')
def sessionxmcx():
    if session.get('XMGLY') == None or session.get('erbuyanzheng') == None:
        return render_template('xyguanliyuan.html')
    else:
        session["xmcxrenwu"] = "YES"
        return "合同已完成"

@app.route('/accept')
def sessionchaxun():
    return render_template('Login.html')

@app.route('/shouquan', methods=['POST'])
def accept():
        if request.form.get("password") == "lrx123456":
            session["XMGLY"] = "YES"
            return render_template("ysq.html")
        elif request.form.get("password") == None:
            return render_template("Login.html")
        else:
            return render_template("Not.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=32323,debug=True)

