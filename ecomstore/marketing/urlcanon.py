from django.http import get_host, HttpResponsePermanentRedirect
from ecomstore import settings

class URLCanonicalizationMiddleware(object):
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        if not settings.DEBUG:
            """ only perform the redirect if not debug mode """
            protocol = 'https://' if request.is_secure() else 'http://'
            host = get_host(request)
            new_url = ''
            try:
                if host in settings.CANON_URLS_TO_REWRITE:
                    new_url = protocol + settings.CANON_URL_HOST + request.get_full_path()
            except AttributeError:
                if host != settings.CANON_URL_HOST:
                    new_url = protocol + settings.CANON_URL_HOST + request.get_full_path()
            if new_url:
                return HttpResponsePermanentRedirect(new_url)