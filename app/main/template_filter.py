
from flask import Flask,render_template,send_file,current_app
from . import main,utils

@main.app_template_filter('is_video_file')
def is_media_file(filename):
    media_suffix=['.mp4']
    for suffix in media_suffix:
        if filename.endswith(suffix):
            return True
    return False

