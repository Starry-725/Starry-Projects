from flask import Flask, render_template, request

app = Flask(__name__)

# 定义路由和视图函数
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    # 处理上传的文件
    return '文件上传成功！'

# 启动应用程序
if __name__ == '__main__':
    app.run(debug=True)
