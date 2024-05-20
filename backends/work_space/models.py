from django.db import models
from django.conf import settings


class WorkSpace(models.Model):
    "Model definition for WorkSpace."
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    type_workspace = models.CharField(
        max_length=50,
        choices=[
            ("service", "Service"),
            ("store", "Store"),
            ("office", "Office"),
            ("warehouse", "Warehouse")
        ],
        default="service",
    )
    director = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.SET_NULL,
                                 null=True)
    opening_date = models.DateField(verbose_name="Дата открытия точки",
                                    auto_now_add=True)

    class Meta:
        verbose_name = "WorkSpace"
        verbose_name_plural = "WorkSpaces"

    def __str__(self):
        return f'{self.title} - {self.address}'
