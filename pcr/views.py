from django.http import HttpResponse


def results(request):
    return HttpResponse("Hello from pcr results.")
