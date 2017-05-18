from django import forms
from .models import VideoUrl
class VideoForm(forms.Form):
    class Meta:
        model = VideoUrl
        fields = ('subject', 'url', 'comment', 'vod_id',)
        # video_subject = forms.CharField(label='VOD Name', max_length=100)
        # video_url = forms.CharField(label='url', max_length=500)
        # video_comment = forms.CharField(label='comment', max_length=500)
