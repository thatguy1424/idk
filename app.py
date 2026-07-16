from flask import Flask, render_template, request
from pornhub_api import PornhubApi

app = Flask(__name__)

api = PornhubApi()


@app.route("/")
def index():
    query = request.args.get("q", "")
    videos = []

    if query:
        results = api.search.search_videos(query)

        for video in results.__root__[:20]:
            videos.append({
                "id": video.video_id,
                "title": video.title,
                "thumb": str(video.thumbs[0].src) if video.thumbs else "",
                "views": video.views,
                "url": str(video.url)
            })

    return render_template(
        "index.html",
        videos=videos,
        query=query
    )


@app.route("/video/<video_id>")
def video_page(video_id):

    return render_template(
        "video.html",
        video_id=video_id
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )