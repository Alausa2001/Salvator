#!/usr/bin/python3
from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.login import *
from api.v1.views.user_med_info import *
from api.v1.views.records import *
from api.v1.app import *
