from django.core.serializers.python import Serializer
from django.core.cache import cache
import datetime
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


class LazyAccountEncoder(Serializer):
    def get_dump_object(self, obj):
        dump_object = {}
        dump_object.update({'id': str(obj.id)})
        dump_object.update({'email': str(obj.email)})
        dump_object.update({'username': str(obj.username)})
        dump_object.update({'profile_image': str(obj.profile_image.url)})
        return dump_object


def online(user_id):
    last_seen_time = cache.get('seen_%s' % user_id)
    if last_seen_time:
        current_time = timezone.localtime(timezone.now())
        if current_time <= last_seen_time + timezone.timedelta(seconds=settings.USER_ONLINE_TIMEOUT):
            return "Online"
        elif current_time <= last_seen_time + timezone.timedelta(seconds=settings.USER_OFFLINE_TIMEOUT):
            return "Away"
    return "Offline"
