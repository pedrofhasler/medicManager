from medicManager.models import *


class Province(models.Model):
    name = models.CharField(null=False, max_length=20)
    status = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)
