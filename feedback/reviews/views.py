from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .forms import ReviewForm
from .models import Review


class ReviewView(CreateView):
    model = Review
    # fields = '__all__'
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
    

# Create your views here.
# def review(request):
#     if request.method == 'POST':
#         # entered_username = request.POST['username']
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # review = Review(user_name=form.cleaned_data["user_name"], 
#             #        review_text=form.cleaned_data["review_text"], 
#             #        rating=form.cleaned_data["rating"])
#             # review.save()
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviewForm()
#     return render(request, "reviews/review.html", {
#         "form": form
#     })


# class ThankyouView(View):
#     def get(self, request):
#         return render(request, "reviews/thank_you.html")
    
class ThankyouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"  # name used in the template

    def get_queryset(self) -> QuerySet[Any]:
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=1)
        return data
    

class SingleReviewView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        favorite_id = self.request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)