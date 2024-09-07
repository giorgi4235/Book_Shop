from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm,PasswordChangeForm,ProfileForm


from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User,Profile
from django.http import HttpResponse


def sign_up_view(request):

    template_name = 'registration/register.html'

    form = UserRegistrationForm()
    
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        print("register: ",form.data)
        if form.is_valid():
            print("register form is valid: ",form.cleaned_data)
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            activation_url = f'http://127.0.0.1:8000/activate/{user.uuid}'
            send_mail(
                'user activattion',
                activation_url,
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            msg = 'your user is created and ativation link is sent to {}'.format(user.email)
            messages.success(request, msg)

            return redirect("sign_in")

    context = {
        'form': form
    }

    return render(request,template_name,context)

def login_view(request):

    template_name = 'registration/login.html'
    form = UserLoginForm()

    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=email, password=password)
            print("user: ",user)
            if user:

                login(request, user)
                if user.status == "1":
                    return redirect("my_books")
                else:
                    return redirect("book_list")
            else:
                messages.success(request, f'{email} does not exist')



    context = {
        'form': form
    }

    return render(request,template_name,context)

def user_activate_view(request,id):

    print("activaciis linkidan moxda viius datrigereba")

    user = User.objects.get(id=id)
    user.is_active = True
    user.save()

    return HttpResponse('your user is successfuly activated')



def logout_view(request):

    logout(request)

    return redirect('sign_in')


# def acitivate_url(request,uuid):
#     user = User.objects.get(uuid=uuid)
#     user.is_active = True
#     user.save()
#     print('user activaciashi shemovida')
#     return HttpResponse('your user is successfuly activated')


def change_password(request):
    template_name = 'registration/password_change.html'
    
    user = request.user
    form = PasswordChangeForm(user)
    if request.POST:
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            print('pass form---',form.cleaned_data)
            if request.user.check_password(form.cleaned_data.get('current_password')) and form.cleaned_data.get('password') == form.cleaned_data.get('repeat_password'):
                #user = form.save(commit=False)
                #user.password = form.cleaned_data.get('password')
                user.set_password(str(form.cleaned_data['password']))
                user.save()
                login(request, user)
                return redirect('products:product-list')
            else:
                print('error test-----')
                messages.success(request, 'current password does not match')
        else:
            print('errors---',form.errors)
    context = {
        'form':form,
    }
    return render(request,template_name,context)


def editProfile(request):

    template_name = 'registration/editProfile.html'

    user = request.user
    
    form = ProfileForm(instance=user.profile)

    if request.method == "POST":

        form = ProfileForm(request.POST,instance=user.profile)

        if form.is_valid():
            data = form.save()

            

            data.save()

            return redirect("book_list")


    context = {
        'form': form
    }

    return render(request,template_name,context)




# def editProfile(request):
#     template_name = 'registration/editProfile.html'

#     profile = request.user.profile
#     form = ProfileForm(instance=profile)

#     if request.POST:
#         form = ProfileForm(request.POST,instance=profile)
#         if form.is_valid():
#             print('form---',form.cleaned_data)
#             data = form.save(commit=False)

#             data.filled = True

#             data.save()

#             return redirect('products:product-list')

#     context = {
#         'form':form
#     }

#     return render(request,template_name,context)


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important: Updates the session with the new password
            # logout(request)  # Log out the user after password change
            return redirect('password_change_done')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/profile.html', {'form': form})

