from tortoise import models, fields


class User(models.Model):
    username = fields.CharField(max_length=64, unique=True)
    first_name = fields.CharField(max_length=64, null=True)
    last_name = fields.CharField(max_length=64, null=True)
    password_hash = fields.CharField(max_length=128)

    def __str__(self) -> str:
        return self.username
