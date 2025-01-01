from ninja.security import HttpBearer
from Staff.models import Staff


class ApiKeyAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            staff = Staff.objects.get(api_key=token)
            return staff.user
        except:
            return None