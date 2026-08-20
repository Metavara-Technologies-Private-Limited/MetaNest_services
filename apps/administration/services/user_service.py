from django.contrib.auth import get_user_model

User = get_user_model()


class AdminUserService:
    @staticmethod
    def get_all_users():
        return User.objects.all().order_by('-id')

    @staticmethod
    def get_user_by_id(user_id):
        return User.objects.filter(id=user_id).first()

    @staticmethod
    def toggle_user_status(user_id):
        user = AdminUserService.get_user_by_id(user_id)
        if user:
            user.is_active = not user.is_active
            user.save()
            return user
        return None