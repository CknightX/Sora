from flask import Blueprint
main=Blueprint('main',__name__)

# 创建蓝图main的路由
from . import views
from . import template_filter 
