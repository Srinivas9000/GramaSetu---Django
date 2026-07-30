from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
<<<<<<< HEAD
from .forms import FeedbackForm, VillageIssueForm



def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

=======
from .forms import FeedbackForm


@login_required(login_url='login')
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


>>>>>>> 94fe287e9a4711d1c632e1ba87a93186096f6d30
def panchaiyeti(request):
    return render(request, "panchaiyeti.html")


def temples(request):
    return render(request, "temples.html")


def tourism(request):
    return render(request, "tourism.html")

def farming(request):
    return render(request, "farming.html")

def school(request):
    return render(request, "school.html")

def sports(request):
    return render(request, "sports.html")

<<<<<<< HEAD
def elections(request):
    return render(request, "elections.html")    


def ward_1(request):
    return render(request, "ward-1.html")

def ward_2(request):
    return render(request, "ward-2.html")

def ward_3(request):
    return render(request, "ward-3.html")

def ward_4(request):
    return render(request, "ward-4.html")

def ward_5(request):
    return render(request, "ward-5.html")

def ward_6(request):
    return render(request, "ward-6.html")

def ward_7(request):
    return render(request, "ward-7.html")

def ward_8(request):
    return render(request, "ward-8.html")

def ward_9(request):
    return render(request, "ward-9.html")

def ward_10(request):
    return render(request, "ward-10.html")

def govtactivities(request):
    return render(request, "govtactivities.html")

def employeeinformation(request):
    return render(request, "employeeinformation.html")

def localactivities(request):
    return render(request, "localactivities.html")


=======
>>>>>>> 94fe287e9a4711d1c632e1ba87a93186096f6d30
def services(request):

    if request.method == "POST":
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "✅ Thank you! Your feedback was sent successfully."
            )

            return redirect('services')   # prevents resubmit problem

    else:
        form = FeedbackForm()

    return render(request, "services.html", {"form": form})


<<<<<<< HEAD

=======
>>>>>>> 94fe287e9a4711d1c632e1ba87a93186096f6d30
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        messages.success(request, "Registration successful")
        return redirect('login')

    return render(request, 'register.html')


def login_view(request):

    # already logged in → go home
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect('login')

<<<<<<< HEAD
from django.shortcuts import render
@login_required
def issue(request):

    if request.method=="POST":

        form=VillageIssueForm(request.POST,request.FILES)

        if form.is_valid():

            issue=form.save(commit=False)

            issue.user=request.user

            issue.save()

            messages.success(request,"Issue Submitted Successfully.")

            return redirect("community")

    else:

        form=VillageIssueForm()
    return render(request, "issue.html")

from .models import VillageIssue

@login_required
def community(request):

    issues = VillageIssue.objects.all().order_by("-created_at")

    return render(request,"community.html",{

        "issues":issues

    })

from .models import VillageIssue

def issue(request):

    if request.method=="POST":

        issue=request.POST.get("issue")

        media=request.FILES.get("media")

        VillageIssue.objects.create(

            issue=issue,

            media=media

        )

        return redirect("community")

    return render(request,"issue.html")

from django.shortcuts import get_object_or_404

@login_required
def delete_issue(request,issue_id):

    issue=get_object_or_404(VillageIssue,id=issue_id)

    if request.user==issue.user or request.user.is_superuser:

        issue.delete()

        messages.success(request,"Issue Deleted Successfully")

    return redirect("community")

from .models import PanchayatGallery

def panchaiyeti(request):

    if request.method == "POST":

        name = request.POST.get("name")

        media = request.FILES.get("media")

        PanchayatGallery.objects.create(

            name=name,

            media=media

        )

        return redirect("panchaiyeti")

    gallery = PanchayatGallery.objects.order_by("-uploaded_at")

    return render(request,
                  "panchaiyeti.html",
                  {
                      "gallery": gallery
                  })
=======


>>>>>>> 94fe287e9a4711d1c632e1ba87a93186096f6d30
