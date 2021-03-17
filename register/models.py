from django.db import models
from django.contrib.auth.models import User

class MT_User(models.Model):
    PK_User = models.AutoField(primary_key=True)
    User_ID = models.CharField(max_length=10,null=True)
    Division_ID = models.CharField(max_length=5,null=True)
    Permit_Group = models.CharField(max_length=5,null=True)
    Key_Date =  models.DateTimeField(auto_now_add=True)
    

class Course_D(models.Model):
    PK_Course_D = models.AutoField(primary_key=True)
    Course_ID = models.CharField(max_length=15, unique=True)
    Course_Name = models.CharField(max_length=300,null=True)
    CourseType_ID = models.CharField(max_length=2,null=True)
    Batch_Type = models.CharField(max_length=1,null=True)
    Batch = models.CharField(max_length=300,null=True)
    Start_Date = models.DateField(null=True)
    End_Date = models.DateField(null=True)
    Duration = models.IntegerField(null=True)
    Location = models.CharField(max_length=300,null=True)
    Area_ID = models.CharField(max_length=3,null=True)
    Number_App = models.IntegerField(null=True)
    Number_People = models.IntegerField(null=True)
    BudgetApp_1 = models.DecimalField(max_digits=13, decimal_places=2,null=True)
    BudgetApp_2 = models.DecimalField(max_digits=13, decimal_places=2,null=True)
    BudgetPay_1 = models.DecimalField(max_digits=13, decimal_places=2,null=True)
    BudgetPay_2 = models.DecimalField(max_digits=13, decimal_places=2,null=True)
    Key_By = models.CharField(max_length=10,null=True)
    Key_Date = models.DateField(auto_now_add=True)
    RegisterStatus = models.BooleanField(null=True)
    RegisterType = models.CharField(max_length=15,null=True)
    Start_Time = models.DateTimeField(null=True)
    End_Time = models.DateTimeField(null=True)
    status = models.IntegerField(null=True, default=1)
    Access_level = models.IntegerField(null=True,default=1)
    def __str__(self):
        return self.Course_Name

#แบ่งตาม conpetency
class Competency(models.Model):
    Comp_ID = models.AutoField(primary_key=True)
    Comp_name = models.CharField(max_length=100,null=True)
    Comp_type = models.CharField(max_length=2,null=True)# MC CC FC
    Comp_level = models.IntegerField(null=True,default=1)
    def __str__(self):
        return self.Comp_name

#รายวิชา
class Subject(models.Model):
    Subject_ID = models.AutoField(primary_key=True)
    Subject_name = models.CharField(max_length=150,null = True)
    Description = models.CharField(max_length=300,null = True)
    Url_location = models.CharField(max_length=100, blank = True)
    ref_cou = models.ForeignKey(Course_D, related_name='referrence_course',on_delete=models.CASCADE,null=True)
    #ref_comp = models.ForeignKey(Competency, related_name='Reference',on_delete = models.CASCADE,null=True)
    def __str__(self):
        return self.Subject_name

#วิธีเรียกใช้งาน related_name คือ ชื่อในrelated_nameตามด้วย_ _ชื่อตัวแปร เช่น Course_score__ID
class Relation_comp(models.Model):
    Course_ID = models.ForeignKey(Course_D,related_name='Course_relation', on_delete=models.CASCADE,null = True)
    Subject_ID = models.ForeignKey(Subject, related_name='Subject_relation',on_delete=models.CASCADE,null=True)

#ตารางความสัมพันธ์ subject com
class Relation_subject(models.Model):
    Mc_no = models.ForeignKey(Competency, related_name='Ref_Mc',on_delete=models.CASCADE,null=True)
    Subject_no = models.ForeignKey(Subject, related_name='Ref_sub',on_delete=models.CASCADE,null=True)

class List_Dept(models.Model):
    PK_List = models.AutoField(primary_key=True)
    ref_course = models.ForeignKey(Course_D, related_name='List_Dept_Course_D',on_delete = models.CASCADE,null= True)
    ref_group = models.CharField(max_length=5,null=True)
    dept = models.CharField(max_length=30,null=True)  
    number_dept = models.IntegerField(null=True)
    number_stamp = models.IntegerField(null=True)
    status = models.IntegerField(default=1, null=True)
    # status 1= on, 0 = offf

class List_Emp(models.Model):
    PK_List_Emp = models.AutoField(primary_key=True)
    ref_course = models.ForeignKey(Course_D, related_name='List_Emp_Course_D',on_delete = models.CASCADE,null= True,default='0')
    E_ID = models.CharField(max_length=10,null=True,blank=True)
    Fullname = models.CharField(max_length=70,null=True,blank=True)
    Position = models.CharField(max_length=20,null=True,default='หผ.')
    Level = models.CharField(max_length=2,null=True,default='08')
    Dep = models.CharField(max_length=100,null=True,blank=True)
    Dept_code = models.CharField(max_length=20,null=True,blank=True,default='0000')
    Email = models.EmailField(blank=True,null=True,max_length=100)
    Tel = models.CharField(blank=True,null=True,max_length=15)
    Regist_Date = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=1, null=True)
    # status 1= on, 0 = off

    def __str__(self):
        return self.E_ID

class Course_sub(models.Model):
    title = models.CharField(max_length=100,null=True)
    area = models.CharField(max_length=10,null=True)
    number_student = models.IntegerField(default=0,null=True)
    ref_course = models.ForeignKey(Course_D, related_name='Sub_Course_D',on_delete = models.CASCADE,null= True,default='0')

class Course_Director(models.Model):
    E_ID = models.CharField(max_length=10,null=True,blank=True)
    Position = models.CharField(max_length=20,null=True,default='อก.')
    Dept_code = models.CharField(max_length=20,null=True,blank=True,default='0000')
    Area = models.CharField(max_length=10,null=True,blank=True,default='สนญ.')
    Year = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.E_ID

class Check_Loginerror(models.Model):
    E_ID = models.CharField(max_length=10,null=True,blank=True)
    Case = models.CharField(max_length=200,null=True,blank=True)
    Date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.E_ID

class Check_Staff_End(models.Model):
    E_ID = models.CharField(max_length=10,null=True,blank=True)
    Status = models.CharField(max_length=200,null=True,blank=True)
    Exp_Date = models.CharField(max_length=100,null=True,blank=True)
    Comment = models.CharField(max_length=100,null=True,blank=True)
    Name = models.CharField(max_length=200,null=True,blank=True)
    Position = models.CharField(max_length=20,null=True,default='อก.')
    Level = models.CharField(max_length=20,null=True,default='อก.')
    Dept_code = models.CharField(max_length=20,null=True,blank=True,default='0000')
    Dept_Short = models.CharField(max_length=200,null=True,blank=True,default='0000')
    Update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.E_ID

























# Create your models here.
