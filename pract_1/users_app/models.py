from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "users"

    def __str__(self):
        return self.email
    
class Profile(models.Model):
    # Зв'язок 1-до-багатьох: один користувач може мати кілька профілів
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles')
    
    # Поля згідно з твоєю діаграмою
    name = models.CharField(max_length=100)
    
    # null=True та blank=True дозволяють створити профіль, навіть якщо аватарки ще немає
    avatar = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "profiles"

    def __str__(self):
        return self.name
