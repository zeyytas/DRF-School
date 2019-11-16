

from rest_framework import routers
from api.v1.views import ExamViewSet

router = routers.DefaultRouter()

router.register(r'exam', ExamViewSet)