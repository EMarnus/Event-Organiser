from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages


def index(request):
    return render(request, "index.html", {})


def booking(request):
    # Calling 'validWeekday' Function to Loop days:
    validateWeekdays = validWeekday(31)

    if request.method == 'POST':
        type = request.POST.get('type')
        day = request.POST.get('day')
        if type is None:
            messages.success(request, "Please Select A Type!")
            return redirect('booking')

        # Store day and type in django session:
        request.session['day'] = day
        request.session['type'] = type

        return redirect('bookingSubmit')

    return render(request, 'booking.html', {
            'validateWeekdays': validateWeekdays,
        })


def bookingSubmit(request):
    user = request.user
    times = [
        "12 AM",
        "1 AM",
        "2 AM",
        "3 AM",
        "4 AM",
        "5 AM",
        "6 AM",
        "7 AM",
        "8 AM",
        "9 AM",
        "10 AM",
        "11 AM",
        "12 PM",
        "1 PM",
        "2 PM",
        "3 PM",
        "4 PM",
        "5 PM",
        "6 PM",
        "7 PM",
        "8 PM",
        "9 PM",
        "10 PM",
        "11 PM",
    ]

    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    # Get stored data from django session:
    day = request.session.get('day')
    type = request.session.get('type')

    # Only show the time of the day that has not been selected before:
    hour = checkTime(times, day)
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if type is not None:
            if day <= maxDate and day >= minDate:
                messages.success(request, "Appointment Saved!")
                return redirect('index')
            else:
                messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A Type!")

    return render(request, 'bookingSubmit.html', {
        'times': hour,
    })


def validWeekday(days):
    # Loop days you want in the next 21 days:
    today = datetime.now()
    weekdays = []
    for i in range(0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays


def userPanel(request):
    user = request.user
    appointments = Appointment.objects.filter(user=user).order_by(
        'day', 'time')
    return render(request, 'userPanel.html', {
        'user': user,
        'appointments': appointments,
    })


def userUpdate(request, id):
    appointment = Appointment.objects.get(pk=id)
    userdatepicked = appointment.day
    # Copy  booking:
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')

    # 24h if statement in template:
    delta24 = (userdatepicked).strftime('%Y-%m-%d') >= (
        today + timedelta(days=1)).strftime('%Y-%m-%d')
    # Calling 'validWeekday' Function to Loop days you want in the next 21 days:
    validateWeekdays = validWeekday(31)

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')

        # Store day and service in django session:
        request.session['day'] = day
        request.session['service'] = service

        return redirect('userUpdateSubmit', id=id)

    return render(request, 'userUpdate.html', {
            'validateWeekdays': validateWeekdays,
            'delta24': delta24,
            'id': id,
        })
