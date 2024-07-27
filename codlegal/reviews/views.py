from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from reviews import forms, models


# Create your views here.

@login_required
def submit_app_review(request):
    user = request.user
    if request.method == "POST":
        review_form = forms.PlatformReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = user
            review.save()
    else:
        review_form = forms.PlatformReviewForm()
    return render(request, "reviews/submit_review.html", {"form": review_form})


def view_app_reviews(request):
    reviews = models.PlatformReview.objects.all()
    return render(request, "reviews/list_reviews.html", context={"reviews": reviews})

def update_app_review(request, pk):
    review = models.PlatformReview.objects.get(pk=pk)
    if request.method == "POST":
        review_form = forms.PlatformReviewForm(data=request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
    else:
        review_form = forms.PlatformReviewForm(instance=review)
    return render(request, "reviews/update_platform_review.html", {"form": review_form})
