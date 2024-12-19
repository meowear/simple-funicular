from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    context = {
        'video_url': '/media/videoroll.mp4'  # URL to your MP4 file
    }
    return render(request, 'video_player/index.html', context)
