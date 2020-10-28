import requests
import logging


API_KEY = '<YOUR API KEY>'

log = logging.getLogger(__name__)


class YouTubeChannelService:

    part = 'snippet,contentDetails,statistics'
    base_url = 'https://youtube.googleapis.com/youtube/v3/channels'
    headers = {'Accept': 'application/json'}


    def __init__(self):
        self.data = {}


    def get_channel_name(self):
        return self.data.get('snippet', {}).get('title')


    def get_total_views(self):
        return int(self.data.get('statistics', {}).get('viewCount', 0))

    def get_total_videos(self):
        return int(self.data.get('statistics', {}).get('videoCount', 0))


    def get_channel_info_by_username(self, username):
        params = {
            'part': self.part,
            'forUsername': username,
            'key': API_KEY
        }
        try:
            response = requests.get(
                self.base_url, headers=self.headers, params=params
            )
            data = response.json()
            items = data.get('items', [])
            if items:
                self.data = items[0]
        except requests.RequestException as e:
            log.error(str(e))



    def get_channel_info_by_channel_id(self, channel_id):
        params = {
            'part': self.part,
            'id': channel_id,
            'key': API_KEY
        }
        try:
            response = requests.get(
                self.base_url, headers=self.headers, params=params
            )
            data = response.json()
            items = data.get('items', [])
            if items:
                self.data = items[0]
        except requests.RequestException as e:
            log.error(str(e))
