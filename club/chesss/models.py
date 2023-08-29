from django.db import models

# Create your models here.
class club(models.Model):
    name = models.CharField(max_length=25)

class member(models.Model):
    name = models.CharField(max_length=25)
    club = models.ForeignKey(club,on_delete=models.CASCADE)


class player(models.Model):
    name = models.CharField(max_length=25)
    member = models.ForeignKey(member,on_delete=models.CASCADE  )


class tournament(models.Model):
    name = models.CharField(max_length=25)
    club = models.ForeignKey(club,on_delete=models.CASCADE)
    player = models.ManyToManyField(player)



class match(models.Model):
    player_one = models.ForeignKey(player,on_delete=models.CASCADE,related_name='player_id_set')
    player_two = models.ForeignKey(player,on_delete=models.CASCADE,related_name='player_two_set')
    tournament = models.ForeignKey(tournament,on_delete=models.CASCADE,related_name='tournament_set')
    winner= models.ForeignKey(player,on_delete=models.CASCADE,related_name='winner_id_set')
    play_date_time = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
