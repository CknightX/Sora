from flask import Flask,render_template,send_file,current_app
from . import main,utils


@main.route('/<path:path>')
def index(path):
    config=current_app.config
    base_path=config.get('BASE_PATH')

    res=None
    context=dict()
    # 本地文件路径
    if path.endswith('/'):
        path=path[:-1]
    local_path=base_path+path

    file_type=utils.get_file_type(local_path)

    if file_type=='dir':
        context['current_path']=path
        context['files']=utils.get_dir_files(local_path)
        context['local_path']=local_path
        res=render_template('files-list.html',**context)
    else:
        if file_type=='video':
            res=send_file(local_path,conditional=True)
        else:
            res=send_file(local_path,conditional=True,as_attachment=True,attachment_filename=path)

    return res

@main.route('/')
def index2():
    config=current_app.config
    base_path=config.get('BASE_PATH')

    path='/'
    context=dict()
    local_path=base_path+path
    context['current_path']=path
    context['files']=utils.get_dir_files(local_path)
    return render_template('files-list.html',**context)
