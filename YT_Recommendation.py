import pandas as pd
from apiclient.discovery import build
import os
from dotenv import load_dotenv, dotenv_values 

load_dotenv() 

api_key = os.getenv("API_Key")
def recommendations(query):
    #query = "Algebra and Probability in machine learning"
    query = query.replace(" ", "+")
    youtube = build("youtube", "v3", developerKey = api_key)
    req = youtube.search().list(q='algebra',part = 'snippet', type = 'video',maxResults=5)
    res = req.execute()
    
    videos = {}
    for i in res['items']:
        video_link = "https://www.youtube.com/watch?v=" + i['id']['videoId']
        video_title = i['snippet']['title']
        videos[video_title] = video_link
    return videos