from django import forms

class SaveForm(forms.Form):
   Emp_id = forms.CharField(label = 'รหัสพนักงาน',max_length = 100)