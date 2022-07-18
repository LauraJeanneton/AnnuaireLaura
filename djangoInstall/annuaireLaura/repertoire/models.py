from django.db import models
from django.urls import reverse

class Contact(models.Model):
    # Champs
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=20, null=False)
    prenom = models.CharField(max_length=30, null=False)
    email=models.CharField(max_length=50, null=True)


    # Metadatas
    class Meta:
        ordering = ['nom','-prenom']

    # Méthodes
    def get_absolute_url(self):
        return reverse('details', args=[str(self.id)])

    def __str__(self):
        return self.nom + " "+self.prenom
