from django.db import models


# Create your models here.


class Student(models.Model):
    """学生类"""
    sex_items = [
        (0, '女'),
        (1, '男'),
        (2, '未知'),
    ]
    student_items = [
        (0, '申请'),
        (1, '通过'),
        (2, '拒绝'),
    ]
    name = models.CharField(max_length=128, verbose_name="姓名")
    sex = models.IntegerField(choices=sex_items, verbose_name="性别")
    profession = models.CharField(max_length=128, verbose_name='职业')
    email = models.EmailField(verbose_name="Email")
    qq = models.CharField(max_length=128, verbose_name="QQ")
    phone = models.CharField(max_length=128, verbose_name="电话")
    status = models.IntegerField(choices=student_items, default=0, verbose_name="申请状态")
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")

    def __str__(self):
        return '<Student: {}>'.format(self.name)

    class Meta:
        verbose_name = verbose_name_plural = "学员信息"



