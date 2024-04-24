from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.core.cache import cache
from django.utils.translation import activate
from django.contrib.sessions.middleware import SessionMiddleware
from django.utils import timezone


class LanguageMiddleware(SessionMiddleware):
    def process_request(self, request):
        super().process_request(request)
        language = request.POST.get('language')
        if language is not None:
            activate(language)
            request.session['lang'] = language
        elif 'lang' in request.session:
            activate(request.session['lang'])


class ActiveUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated and request.user.is_active:
            user_id = request.user.id
            if not cache.get('seen_%s' % user_id):
                cache.set('seen_%s' % user_id, timezone.localtime(timezone.now()), settings.USER_LAST_SEEN_TIMEOUT)

        return response
