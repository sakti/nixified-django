from django.http import HttpResponse
from django.conf import settings

content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Hello, World!</title>
</head>
<body style="background-color: {settings.BACKGROUND_COLOR};">
    <h1>Hello, World!</h1>
</body>
</html>
"""


def index(request):
    return HttpResponse(content, content_type="text/html")
