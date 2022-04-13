from factory import Faker, SubFactory
from factory.django import DjangoModelFactory, ImageField

from events.tests.factories import UserFactory
from pycompanies.models import Company, UserCompanyProfile


class CompanyFactory(DjangoModelFactory):
    class Meta:
        model = Company

    name = Faker('company')
    owner = SubFactory(UserFactory)
    photo = ImageField(color='blue')
    rank = 1


class UserCompanyProfileFactory(DjangoModelFactory):
    class Meta:
        model = UserCompanyProfile

    user = SubFactory(UserFactory)
    company = SubFactory(CompanyFactory)
