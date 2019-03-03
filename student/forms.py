#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ypp
from django import forms
from student.models import Student


class StudentForm(forms.Form):

    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字！')

    class Meta:
        model = Student
        fields = ('name', 'sex', 'profession', 'email', 'qq', 'phone')
