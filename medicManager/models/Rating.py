from medicManager.models import *


class Rating(models.Model):
    user = models.ForeignKey(User, related_name="rater", on_delete=models.CASCADE)
    user_rated = models.ForeignKey(User, related_name="rated", on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    opinion = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return "Rater: {} | Rated: {}".format(self.user.first_name, self.user_rated)
