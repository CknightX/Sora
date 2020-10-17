from flask import Flask,render_template,send_file
from . import main,utils

base_path='D:/'

@main.route('/<path:path>')
def index(path):
    context=dict()
    # 本地文件路径
    local_path=base_path+path
    if local_path.endswith('/'):
        local_path=local_path[:-1]
    print(local_path)
    file_type=utils.get_file_type(local_path)
    if file_type=='dir':
        context['current_path']=path
        context['files']=utils.get_dir_files(local_path)
        return render_template('files-list.html',**context)
    elif file_type=='file':
        return send_file(local_path,conditional=True)

@main.route('/')
def index2():
    path='/'
    context=dict()
    local_path=base_path+path
    context['current_path']=path
    context['files']=utils.get_dir_files(local_path)
    return render_template('files-list.html',**context)