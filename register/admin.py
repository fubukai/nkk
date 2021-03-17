from django.contrib import admin
from .models import Course_D, MT_User, List_Dept, List_Emp, Course_Director, Check_Loginerror, Check_Staff_End,Subject,Competency,Relation_subject,Relation_comp
admin.site.register(Course_D)
admin.site.register(MT_User)
admin.site.register(List_Dept)
admin.site.register(List_Emp)
admin.site.register(Course_Director)
admin.site.register(Check_Loginerror)
admin.site.register(Check_Staff_End)
admin.site.register(Subject)
admin.site.register(Competency)
admin.site.register(Relation_subject)
admin.site.register(Relation_comp)
# Register your models here.
