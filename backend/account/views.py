from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .mixins import SuperuserAccessMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from Book.models import Book, BookPublisher, BookSubject, BookType, EducationYear
from django.contrib.auth import get_user_model
from .forms import ProfileForm
from django.http import HttpResponse
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage


# Create your views here.


class BookListView(LoginRequiredMixin, ListView):
    queryset = Book.objects.all()
    template_name = 'registration/home.html'


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = [
        'title',
        'slug',
        'description',
        'image',
        'author',
        'number_of_pages',
        'weight',
        'released_year',
        'international_standard_book_number',
        'price',
        'status',
        'amount',
        'book_publisher',
        'book_type',
        'book_subject',
        'book_education_year',

    ]
    template_name = 'registration/book_create_update.html'


class BookDeleteView(SuperuserAccessMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('account:home')
    template_name = 'registration/book_confirm_delete.html'


class BookUpdateView(SuperuserAccessMixin, UpdateView):
    model = Book
    fields = [
        'title',
        'slug',
        'description',
        'image',
        'author',
        'number_of_pages',
        'weight',
        'released_year',
        'international_standard_book_number',
        'price',
        'status',
        'amount',
        'book_publisher',
        'book_type',
        'book_subject',
        'book_education_year',

    ]
    template_name = 'registration/book_create_update.html'


class BookPublisherListView(LoginRequiredMixin, ListView):
    queryset = BookPublisher.objects.all()
    template_name = 'registration/book_publisher_list.html'


class BookPublisherCreateView(LoginRequiredMixin, CreateView):
    model = BookPublisher
    fields = [
        'title',
        'slug',
        'description',
    ]
    template_name = 'registration/book_publisher_create_update.html'


class BookPublisherDeleteView(SuperuserAccessMixin, DeleteView):
    model = BookPublisher
    success_url = reverse_lazy('account:book-publisher-list')
    template_name = 'registration/book_confirm_delete.html'


class BookPublisherUpdateView(SuperuserAccessMixin, UpdateView):
    model = BookPublisher
    fields = [
        'title',
        'slug',
        'description',
    ]
    template_name = 'registration/book_publisher_create_update.html'


class BookSubjectListView(LoginRequiredMixin, ListView):
    queryset = BookSubject.objects.all()
    template_name = 'registration/book_subject_list.html'


class BookSubjectCreateView(LoginRequiredMixin, CreateView):
    model = BookSubject
    fields = [
        'title',
        'slug',
    ]
    template_name = 'registration/book_subject_create_update.html'


class BookSubjectDeleteView(SuperuserAccessMixin, DeleteView):
    model = BookSubject
    success_url = reverse_lazy('account:book-subject-list')
    template_name = 'registration/book_confirm_delete.html'


class BookSubjectUpdateView(SuperuserAccessMixin, UpdateView):
    model = BookSubject
    fields = [
        'title',
        'slug',
    ]
    template_name = 'registration/book_subject_create_update.html'


class BookTypeListView(LoginRequiredMixin, ListView):
    queryset = BookType.objects.all()
    template_name = 'registration/book_type_list.html'


class BookTypeCreateView(LoginRequiredMixin, CreateView):
    model = BookType
    fields = [
        'title',
        'slug',
    ]
    template_name = 'registration/book_type_create_update.html'


class BookTypeDeleteView(SuperuserAccessMixin, DeleteView):
    model = BookType
    success_url = reverse_lazy('account:book-type-list')
    template_name = 'registration/book_confirm_delete.html'


class BookTypeUpdateView(SuperuserAccessMixin, UpdateView):
    model = BookType
    fields = [
        'title',
        'slug',
    ]
    template_name = 'registration/book_type_create_update.html'


class EducationYearListView(LoginRequiredMixin, ListView):
    queryset = EducationYear.objects.all()
    template_name = 'registration/education_year_list.html'


class EducationYearCreateView(LoginRequiredMixin, CreateView):
    model = EducationYear
    fields = [
        'title',
        'slug',
    ]
    template_name = 'registration/education_year_create_update.html'


class EducationYearDeleteView(SuperuserAccessMixin, DeleteView):
    model = EducationYear
    success_url = reverse_lazy('account:education-year-list')
    template_name = 'registration/book_confirm_delete.html'


class EducationYearUpdateView(SuperuserAccessMixin, UpdateView):
    model = EducationYear
    fields = [
        'title',
        'slug',
    ]
    template_name = 'registration/education_year_create_update.html'


# view to show profile of user
class Profile(UpdateView):
    model = get_user_model()
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('account:profile')
    form_class = ProfileForm

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

    def get_object(self, **kwargs):
        return get_user_model().objects.get(pk=self.request.user.pk)


class Register(CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        context = {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        }
        mail_subject = 'لینک فعالسازی حساب کاربری .'
        message = render_to_string('registration/active_account.html', context=context)
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return HttpResponse('برای کامل شدن ثبت نام لطفا حساب کاربری خود را فعال کنید.')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('ممنون برای ثبت نام در سایت برای وارد شدن به حساب کاربری <a/> کلیک کنید "a href="/login>.')
    else:
        return HttpResponse('لینک فعالسازی منقضی شده است.')
