from ecomstore.accounts.models import UserProfile
from ecomstore.accounts.forms import UserProfileForm

def retrieve(request):
    ''' note that this requires an authenticated
    user before we try calling it '''
    try:
        profile = request.user.get_profile()
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
        profile.save()
    return profile

def set(request):
    profile = retrieve(request)
    profile_form = UserProfileForm(request.POST, instance=profile)
    profile_form.save()
