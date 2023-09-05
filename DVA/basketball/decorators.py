from functools import wraps
from django.shortcuts import redirect

def custom_login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if 'score_keeper_id' in request.session:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')  
    return _wrapped_view
