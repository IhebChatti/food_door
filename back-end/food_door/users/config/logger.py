# from django.contrib.auth import user_logged_in, user_login_failed

from datetime import datetime, timedelta

import pytz

from users.models import UserLoginActivity

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def log_user_logged_in_success(sender, user, request):
    try:
        user_agent_info = request.META.get('HTTP_USER_AGENT', '<unknown>')[:255],
        user_login_activity_log = UserLoginActivity(login_IP=get_client_ip(request),
                                                    login_username=user.username,
                                                    user_agent_info=user_agent_info,
                                                    status='success')
        user.last_login = datetime.now(tz=pytz.utc)
        user.save()
        user_login_activity_log.save()
    except Exception:
        # log the error
        pass
        # error_log.error("log_user_logged_in request: %s, error: %s" % (request, e))

def log_user_logged_in_failed(sender, credentials, request): #pylint: disable=unused-argument
    try:
        user_agent_info = request.META.get('HTTP_USER_AGENT', '<unknown>')[:255],
        user_login_activity_log = UserLoginActivity(login_IP=get_client_ip(request),
                                                    login_username=credentials['email'],
                                                    user_agent_info=user_agent_info,
                                                    status='failed')
        user_login_activity_log.save()
    except Exception:
        # log the error
        pass
        # error_log.error("log_user_logged_in request: %s, error: %s" % (request, e))
