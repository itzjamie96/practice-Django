from django.db import models

# Create your models here.
class Poll(models.Model):
    
    question = models.TextField()

    choice1 = models.CharField(max_length=100)
    choice2 = models.CharField(max_length=100)

    choice1_count = models.IntegerField(default=0)
    choice2_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    def p1(self):
        if self.choice1_count>0 or self.choice2_count>0:
            return round(self.choice1_count/(self.choice1_count + self.choice2_count)*100)
        else:
            return 0

    def p2(self):
        if self.choice1_count>0 or self.choice2_count>0:
            return round(self.choice2_count/(self.choice1_count + self.choice2_count)*100)
        else:
            return 0



class Comment(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content
    
    
