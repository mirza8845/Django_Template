from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Meetup, Participant
# from .forms import RegistrationForm
from .forms import RegistrationForm

# Create your views here.

def index(request):
    meetups = Meetup.objects.all()
    # meetups= [
    #     {"title": "Meetup 1", "location": "New York", "slug": "a-first-meetup"},
    #     {"title": "Meetup 2", "location": "Paris", "slug": "a-second-meetup"}
    # ]
    return render(request, "meetups/index.html", {
                      'meetups': meetups
                   })

def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        # selected_meetup= {
        #     "title": "Meetup 1",
        #     "location": "New York",
        #     "slug": "a-first-meetup",
        #     "disc": "This is first meetup discription here......."
        # }
        if request.method == "GET":
            registration_form = RegistrationForm()

        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, was_created = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration', meetup_slug=meetup_slug)

        return render(request, "meetups/meetup-details.html", {
            'meetup_details': selected_meetup,
            'meetup_found': selected_meetup.slug,
            'form': registration_form
        })
    except Exception as exc:
        return render(request, "meetups/meetup-details.html", {
            'meetup_found': False
        })

def confirm_registration(request, meetup_slug ):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration_success.html', {
                  'origanizer_data': meetup.organizer_email
                })