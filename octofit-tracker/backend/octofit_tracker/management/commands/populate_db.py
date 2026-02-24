from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from djongo import models

# Define models for teams, activities, leaderboard, and workouts
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users (superheroes)
        users = [
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'team': marvel},
            {'username': 'captainamerica', 'email': 'cap@marvel.com', 'team': marvel},
            {'username': 'spiderman', 'email': 'spiderman@marvel.com', 'team': marvel},
            {'username': 'batman', 'email': 'batman@dc.com', 'team': dc},
            {'username': 'superman', 'email': 'superman@dc.com', 'team': dc},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com', 'team': dc},
        ]
        for u in users:
            user = User.objects.create_user(username=u['username'], email=u['email'], password='password123')
            # Optionally, link user to team if you have a profile model

        # Create activities
        Activity.objects.create(user='ironman', activity_type='Running', duration=30)
        Activity.objects.create(user='batman', activity_type='Cycling', duration=45)
        Activity.objects.create(user='spiderman', activity_type='Swimming', duration=25)
        Activity.objects.create(user='superman', activity_type='Flying', duration=60)

        # Create leaderboard
        Leaderboard.objects.create(user='ironman', points=100)
        Leaderboard.objects.create(user='batman', points=90)
        Leaderboard.objects.create(user='superman', points=110)

        # Create workouts
        Workout.objects.create(name='Full Body Blast', description='A workout for all major muscle groups.')
        Workout.objects.create(name='Cardio Burn', description='High intensity cardio session.')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
