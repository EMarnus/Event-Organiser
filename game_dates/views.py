from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import CommentForm
from django.contrib import messages
from django.core.paginator import Paginator

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


def index(request):
    user = request.user
    appointments = Appointment.objects.all().order_by('day')

    # Paginator
    paginator = Paginator(appointments, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nums = "a" * page_obj.paginator.num_pages

    return render(request, 'index.html', {
        'appointments': appointments,
        'user': user,
        'page_obj': page_obj,
        'nums': nums,
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
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=30)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    # Get stored data from django session:
    day = request.session.get('day')
    type = request.session.get('type')

    hour = checkTime(times, day)
    if request.method == 'POST':
        time = request.POST.get('time')
        description = request.POST.get('description')
        content = request.POST.get('content')

        if type is not None:
            if day <= maxDate and day >= minDate:
                AppointmentForm = Appointment.objects.get_or_create(
                    user=user,
                    type=type,
                    day=day,
                    time=time,
                    description=description,
                    content=content,
                )
                messages.success(request, "Appointment Saved!")
                return redirect('index')
            else:
                messages.success(
                    request, "The Selected Date Isn't In The Correct Time \
                        Period!")
        else:
            messages.success(request, "Please Select A Type!")

    return render(request, 'bookingSubmit.html', {
        'times': hour,
    })


def bookingDetails(request, booking_id):
    booking = Appointment.objects.get(pk=booking_id)
    comments = booking.comments.filter(approved=True).order_by('created_on')
    attending = booking.number_of_attendees()
    tentative = booking.number_of_tentative()

    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.name = request.user
            new_comment.post = Appointment.objects.get(id=booking_id)
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'bookingDetails.html', {
        'booking': booking,
        'comments': comments,
        'comment_form': comment_form,
        'attending': attending,
        'tentative': tentative,
        })


def attendingEvent(request, booking_id):
    event = get_object_or_404(Appointment, id=request.POST.get('booking_id'))

    if event.attending.filter(id=request.user.id).exists():
        event.attending.remove(request.user)
    else:
        event.attending.add(request.user)

    return HttpResponseRedirect(
        reverse('bookingDetails', args=[str(booking_id)]))


def tentativeEvent(request, booking_id):
    event = get_object_or_404(Appointment, id=request.POST.get('booking_id'))

    if event.tentative.filter(id=request.user.id).exists():
        event.tentative.remove(request.user)
    else:
        event.tentative.add(request.user)

    return HttpResponseRedirect(
        reverse('bookingDetails', args=[str(booking_id)]))


def checkTime(times, day):
    """
    Only show the time of the day that has not been selected before
    """
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
    z = datetime.strptime(x, '%Y-%m-%d')
    y = z.strftime('%A')


def userPanel(request):
    user = request.user
    appointments = Appointment.objects.filter(user=user).order_by(
        'day', 'time')
    return render(request, 'userPanel.html', {
        'user': user,
        'appointments': appointments,
    })


def bookingUpdate(request, booking_id):
    booking = Appointment.objects.get(pk=booking_id)
    booking_id = booking.pk
    userdatepicked = booking.day
    # Copy  booking:
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')

    # 24h if statement in template:
    delta24 = (userdatepicked).strftime('%Y-%m-%d') >= (
        today + timedelta(days=1)).strftime('%Y-%m-%d')
    # Calling 'validWeekday' Function to Loop days you want in the next 31:
    validateWeekdays = validWeekday(31)

    if request.method == 'POST':
        type = request.POST.get('type')
        day = request.POST.get('day')

        # Store in django session:
        request.session['day'] = day
        request.session['type'] = type
        request.session['booking_id'] = booking_id

        return redirect('bookingUpdateSubmit',  booking_id)

    return render(request, 'bookingUpdate.html', {
            'validateWeekdays': validateWeekdays,
            'delta24': delta24,
            'booking_id': booking_id,
            'booking': booking
        })


def bookingUpdateSubmit(request, booking_id):
    booking = Appointment.objects.get(pk=booking_id)
    user = request.user
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=30)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    type = request.session.get('type')
    booking_id = request.session.get('booking_id')

    hour = checkEditTime(times, day, booking_id)
    if request.method == 'POST':
        time = request.POST.get('time')
        date = dayToWeekday(day)
        description = request.POST.get('description')
        content = request.POST.get('content')

        if type is not None:
            if day <= maxDate and day >= minDate:
                AppointmentForm = Appointment.objects.filter(
                    pk=booking_id).update(
                        user=user,
                        type=type,
                        day=day,
                        time=time,
                        description=description,
                        content=content,
                )
                messages.success(request, "Appointment Updated!")
                return redirect('index')
            else:
                messages.success(
                    request, "The Selected Date Isn't In The Correct Time \
                        Period!")
        else:
            messages.success(request, "Please Select A Type!")
        return redirect('postDetails')

    return render(request, 'bookingUpdateSubmit.html', {
        'booking_id': booking_id,
        'times': hour,
        'booking': booking,
    })


def bookingDelete(request, booking_id):
    booking = Appointment.objects.get(pk=booking_id)
    if booking.user == request.user:
        booking.delete()
        messages.success(request, "Event deleted!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, "You do not have permission to delete \
            this Event")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def checkEditTime(times, day, booking_id):
    x = []
    appointment = Appointment.objects.get(pk=booking_id)
    time = appointment.time
    for k in times:
        if (Appointment.objects.filter(day=day, time=k).count() < 1
                or time == k):
            x.append(k)
    return x


def userUpdate(request, id):
    appointment = Appointment.objects.get(pk=id)
    userdatepicked = appointment.day
    # Copy booking:
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')

    # 24h if statement in template:
    delta24 = (userdatepicked).strftime('%Y-%m-%d') >= (today + timedelta(
        days=1)).strftime('%Y-%m-%d')
    # Calling 'validWeekday' Function to Loop days you
    # want in the next 21 days:
    weekdays = validWeekday(22)

    # Only show the days that are not full:
    validateWeekdays = isWeekdayValid(weekdays)

    return render(request, 'userUpdate.html', {
            'weekdays': weekdays,
            'validateWeekdays': validateWeekdays,
            'delta24': delta24,
            'id': id,
        })


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
