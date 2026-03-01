from django.db import models
import json

class CodingQuestion(models.Model):
    topic = models.CharField(max_length=100)
    question = models.TextField()
    test_cases_json = models.TextField(help_text="Store test cases as JSON: [{'input': '...', 'output': '...'}]")

    def get_test_cases(self):
        return json.loads(self.test_cases_json)