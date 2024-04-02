from flask import Flask, render_template, request
from googleapiclient.discovery import build

import api
import emotion

app = Flask(__name__)

# YouTube API key
API_KEY = "AIzaSyA3f8zPvrUDvinVT0A3Ywovr04crqjBIJc"

# Function to retrieve video comments
# def get_video_comments(video_id):
#     youtube = build("youtube", "v3", developerKey=API_KEY)
#     comments = []
#     next_page_token = None

#     while True:
#         comments_request = youtube.commentThreads().list(
#             part="snippet",
#             videoId=video_id,
#             textFormat="plainText",
#             pageToken=next_page_token
#         )
#         comments_response = comments_request.execute()

#         for item in comments_response["items"]:
#             comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
#             comments.append(comment)

#         next_page_token = comments_response.get("nextPageToken")

#         if not next_page_token:
#             break

#     return comments

@app.route('/')
def index():
    return render_template('indexx.html', result=None)

@app.route('/analyze', methods=['POST'])
def analyze():
    #for video_id
    video_id = request.form['video_id']
    result = 0
    #for url based
    # url = request.form['video_id']

    # video_id = url.split("=")[1]
    

    f = api.create_comments(video_id)

    e = emotion.strat_emotion_eng(f)

    # Save comments to a file
    # output_file = "output_file.txt"
    # with open(output_file, 'w', encoding='utf-8') as file:
    #     for comment in comments:
    #         file.write(comment + '\n')

    # print(f"Comments saved to '{output_file}' successfully!")


    # # Execute another Python file
    # second_file_path = "emotion.py"
    # subprocess.run(["python3", second_file_path])

    if(e == 1):
        return render_template('result.html')
        # return render_template('indexx.html', result=1)
    else:
        return render_template("failed.html")
        # return render_template('indexx.html', result=0)
    

if __name__ == '__main__':
    app.run(debug=True)

