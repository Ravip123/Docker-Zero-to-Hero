from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <html>
    <head>
        <title>Docker + Django Demo</title>
    </head>
    <body style="font-family: Arial; text-align:center; margin-top:50px;">
        <h1>🚀 Docker + Django Running Successfully!</h1>
        <p>Containerized Django application deployed locally.</p>

        <h3>System Status</h3>
        <ul style="display:inline-block; text-align:left;">
            <li>✅ Docker Container Running</li>
            <li>✅ Django Server Running</li>
            <li>✅ Port 8000 Exposed</li>
        </ul>

        <br><br>

        <button onclick="alert('Hello Ravi! Docker is working 🎉')">
            Click Me
        </button>
    </body>
    </html>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
