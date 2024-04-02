from googleapiclient.discovery import build
import subprocess

API_KEY = "AIzaSyA3p68jgLuC_pC2cYP4tKd7Er2-5-E6vqg"
VIDEO_ID = "-Ebkbgof0io"

youtube = build("youtube", "v3", developerKey=API_KEY)

# Retrieve video comments
comments = []

# Initialize nextPageToken for pagination
next_page_token = None

while True:
    # Make request to fetch comments
    comments_request = youtube.commentThreads().list(
        part="snippet",
        videoId=VIDEO_ID,
        textFormat="plainText",
        pageToken=next_page_token
    )
    comments_response = comments_request.execute()

    # Extract comments from response
    for item in comments_response["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)

    # Check if there are more pages of comments
    next_page_token = comments_response.get("nextPageToken")

    # Break the loop if no more pages
    if not next_page_token:
        break

# Save comments to a file
output_file = "output_file.txt"
with open(output_file, 'w', encoding='utf-8') as file:
    for comment in comments:
        file.write(comment + '\n')

print(f"Comments saved to '{output_file}' successfully!")

# Execute another Python file at the end
second_file_path = r"/home/rutika/Documents/PBL/emotion.py"
subprocess.run(["python3", second_file_path])
