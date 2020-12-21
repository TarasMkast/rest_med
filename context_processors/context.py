from contacts.models import Social, MapMarker, Contacts
from config.models import *


def context(request):
    soc = Social.objects.all()
    marker = MapMarker.objects.all()
    con = Contacts.objects.all()

    license_field = LicenseField.objects.all()
    bg = Background.objects.filter(is_active=True)

    lat = None
    long = None

    for obj in marker:
        long = obj.latitude
        lat = obj.longitude

    return {'social': soc,
            'lat': lat,
            'long': long,
            'contacts': con,
            'license': license_field,
            'background': bg,
            }
