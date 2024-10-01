import threading
import os
from django.conf import settings
from .utils import tenant_db_from_request
from django.shortcuts import redirect

THREAD_LOCAL = threading.local()


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the tenant database from the request
        db = tenant_db_from_request(request)
        setattr(THREAD_LOCAL, "DB", db)

        print('-------------------------------- Middleware Start ------------------------------------')
        print(db)
        print('-------------------------------- Middleware End ------------------------------------')

        # Set tenant-specific MEDIA_ROOT
        if db:

            tenant_media_root = os.path.join(settings.BASE_DIR, "Media", db)
            settings.MEDIA_ROOT = tenant_media_root  # Override MEDIA_ROOT for the tenant
        else:
            tenant_media_root = os.path.join(settings.BASE_DIR, "Media", 'default')
            settings.MEDIA_ROOT = tenant_media_root  # Override MEDIA_ROOT for the tenant


        response = self.get_response(request)
        return response


def get_current_db_name():
    return getattr(THREAD_LOCAL, "DB", None)


def set_db_for_router(db):
    setattr(THREAD_LOCAL, "DB", db)