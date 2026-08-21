from apps.administration.models import SocietyInfo


class SocietyInfoService:
    @staticmethod
    def get_society_info():
        obj, _ = SocietyInfo.objects.get_or_create(
            id=1,
            defaults={
                "name": "Epsilon Homes",
                "registration_no": "MAH/2015/EPH-001",
                "address": "Survey No. 45, Baner Road, Baner",
                "city": "Pune",
                "state": "Maharashtra",
                "pin_code": "411045",
                "phone": "+91 20 2560 8800",
                "email": "admin@epsilonhomes.in",
            }
        )
        return obj

    @staticmethod
    def update_society_info(data):
        obj = SocietyInfoService.get_society_info()
        for key, value in data.items():
            setattr(obj, key, value)
        obj.save()
        return obj