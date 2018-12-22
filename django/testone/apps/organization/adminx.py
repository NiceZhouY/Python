# -*- coding: utf-8 -*-
"""
@author: Yi_Zhou
"""
import xadmin

from .models import *

class CityDictAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class CourseOrgAdmin(object):
    list_display = ['name', 'fav_num', 'address']
    search_fields = ['name', 'fav_num', 'address']
    list_filter = ['name', 'fav_num', 'address']


class TeacherAdmin(object):
    list_display = ['nama', 'work_years', 'fav_num', 'add_time']
    search_fields =['nama', 'work_years', 'fav_num', 'add_time']
    list_filter = ['nama', 'work_years', 'fav_num', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
