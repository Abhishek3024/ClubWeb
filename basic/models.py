from django.db import models
from django.utils import timezone
# Create your models here.
CLUB_NAMES = (
    ('ArtClub', 'ART CLUB'),
    ('DanceClub', 'DANCE CLUB'),
    ('MusicClub', 'MUSIC CLUB'),
    ('CodingClub', 'CODING CLUB'),
    ('GamingClub', 'GAMING CLUB'),
    ('PhotographyClub', 'PHOTOGRAPHY CLUB'),
)


class Post(models.Model):
    club_name = models.CharField(max_length=20, choices=CLUB_NAMES)
    title = models.CharField(max_length=120)
    information = models.TextField()
    post_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.club_name + '--' + self.title


class Club(models.Model):
    club_name = models.CharField(max_length=20, choices=CLUB_NAMES)
    club_secretary = models.CharField(max_length=20)
    club_joint_secretary = models.CharField(max_length=20)
    club_info = models.TextField()
    club_logo = models.FileField()

    def __str__(self):
        return self.club_name


class ClubMember(models.Model):
    club = models.ForeignKey(Club)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
