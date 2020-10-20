import os
from flask import make_response
import mimetypes


class File:
    def __init__(self,filename,filepath):
        self.filename=filename
        self.filepath=filepath
        # 路径后约定携带 /
        if not self.filepath.endswith('/'):
            self.filepath+='/'
        self.filetype=get_file_type(self.filepath+self.filename)

def get_dir_files(path):
    try:
        files=os.listdir(path)
    except os.error:
        #TODO
        return []
        pass
    res=[]
    for file in files:
        res.append(File(file,path))

    return res


def get_file_type(path):
    if os.path.isdir(path):
        return 'dir'
    if path.endswith('mp4'):
        return 'video'

def resolve_file(path):
    f=open(path,'rb')
    f.seek(0,os.SEEK_END)
    filesize=f.tell()
    f.seek(0,os.SEEK_SET)
    file_stat=os.fstat(f.fileno())
    ctype=mimetypes.guess_type(path)

    resp=make_response(f)
    resp.status=200
    resp.headers['Content-Type']=ctype
    resp.headers['Content-Length']=str(file_stat[6])
    resp.headers['Last-Modified']=''
    resp.headers['Connection']='close'

    return resp



if __name__=='__main__':
    print(get_dir_files('c:/1Myfiles')[0].filename)

