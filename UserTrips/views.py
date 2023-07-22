from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import UserDetails, Preferences, PublishedTrips
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
import random

# Create your views here.

def LandingPage(request):
    return render(request,"index.html")
	
def signup(request):

    if request.method == 'POST':
        firstName = request.POST['fname']
        lastName = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['pass']
        cpassword = request.POST['passconfirm']
        pno = request.POST['contact']
        dob = request.POST['dob']
        city = request.POST['city']
        gender = request.POST['gender']
        securityQues = request.POST['secques']
        securityAns = request.POST['secans']
        bio = request.POST['bio']
        c = str(cluster())

        if password == cpassword:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email already exists!')
                return redirect('signup')
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'User already exists!')
                return redirect('signup')
            else:
                user = User.objects.create_user(username = username , email = email, password = password, first_name=firstName, last_name=lastName)
                user.save()

            user = authenticate(request, username=username, password=password)
            login(request, user)

            user = request.user
            u = UserDetails.objects.create(
                user=user, 
                pno=pno, 
                city=city, 
                dob=dob, 
                gender=gender, 
                securityQues=securityQues, 
                securityAns=securityAns, 
                bio=bio,
                cluster = c
            )
  
            u.save()

                
            return redirect('preferences')         
    return render(request,"signup.html")

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        secAns = request.POST['secAns']

        user = authenticate(username = username, password = password)

        if user is not None and UserDetails.objects.filter(securityAns = secAns).exists():
            auth.login(request, user)
            return redirect('recomnendations')
        else:
            messages.info(request, 'Credentials Invalid!')
            return redirect('Login') 
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def cluster():
    r = random.randint(0,5)
    print(r)
    return r

@login_required
def preferences(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            age = request.POST.getlist('age_group')
            gender = request.POST.getlist('gender')
            maritalStatus = request.POST.getlist('maritalStatus')
            travelFrequency = request.POST.getlist('travelFrequency')
            tripType = request.POST.getlist('tripType')
            budget = request.POST.getlist('budget')
            travelCompanion = request.POST.getlist('travelCompanion')
            communicationStyle = request.POST.getlist('communicationStyle')
            interests = request.POST.getlist('interests')
            kindOfTrips = request.POST.getlist('kindOfTrips')
            travelDestination = request.POST.getlist('travelDestination')
            stays = request.POST.getlist('stays')
            travelMotivation = request.POST.getlist('travelMotivation')
            requirement = request.POST.getlist('requirement')
            modeOfTravel = request.POST.getlist('modeOfTravel')
            travelPace = request.POST.getlist('travelPace')
            eatingPlaces = request.POST.getlist('eatingPlaces')
            accomodations = request.POST.getlist('accomodations')

            p = Preferences.objects.create(
                user = user,
                age = age,
                gender = gender,
                maritalStatus = maritalStatus,
                travelFrequency = travelFrequency,
                tripType = tripType,
                budget = budget,
                travelCompanion = travelCompanion,
                communicationStyle = communicationStyle,
                interests = interests,
                kindOfTrips = kindOfTrips,
                travelDestination = travelDestination,
                stays = stays,
                travelMotivation = travelMotivation,
                requirement = requirement,
                modeOfTravel = modeOfTravel,
                travelPace = travelPace,
                eatingPlaces = eatingPlaces,
                accomodations = accomodations
            )
            p.save()
        #  # Preprocess the preferences
        # preferences = preprocess([preference_1, preference_2, ...])
        
        # # Load the pre-trained k-means model
        # kmeans=joblib.load('finalized_model.sav')
        # # Predict the cluster value
        # cluster = kmeans.predict(preferences)

        # model = load_model('kmeans_model.pkl')
        # encoder = load_encoder('encoder.pkl')

        #  # Preprocess the new data point
        # answers=age+gender+maritalStatus+travelFrequency+tripType+budget+travelCompanion+communicationStyle+interests+kindOfTrips+travelDestination+stays+travelMotivation+requirement+modeOfTravel+travelPace+eatingPlaces+accomodations
        # # print(answers)
        # cluster = predict_cluster(answers, model, encoder)

            return redirect('recomnendations')
    return render(request, 'preferences.html')

from .models import Preferences
#from mlxtend.preprocessing import TransactionEncoder
import numpy as np
#import pandas as pd

@login_required
def get_user_preferences(request):
    user = Preferences.objects.get(user=request.user)
    age = user.age
    gender = user.gender
    maritalStatus = user.maritalStatus
    travelFrequency = user.travelFrequency
    tripType = user.tripType
    budget = user.budget
    travelCompanion = user.travelCompanion
    communicationStyle = user.communicationStyle
    interests = user.interests
    kindOfTrips = user.kindOfTrips
    travelDestination = user.travelDestination
    stays = user.stays
    travelMotivation = user.travelMotivation
    requirement = user.requirement
    modeOfTravel = user.modeOfTravel
    travelPace = user.travelPace
    eatingPlaces = user.eatingPlaces
    accomodations = user.accomodations

    # answers=age+gender+maritalStatus+travelFrequency+tripType+budget+travelCompanion+communicationStyle+interests+kindOfTrips+travelDestination+stays+travelMotivation+requirement+modeOfTravel+travelPace+eatingPlaces+accomodations
    # print(answers)

    # return age, gender, maritalStatus, travelFrequency, tripType, budget, travelCompanion, communicationStyle, interests, kindOfTrips, travelDestination, stays, travelMotivation, requirement, modeOfTravel, travelPace, eatingPlaces, accomodations

    user_prefs_list = [
        age,
        gender,
        maritalStatus,
        travelFrequency,
        tripType,
        budget,
        travelCompanion,
        communicationStyle,
        interests,
        kindOfTrips,
        travelDestination,
        stays,
        travelMotivation,
        requirement,
        modeOfTravel,
        travelPace,
        eatingPlaces,
        accomodations]
    
    #my_df = pd.DataFrame(user_prefs_list)
    my_df = my_df.applymap(lambda x: x.split(','))
    my_df.head()

    size = my_df.shape[0]
    dataset = []
    for i in range(size):
        row_list = my_df.loc[i, :].values.flatten().tolist()
        flat_list = [item for sublist in row_list for item in sublist]
        dataset.append(flat_list)
        
    print(dataset)
    
    #from mlxtend.preprocessing import TransactionEncoder
    #te = TransactionEncoder()
    #te_ary = te.fit(dataset).transform(dataset)
    #df = pd.DataFrame(te_ary, columns=te.columns_)*1
    #Y=df.values

    #import joblib

    # "C:\Django\TripZ\UserTrips\finalized_model.sav"
    filename = 'C://Django//tripZ//UserTrips//finalized_model.sav'
    #kmeans_model = joblib.load(filename)

    #recommendations = kmeans_model.predict(Y)
    predicted_cluster = recommendations[0]
    print(predicted_cluster)

    
    return render(request, 'recommendations.html', {'recommendations': recommendations})

def recommendations(request):
    
    #if request.user.is_authenticated:
        
        if request.method == 'GET':
            leavingFrom = request.GET.get('goingFrom')
            goingTo = request.GET.get('goingTo')
            startDate = request.GET.get('startDate')
            endDate = request.GET.get('endDate')

            trips = PublishedTrips.objects.filter(
                leavingFrom=leavingFrom,
                goingTo=goingTo,
                startDate=startDate,
                endDate=endDate,
            )
            
            if trips.exists():
                users = User.objects.filter(publishedtrips__in=trips).distinct()
                # users = User.objects.filter(publishedtrips__in=trips).distinct().values_list('username', flat=True)
                user_details_list = []
                for user in users:
                    user_details = user.userdetails.get()
                    user_details_list.append(user_details)
                return {'users': users, 'user_details' : user_details_list }
                #return render(request, 'recommendations.html', {'users': users, 'user_details' : user_details_list })
            else:
                #return render(request, 'recommendations.html', {'users': []})
                return {'users': []}
        return redirect('recomndations')
        #return render(request, 'recomnendations.html')
    # else:
    #     return redirect('/')

from django.core.cache import cache
cache.clear()


def recomnendations(request):
    if request.user.is_authenticated:
        if request.GET:
            d = recommendations(request)
            return render(request, 'recommendations.html', d)
        
        user = request.user
        userD = UserDetails.objects.get(user=user)
        cluster = userD.cluster
        user_details = UserDetails.objects.filter(cluster__icontains = cluster)
        #u = User.objects.filter(user__in=user_details)
        u = [ud.user for ud in user_details] 
        print(u)
        return render(request, 'recomnendations.html', {'users':u})
    else:
        return redirect('/')
    

@login_required
def personalDashboard(request):
    user = request.user
    userD = UserDetails.objects.get(user = user)
    try : 
        publishedTrips = PublishedTrips.objects.filter(user = user)
        # c = publishedTrips.count()
        return render(request, 'personal-dashboard.html', { 'user': user, 'userD': userD, 'publishedTrips': publishedTrips, })

    except PublishedTrips.DoesNotExist:
        publishedTrips = None
        return render(request, 'personal-dashboard.html', { 'user': user, 'userD': userD })

@login_required
def publish_a_trip(request):
    if request.method == 'POST':
        user = request.user
        goingFrom = request.POST['goingFrom']
        goingTo = request.POST.get('goingTo')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        noOfPersons = request.POST.get('noOfPeople')

        p = PublishedTrips.objects.create(
            user=user,
            leavingFrom=goingFrom,
            goingTo=goingTo,
            startDate=startDate,
            endDate=endDate,
            noOfPersons = noOfPersons
        )
        p.save()
        return redirect('/personal-dashboard')
    return render(request, 'publish_trip.html')

   

def aboutus(request):
    return render(request,"aboutus.html")

def contactus(request):
    return render(request,"contactus.html")

def userprofile(request, username):
    if request.method == 'GET':
        user = get_object_or_404(User, username=username)
        user_details = UserDetails.objects.get(user = user)
        trips = PublishedTrips.objects.filter(user = user)
        return render(request, "userprofile.html", {'user' : user, 'user_details': user_details, 'trips' : trips})
    return render(request, "userprofile.html")

