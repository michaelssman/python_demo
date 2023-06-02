from flask import Flask, render_template, request

app = Flask(__name__)


# 创建了网址 /show/info 和 函数index 的对应关系
# 用户在浏览器访问 /show/info 网站自动执行 index
@app.route("/show/info")
def index():
    return render_template("index.html")


@app.route("/get/news")
def get_news():
    return render_template("get_news.html")


# GET请求是打开注册页面，POST请求是点击注册提交
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        # 接收到数据
        print(request.form)
        user = request.form.get("name")
        pwd = request.form.get("pd")
        hobby_list = request.form.getlist("hobby")
        print(user, pwd, hobby_list)
        # 将用户信息写入数据库，实现注册
        # 给用户返回结果
        return "注册成功"


# 登录
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        print(request.form)
        username = request.form.get("username")
        password = request.form.get("password")
        print(username,password)
        return "登录成功"


@app.route("/vue_demo")
def vue_demo():
    return render_template("vue_demo/Demo3.html")


if __name__ == '__main__':
    app.run()
