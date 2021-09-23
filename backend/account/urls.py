from django.contrib.auth import views
from django.urls import path
from .views import (
    BookListView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    BookPublisherListView,
    BookPublisherCreateView,
    BookPublisherUpdateView,
    BookPublisherDeleteView,
    BookSubjectListView,
    BookSubjectCreateView,
    BookSubjectUpdateView,
    BookSubjectDeleteView,
    BookTypeListView,
    BookTypeCreateView,
    BookTypeUpdateView,
    BookTypeDeleteView,
    EducationYearListView,
    EducationYearCreateView,
    EducationYearUpdateView,
    EducationYearDeleteView,

)

app_name = 'account'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    #
    # path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #
    # path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

urlpatterns += [
    path('', BookListView.as_view(), name='home'),
    path('book/create/', BookCreateView.as_view(), name='book-create'),
    path('book/update/<int:pk>', BookUpdateView.as_view(), name='book-update'),
    path('book/delete/<int:pk>', BookDeleteView.as_view(), name='book-delete'),
    path('book-publisher/list/', BookPublisherListView.as_view(), name='book-publisher-list'),
    path('book-publisher/create/', BookPublisherCreateView.as_view(), name='book-publisher-create'),
    path('book-publisher/update/<int:pk>', BookPublisherUpdateView.as_view(), name='book-publisher-update'),
    path('book-publisher/delete/<int:pk>', BookPublisherDeleteView.as_view(), name='book-publisher-delete'),
    path('book-subject/list/', BookSubjectListView.as_view(), name='book-subject-list'),
    path('book-subject/create/', BookSubjectCreateView.as_view(), name='book-subject-create'),
    path('book-subject/update/<int:pk>', BookSubjectUpdateView.as_view(), name='book-subject-update'),
    path('book-subject/delete/<int:pk>', BookSubjectDeleteView.as_view(), name='book-subject-delete'),
    path('book-type/list/', BookTypeListView.as_view(), name='book-type-list'),
    path('book-type/create/', BookTypeCreateView.as_view(), name='book-type-create'),
    path('book-type/update/<int:pk>', BookTypeUpdateView.as_view(), name='book-type-update'),
    path('book-type/delete/<int:pk>', BookTypeDeleteView.as_view(), name='book-type-delete'),
    path('education-year/list/', EducationYearListView.as_view(), name='education-year-list'),
    path('education-year/create/', EducationYearCreateView.as_view(), name='education-year-create'),
    path('education-year/update/<int:pk>', EducationYearUpdateView.as_view(), name='education-year-update'),
    path('education-year/delete/<int:pk>', EducationYearDeleteView.as_view(), name='education-year-delete'),
]
