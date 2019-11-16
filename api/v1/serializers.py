from rest_framework.serializers import ModelSerializer, SerializerMethodField

from schoolapp.models import Exam


class ExamSerializer(ModelSerializer):
    grade = SerializerMethodField()

    @staticmethod
    def get_grade(obj):

        try:
            if obj.get('grade') < 20:
                return 'F'
            elif 20 <= obj.get('grade') < 50:
                return 'E'
            elif 50 <= obj.get('grade') < 70:
                return 'D'
            elif 70 <= obj.get('grade') < 80:
                return 'C'
            elif 80 <= obj.get('grade') < 90:
                return 'B'
            elif 90 <= obj.get('grade') <= 100:
                return 'A'

        except (AttributeError, TypeError, ZeroDivisionError):
            return None

    def __init__(self, *args, **kwargs):
        super(ExamSerializer, self).__init__(*args, **kwargs)

        fields = ''
        if self.context['request'].query_params.get('show'):
            fields = self.context['request'].query_params.get('show')

        if self.context['request'].query_params.get('group_by'):
            fields += ',' + self.context['request'].query_params.get('group_by')

        if self.context['request'].query_params.get('sort_by'):
            fields += ',' + self.context['request'].query_params.get('sort_by').split(':')[0]

        if fields:
            fields = fields.split(',')
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Exam
        fields ='__all__'