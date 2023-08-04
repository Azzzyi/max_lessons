from django.db import models

class Advertisement(models.Model):
     title = models.CharField("заголовок", max_length= 128)
     description = models.TextField("описание")
     price = models.DecimalField("цена",max_digits=10,decimal_places=2)
     auction = models.BooleanField("торг", help_text="отметьте, если торг уместен")
     create_at = models.DateField(auto_now_add=True)
     update_at = models.DateField(auto_now=True)

     def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"
    
     class Meta:
        db_table = "advertisements"
