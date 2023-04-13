from django.db import models
from django.conf import settings

#Create your models here.
class UserDetails(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='userdetails')
    pno = models.CharField(max_length=10)
    dob = models.DateField()
    city = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    securityQues = models.TextField(max_length=50)
    securityAns = models.TextField(max_length=50)
    bio = models.TextField(max_length=200)

    def __str__(self):
        return self.user.username
    
class Preferences(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='preferences')
    age = models.JSONField(default=list)
    gender = models.JSONField(default=list)
    maritalStatus = models.JSONField(default=list)
    travelFrequency = models.JSONField(default=list)
    tripType = models.JSONField(default=list)
    budget = models.JSONField(default=list)
    travelCompanion = models.JSONField(default=list)
    communicationStyle = models.JSONField(default=list)
    interests = models.JSONField(default=list)
    kindOfTrips = models.JSONField(default=list)
    travelDestination = models.JSONField(default=list)
    stays = models.JSONField(default=list)
    travelMotivation = models.JSONField(default=list)
    requirement = models.JSONField(default=list)
    modeOfTravel = models.JSONField(default=list)
    travelPace = models.JSONField(default=list)
    eatingPlaces = models.JSONField(default=list)
    accomodations = models.JSONField(default=list)

    def __str__(self):
        return self.user.username
    
class PublishedTrips(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='publishedtrips')
    leavingFrom = models.CharField(max_length=20)
    goingTo = models.CharField(max_length=20)
    startDate = models.DateField()
    endDate = models.DateField()
    noOfPersons = models.IntegerField()
    #noOfDays = models.IntegerField()

    def __str__(self):
        return self.user.username 

    # def calculate_no_of_days(self):
    #     self.noOfDays = int(self.endDate - self.startDate)
    #     return self.noOfDays

    # def save(self):
    #     self.noOfPersons = self.calculate_no_of_days()
    #     super(PublishedTrips, self).save()

# class TripHistory(models.Model):
#     trip_id = models.ForeignKey(PublishedTrips, on_delete=models.CASCADE)
#     username = models.ForeignKey(UserDetails, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.username

# class Confirmation(models.Model):
#     trip_id = models.ForeignKey(PublishedTrips, on_delete=models.CASCADE)
#     username = models.ForeignKey(UserDetails, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.username

