from django.db import models

# Create your models here.
class University(models.Model):
    university_name = models.CharField(max_length=50)

    def __str__(self):
        return self.university_name




class StudentVendor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_email = models.EmailField(verbose_name="Student Email", unique=True, max_length=255)
    vendor_email = models.EmailField(verbose_name="Vendor Email", unique=True, max_length=255)
    reg_no = models.CharField(unique=True, max_length=255)
    is_vendor = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=25)
    address = models.CharField(max_length=255, blank=True)
    student_university = models.ForeignKey(University, on_delete=models.CASCADE)

    profile_image = models.ImageField(upload_to='uploads/profile', blank=False, null=False, default="static/images/profile.jpg")

    @staticmethod
    def get_student_vendor_by_reg_no(reg_no):
        try:
            return StudentVendor.objects.get(reg_no=reg_no)
        except:
            return None
        
    def get_full_name(self):
        return self.last_name + " " + self.first_name
    
    def __str__(self):
        return self.student_email

