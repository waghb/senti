from googleapiclient.discovery import build
import subprocess

API_KEY = "AIzaSyA3p68jgLuC_pC2cYP4tKd7Er2-5-E6vqg"
VIDEO_ID = "DC7nYB0nuN0"

youtube = build("youtube", "v3", developerKey=API_KEY)

# Retrieve video comments
comments_request = youtube.commentThreads().list(
    part="snippet",
    videoId=VIDEO_ID,
    textFormat="plainText"
)
comments_response = comments_request.execute()

# Save comments to another file
output_file = r"/home/rutika/Documents/PBL/E/output_file"
with open(output_file, 'w', encoding='utf-8') as file:
    for item in comments_response["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        file.write(comment + '\n')

print(f"Comments saved to '{output_file}' successfully!")

# Execute another Python file at the end
second_file_path = r"/home/rutika/Documents/PBL/E/emotione.py"
subprocess.run(["python3", second_file_path])
