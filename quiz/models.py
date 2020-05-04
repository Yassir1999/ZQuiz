from django.db import models
from django.urls.base import reverse


class Category(models.Model):
    name = models.CharField(max_length=50, default="General")
    text = models.CharField(max_length=50, default=" ")
    creationDate = models.DateField('Created on ')
    imagePath = models.CharField(max_length=250, default="imageurl")

    def get_absolute_url(self):
        return reverse('searchbycategory', kwargs={'Category_id': self.id})

    def __str__(self):
        return self.name

class Quiz(models.Model):
    title = models.CharField(max_length=50)
    hits = models.IntegerField(default=0)
    mainQuestion = models.CharField(max_length=250)
    genre = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    publicationDate = models.DateField('Published on ')
    quizImagePath = models.CharField(max_length=250, default="pixabay-unsplash")
    isTest = models.IntegerField(default=1)
    result1 = models.CharField(max_length=50, blank=True)
    result2 = models.CharField(max_length=50, blank=True)
    result3 = models.CharField(max_length=50, blank=True)
    result4 = models.CharField(max_length=50, blank=True)
    result5 = models.CharField(max_length=50, blank=True)
    result6 = models.CharField(max_length=50, blank=True)
    result7 = models.CharField(max_length=50, blank=True)
    result8 = models.CharField(max_length=50, blank=True)
    result9 = models.CharField(max_length=50, blank=True)
    result1img = models.CharField(max_length=250, blank=True)
    result2img = models.CharField(max_length=250, blank=True)
    result3img = models.CharField(max_length=250, blank=True)
    result4img = models.CharField(max_length=250, blank=True)
    result5img = models.CharField(max_length=250, blank=True)
    result6img = models.CharField(max_length=250, blank=True)
    result7img = models.CharField(max_length=250, blank=True)
    result8img = models.CharField(max_length=250, blank=True)
    result9img = models.CharField(max_length=250, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.title, self.mainQuestion)

    def get_absolute_url(self):
        return reverse('startQuiz', kwargs={'Quiz_id': self.id})


class QuizViews(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    ip = models.CharField(max_length=16)


class Question(models.Model):
    question = models.CharField(max_length=250, default="if Test, remember that the question's worth should be the max of the options worths")
    questionWorth = models.IntegerField(default=1)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50, blank=True)
    option4 = models.CharField(max_length=50, blank=True)
    option5 = models.CharField(max_length=50, blank=True)
    option1Worth = models.IntegerField(default=1)
    option2Worth = models.IntegerField(default=0)
    option3Worth = models.IntegerField(default=0, null=True)
    option4Worth = models.IntegerField(default=0, null=True)
    option5Worth = models.IntegerField(default=0, null=True)
    option1img = models.CharField(max_length=250, blank=True)
    option2img = models.CharField(max_length=250, blank=True)
    option3img = models.CharField(max_length=250, blank=True)
    option4img = models.CharField(max_length=250, blank=True)
    option5img = models.CharField(max_length=250, blank=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
