# api/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bs4 import BeautifulSoup
import requests
from urllib.parse import unquote

# Proxy fetch function
def proxy_fetch(target_url):
    response = requests.get(target_url)
    if response.status_code == 200:
        return response.content
    return None

# Original function to get video info
def get_video_info(video_url):
    content = proxy_fetch(video_url)
    if content:
        soup = BeautifulSoup(content, 'html.parser')
        video_tag = soup.find('video')
        if video_tag:
            video_src = video_tag['src']
            return video_src
    return None

@api_view(['POST'])
def get_video_api(request):
    video_url = request.data.get('video_url')

    if video_url:
        video_src = get_video_info(video_url)
        if video_src:
            video_src_decoded = unquote(video_src)
            return Response({'video_src': video_src_decoded})
        else:
            return Response({'error': 'Failed to get video source.'}, status=400)
    else:
        return Response({'error': 'Video URL not provided.'}, status=400)
