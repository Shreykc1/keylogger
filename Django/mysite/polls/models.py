from django.db import models



class Party(models.Model):
    name = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} , {self.votes}"

class Voter(models.Model):
    whom = models.ForeignKey(Party, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} , {self.whom}" 
    
    
