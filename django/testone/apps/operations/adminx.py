# -*- coding: utf-8 -*-
"""
@author: Yi_Zhou
"""
import xadmin

from .models import *

class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_tiem']
    search_fields = ['name', 'mobile', 'course_name', 'add_tiem']
    list_filter = ['name', 'mobile', 'course_name', 'add_tiem']


class CourseCommentsAdmin(object):
    list_display = ['comments', 'add_time']
    search_fields = ['comments', 'add_time']
    list_filter = ['comments', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['fav_id', 'fav_type', 'add_tiem']
    search_fields = ['fav_id', 'fav_type', 'add_tiem']
    list_filter = ['fav_id', 'fav_type', 'add_tiem']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read', 'add_time']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class UserCourseAdmin(object):
    pass

xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)