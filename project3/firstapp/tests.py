from django.test import TestCase
from datetime import date
from firstapp.models import Topic, Webpage, AcessRecord


class FirstAppModelTests(TestCase):
    def test_topic_creation(self):
        topic = Topic.objects.create(top_name="Search Engine")
        self.assertEqual(str(topic), "Search Engine")

    def test_webpage_and_access_record_relationships(self):
        topic = Topic.objects.create(top_name="Cloud")
        webpage = Webpage.objects.create(topic=topic, name="Google Cloud", url="https://cloud.google.com")
        self.assertEqual(str(webpage), "Google Cloud")

        record = AcessRecord.objects.create(name=webpage, date=date(2026, 11, 1))
        self.assertEqual(str(record), "2026-11-01")
        self.assertEqual(record.name.topic.top_name, "Cloud")
