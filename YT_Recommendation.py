import pandas as pd
from apiclient.discovery import build

#creds_data = pd.read_json("creds.json")
api_key = "AIzaSyBo8neO87v5UwoFhisEYThE0KZcqeqCkaE"

query = "Algebra and Probability in machine learning"
query = query.replace(" ", "+")
print(query)


youtube = build("youtube", "v3", developerKey = api_key)

req = youtube.search().list(q='algebra',part = 'snippet', type = 'video',maxResults=5)
res = req.execute()
print(res)

videos = {}
for i in res['items']:
    # print(i['id']['videoId'])
    # print(i['snippet']['title'])

    video_link = "https://www.youtube.com/watch?v=" + i['id']['videoId']
    video_title = i['snippet']['title']
    videos[video_title] = video_link

print(videos)