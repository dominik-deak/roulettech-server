from django.core.management.base import BaseCommand
from todo.models import TodoItem


class Command(BaseCommand):
    help = "Seed the database with sample todo items"

    def handle(self, *args, **kwargs):
        # Clear the database
        TodoItem.objects.all().delete()

        # Insert mock data
        todos = [
            {"title": "Buy groceries", "completed": False},
            {"title": "Read a book", "completed": True},
            {"title": "Write some code", "completed": False},
            {"title": "Exercise for 30 minutes", "completed": True},
        ]

        for todo in todos:
            TodoItem.objects.create(**todo)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully."))
