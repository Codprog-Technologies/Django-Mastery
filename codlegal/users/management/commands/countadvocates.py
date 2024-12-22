from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

UserModel = get_user_model()


class Command(BaseCommand):
    help = "Helps to count the number of Advocates Registered in Our Application"

    def handle(self, *args, **options):
        count = UserModel.objects.filter(role=UserModel.RoleChoices.ADVOCATE).count()
        # print("Total Advocate Users are " + str(count))
        self.stdout.write(
            self.style.SUCCESS('Total Advocate Users are "%s"' % count)
        )
