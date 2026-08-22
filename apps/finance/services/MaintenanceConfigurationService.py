from apps.finance.models.MaintenanceConfiguration import MaintenanceConfiguration


class MaintenanceConfigurationService:

    @staticmethod
    def get_configuration():
        return MaintenanceConfiguration.objects.filter(
            is_deleted=False
        ).first()

    @staticmethod
    def update_configuration(data):
        configuration = MaintenanceConfiguration.objects.filter(
            is_deleted=False
        ).first()

        if configuration:
            for field, value in data.items():
                setattr(configuration, field, value)

            configuration.save()

        else:
            configuration = MaintenanceConfiguration.objects.create(
                **data
            )

        return configuration