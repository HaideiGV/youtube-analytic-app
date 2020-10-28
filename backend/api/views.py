from django.http import HttpResponse, JsonResponse

from .services import YouTubeChannelService


def index(request):
    return HttpResponse("Start page.")


def get_channel_info(request):
    query_params = request.GET

    username = query_params.get('username')
    channel_id = query_params.get('channel_id')

    service = YouTubeChannelService()

    if not username and not channel_id:
        return JsonResponse(data={})

    if channel_id:
        service.get_channel_info_by_channel_id(channel_id)

    if username:
        service.get_channel_info_by_username(username)

    channel_name = service.get_channel_name()
    total_views = service.get_total_views()
    total_videos = service.get_total_videos() or 1
    data = {
        'channel_name': channel_name,
        'total_views': total_views,
        'avg_views': int(total_views / total_videos)
    }

    return JsonResponse(data=data, content_type='application/json')

