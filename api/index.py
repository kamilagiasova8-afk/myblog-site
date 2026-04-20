from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

posts = [
    {
        "id": 1,
        "title": "대학교 생활",
        "content": "명지대학교 경영학과에서의 첫 학기 이야기를 공유합니다."
    },
    {
        "id": 2,
        "title": "일상 기록",
        "content": "오늘의 공부와 하루 일상을 기록하는 공간입니다."
    },
    {
        "id": 3,
        "title": "나의 목표",
        "content": "앞으로 이루고 싶은 꿈과 목표들을 적어봅니다."
    }
]

@app.route("/")
def home():
    return render_template("home.html", posts=posts)

@app.route("/post/<int:post_id>")
def post(post_id):
    selected_post = next((p for p in posts if p["id"] == post_id), None)

    if not selected_post:
        return "Post not found", 404

    return render_template("post.html", post=selected_post)

app = app
