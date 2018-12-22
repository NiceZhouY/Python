from django.db import models

# Create your models here.

class UserMessage(models.Model):
    name = models.CharField(max_length=20, null=True, blank="", default="", verbose_name="用户名")
    email = models.EmailField(verbose_name=u"邮箱")
    message = models.CharField(max_length=100, verbose_name=u"留言信息")

    class Meta:
        verbose_name=u"用户留言信息"
        verbose_name_plural=verbose_name