
class ChannelModel:
    id = 'IntegerField'
    uuid = 'UUID'
    name = 'CharField'
    url = 'CharField'
    created_at = 'DateTimeField'
    updated_at = 'DateTimeField'
    published_at = 'DateTimeField'
    description = 'CharField'


class ChannelVideoModel:
    id = 'IntegerField'
    channel_id = 'ForeignKey(ChannelModel.id)'
    created_at = 'DateTimeField'
    updated_at = 'DateTimeField'
    views_count = 'IntegerField'
    comments_count = 'IntegerField'
    videos_count = 'IntegerField'
    subscribers_count = 'IntegerField'


class ChannelStatisticModel:

    """This model can be used for storing data showed on the site."""

    id = 'IntegerField'
    channel_id = 'ForeignKey(ChannelModel.id)'
    created_at = 'DateTimeField'
    updated_at = 'DateTimeField'
    total_views = 'IntegerField'
    total_comments = 'IntegerField'
    total_videos = 'IntegerField'
    total_subscribers = 'IntegerField'



