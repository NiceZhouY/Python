# -*- coding: utf-8 -*-
"""
@author: Yi_Zhou
"""
import xadmin

from .models import *

class CourseAdmin(object):
    list_display = ['name', 'degree', 'leran_times', 'students']
    search_fields = ['name', 'degree', 'leran_times', 'students']
    list_filter = ['name', 'degree', 'leran_times', 'students']


class LessonAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name', 'add_time']
    list_filter = ['name', 'add_time']


class VideoAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name', 'add_time']
    list_filter = ['name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name', 'add_time']
    list_filter = ['name', 'add_time']



xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)