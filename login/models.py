from django.db import models

# Create your models here.
class UserTable(models.Model):
    #employee=models.ForeignKey(EmployeeTable,on_delete=models.CASCADE)
    empid=models.CharField(max_length=100,null=False,unique=True)
    emp_name=models.CharField(max_length=100,null=False)
    email_id=models.CharField(max_length=100,null=False,unique=True)
    proj_manager=models.CharField(max_length=100,null=False)
    password=models.CharField(max_length=100,null=False)
    secret_code=models.CharField(max_length=100,null=False)
    role=models.CharField(max_length=10,null=False,choices=(('Admin','Admin'),('User','User')),default='User')

    def __str__(self):
        return self.empid


class EmployeeTable(models.Model):
    empid=models.CharField(max_length=100,null=False,unique=True)
    emp_name=models.CharField(max_length=100,null=False)
    email_id=models.CharField(max_length=100,null=False,unique=True)
    proj_manager=models.CharField(max_length=100,null=False)