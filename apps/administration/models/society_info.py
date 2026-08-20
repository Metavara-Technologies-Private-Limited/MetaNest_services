from django.db import models


class SocietyInfo(models.Model):
    name = models.CharField(max_length=255, default="Epsilon Homes")
    registration_no = models.CharField(max_length=100, default="MAH/2015/EPH-001")
    address = models.TextField(default="Survey No. 45, Baner Road, Baner")
    city = models.CharField(max_length=100, default="Pune")
    state = models.CharField(max_length=100, default="Maharashtra")
    pin_code = models.CharField(max_length=10, default="411045")
    phone = models.CharField(max_length=20, default="+91 20 2560 8800")
    email = models.EmailField(default="admin@epsilonhomes.in")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "administration"
        db_table = "society_info"
        verbose_name_plural = "Society Info"

    def __str__(self):
        return self.name