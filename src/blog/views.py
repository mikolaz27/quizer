from random import randint

from django.http import HttpResponse
from faker import Faker

from blog.models import Blog, Entity


def create_blog(request) -> HttpResponse:
    faker = Faker()
    saved_blog = Entity(
        blog=[
            Blog(
                name=faker.word(),
                text=faker.paragraph(nb_sentences=5),
                author=faker.first_name(),
                rating=randint(1, 100),
                category=faker.word(),
            )
            for _ in range(10)
        ],
        headline=faker.paragraph(nb_sentences=1),
    ).save()

    return HttpResponse(f"Done {saved_blog}")


def all_blogs(request):
    blogs = Entity.objects.all()
    print(blogs)

    return HttpResponse(f"Done {[blog.headline for blog in blogs]}")
