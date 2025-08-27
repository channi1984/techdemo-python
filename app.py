from flask import Flask

# Flask 클래스의 인스턴스 생성
app = Flask(__name__)

# 홈페이지에 대한 라우트 정의
@app.route('/')
def hello_world():
	return 'Hello, Wolrd'

# 애플리케이션 실행
if __name__ == '__main__':
	app.run(debug=True)