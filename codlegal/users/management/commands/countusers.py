from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

UserModel = get_user_model()


class Command(BaseCommand):
    help = "Helps to count the number of users by requested Roles"

    def add_arguments(self, parser):
        parser.add_argument("role", type=str, help="User Role : AD / CL")

    def handle(self, *args, **options):
        role = options['role']
        count = UserModel.objects.filter(role=role).count()
        # print("Total Advocate Users are " + str(count))
        self.stdout.write(
            self.style.SUCCESS('Total %s Users are "%s"' % (role, count))
        )
