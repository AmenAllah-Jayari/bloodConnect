from django.db import models
from django.contrib.auth.models import User

class Donneur(models.Model):
    CHOICES_SANG = [
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')
    ]
    CHOICES_SEXE = [('M', 'Homme'), ('F', 'Femme')]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    groupe_sanguin = models.CharField(max_length=3, choices=CHOICES_SANG)
    sexe = models.CharField(max_length=1, choices=CHOICES_SEXE)
    date_naissance = models.DateField()
    ville = models.CharField(max_length=100)
    actif = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='profiles/', default='profiles/default.png', null=True, blank=True)
    adresse = models.TextField(null=True, blank=True)
    telephone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.groupe_sanguin})"

class Hopital(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200)
    adresse = models.TextField()
    ville = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    est_valide = models.BooleanField(default=True)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom