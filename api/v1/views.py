from django.db.models import Sum, F, FloatField, Count
from django_filters import rest_framework as django_filters

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from api.v1.serializers import ExamSerializer

from schoolapp.models import Exam


class CustomPagination(PageNumberPagination):
    page_size_query_param = 'per_page'


class CustomFilter(django_filters.FilterSet):
    date_from = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    date_to = django_filters.DateFilter(field_name='date', lookup_expr='lte')

    @property
    def qs(self):
        show = self.request.GET.get('show')
        teacher_name = self.request.GET.get('teacher_name')
        course_name = self.request.GET.get('course_name')
        sort_by = self.request.GET.get('sort_by')
        group_by = self.request.GET.get('group_by')

        queryset = super(CustomFilter, self).qs

        if show and 'grade' in show:
            queryset = queryset.values().annotate(
                grade=((Sum(F('score'), output_field=FloatField())) / (Count(F('date'), output_field=FloatField()))))
        elif show:
            shows = show.split(',')
            queryset = queryset.values(*shows)

        if teacher_name:
            queryset = queryset.filter(os__in=teacher_name.split(','))

        if course_name:
            queryset = queryset.filter(os__in=course_name.split(','))

        if group_by:
            group_by = group_by.split(',')
            if show and 'grade' in show:
                queryset = queryset.values('student_name', 'course_name').distinc()
            else:
                queryset = queryset.values(*group_by).distinct()

        if sort_by:
            sort_by = sort_by.split(':')

            if len(sort_by) == 2 and sort_by[1] == 'desc':
                queryset = queryset.order_by('-{}'.format(sort_by[0]))
            else:
                queryset = queryset.order_by(sort_by[0])

        return queryset

    class Meta:
        model = Exam
        fields = '__all__'


class ExamViewSet(viewsets.ModelViewSet):

    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
    pagination_class = CustomPagination
    filterset_fields = '__all__'
    ordering_fields =  '__all__'
    filterset_class = CustomFilter
