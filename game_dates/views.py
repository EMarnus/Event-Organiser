from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages


def index(request):
    user = request.user
    appointments = Appointment.objects.order_by('day')
    return render(request, "index.html", {
        'appointments': appointments,
        'user': user,
    })


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
                AppointmentForm = Appointment.objects.get_or_create(
                        user=user,
                        type=type,
                        day=day,
                        time=time,
                    )
                messages.success(request, "Appointment Saved!")
                return redirect('index')
            else:
                messages.success(
                    request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A Type!")

    return render(request, 'bookingSubmit.html', {
        'times': hour,
    })


"""
Only show the time of the day that has not been selected before
"""
def checkTime(times, day):
    x = []
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x


"""
Loops days you want
"""
def validWeekday(days):
    today = datetime.now()
    weekdays = []
    for i in range(0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays


def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')


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
    # Calling 'validWeekday' Function to Loop days you want in the next 31:
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


def userUpdateSubmit(request, id):
    user = request.user
    times = [
        "3 PM", "3:30 PM", "4 PM", "4:30 PM", "5 PM",
        "5:30 PM", "6 PM", "6:30 PM", "7 PM", "7:30 PM"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    service = request.session.get('service')

    # Only show the time of the day that has not been selected before and the time he is editing:
    hour = checkEditTime(times, day, id)
    appointment = Appointment.objects.get(pk=id)
    userSelectedTime = appointment.time
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if service is not None:
            if day <= maxDate and day >= minDate:
                if Appointment.objects.filter(day=day, time=time).count() < 1 or userSelectedTime == time:
                    AppointmentForm = Appointment.objects.filter(pk=id).update(
                        user=user,
                        service=service,
                        day=day,
                        time=time,
                    )
                    messages.success(request, "Appointment Edited!")
                    return redirect('index')
                else:
                    messages.success(
                        request, "The Selected Time Has Been Reserved Before!")
            else:
                messages.success(
                    request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A Service!")
        return redirect('userPanel')

    return render(request, 'userUpdateSubmit.html', {
        'times': hour,
        'id': id,
    })


"""
Only show the time of the day that has not been selected before
"""
def checkEditTime(times, day, id):
    x = []
    appointment = Appointment.objects.get(pk=id)
    time = appointment.time
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1 or time == k:
            x.append(k)
    return x


def organiserPanel(request):
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=31)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime
    # Only show the Appointments 31 days from today
    items = Appointment.objects.filter(
        day__range=[minDate, maxDate]).order_by('day', 'time')

    return render(request, 'organiserPanel.html', {
        'items': items,
    })
