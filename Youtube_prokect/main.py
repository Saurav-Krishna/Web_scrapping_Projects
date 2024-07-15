
from googleapiclient.discovery import build
import pandas as pd
api_key = 'AIzaSyB99eFxxXYbKmseBG8tEDRNV2myrLyUtng'


youtube = build('youtube', 'v3', developerKey=api_key) #service object 

# request = youtube.channels().list(part='statistics', forUsername='GoogleDevelopers')
# response = request.execute()
# print(response)


search_request = youtube.search().list(q='avatar moview', part='snippet', type='video', maxResults=1)
search_response = search_request.execute()


video_id = search_response['items'][0]['id']['videoId']

video_request =youtube.videos().list(part='snippet', id=video_id)
# print(video_id)
video_response = video_request.execute()
v_info  = {
    'ID': video_response['items'][0]['id'],
    'Snippet': video_response['items'][0]['snippet'],
    'Channel Title': video_response['items'][0]['snippet']['channelTitle'],
    'Video Description': video_response['items'][0]['snippet']['description'],
    'Channel Id': video_response['items'][0]['snippet']['channelId'],
    'Title': video_response['items'][0]['snippet']['title'],
    'Vidoe URL': f'https://www.youtube.com/watch?v={video_id}'
}

print(v_info)



search_rq2 = youtube.search().list(
    q= 'Avatar movie',
    part='snippet',
    type='video',
    maxResults=50,
    regionCode = 'US',
#cant order based on relevance only on view count?
)
search_response2 = search_rq2.execute()

# extracting info for each video 
videos_info = []

for i in search_response2['items']:
    
    video_ID = i['id']['videoId']
    v_title = i['snippet']['title']
    
    # for likes ,comments as they are stats
    stats_req = youtube.videos().list(
        part = 'statistics',
        id = video_ID
    )
    
    stats_response = stats_req.execute()
    
    try:
        v_likes = stats_response['items'][0]['statistics']['likeCount']
    except:
        v_likes = 0
    try:
        v_comments = stats_response['items'][0]['statistics']['commentCount']
    except:
        v_comments = 0
        
    v_likes = stats_response['items'][0]['statistics']['likeCount']
    v_comments = stats_response['items'][0]['statistics']['commentCount']
    
    videos_info.append ({
        'video ID': video_ID,
        'Title': v_title,
        'No. of Likes': v_likes,
        'No, of Comments': v_comments
    })
    
# for i in videos_info:
#     print(i)
    
df = pd.DataFrame(videos_info)

df.to_csv('Avatar_youtube.csv',index=False)
    
    

