from django.db import models
from authentications.models import User

class Scrap(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    scrap_description = models.TextField()
    scrap_image = models.ImageField(upload_to='scrap_images/')
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date_submitted}"

class ScrapOrder(models.Model):
    scrap = models.ForeignKey(Scrap, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Collected', 'Collected')], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.status}"

class ScrapCollected(models.Model):
    scrap_order = models.ForeignKey(ScrapOrder, on_delete=models.CASCADE)
    collected_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collector')
    sales_amount = models.DecimalField(max_digits=10, decimal_places=2)
    collected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Scrap collected from Order {self.scrap_order.id} by {self.collected_by.username}"
