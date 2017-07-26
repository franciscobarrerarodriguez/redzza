from django.shortcuts import redirect


# Decorador para exigir que la peticion se realice bajo ajax.
def require_AJAX(function):
    """Return a bad request instance if the view is not using AJAX
    function -- the view
    """

    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return redirect('index')
        return function(request, *args, **kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
