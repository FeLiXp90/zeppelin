from rest_framework import serializers
from .models import (
    AcademicDegreeCategory,
    AcademicDegree,
    AcademicDegreeStatus,
    KnowledgeLevel,
    ExperienceLevel,
    Position,
    Employee,
    EmployeeKnowledge,
    SthStageKnowledgeLevel,
    SthStageExperienceLevel,
    Team,
)

class AcademicDegreeCategoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicDegreeCategory
        exclude = ("polymorphic_ctype",)

class AcademicDegreeCategoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = AcademicDegreeCategory
        exclude = ("polymorphic_ctype",)


class AcademicDegreeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicDegree
        exclude = ("polymorphic_ctype",)

class AcademicDegreeReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = AcademicDegree
        exclude = ("polymorphic_ctype",)


class AcademicDegreeStatusWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicDegreeStatus
        exclude = ("polymorphic_ctype",)

class AcademicDegreeStatusReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = AcademicDegreeStatus
        exclude = ("polymorphic_ctype",)


class KnowledgeLevelWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeLevel
        exclude = ("polymorphic_ctype",)

class KnowledgeLevelReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = KnowledgeLevel
        exclude = ("polymorphic_ctype",)


class ExperienceLevelWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceLevel
        exclude = ("polymorphic_ctype",)

class ExperienceLevelReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = ExperienceLevel
        exclude = ("polymorphic_ctype",)


class PositionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        exclude = ("polymorphic_ctype",)

class PositionReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Position
        exclude = ("polymorphic_ctype",)


class EmployeeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ("polymorphic_ctype",)

class EmployeeReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Employee
        exclude = ("polymorphic_ctype",)


class EmployeeKnowledgeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeKnowledge
        exclude = ("polymorphic_ctype",)

class EmployeeKnowledgeReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = EmployeeKnowledge
        exclude = ("polymorphic_ctype",)


class SthStageKnowledgeLevelWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SthStageKnowledgeLevel
        exclude = ("polymorphic_ctype",)

class SthStageKnowledgeLevelReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = SthStageKnowledgeLevel
        exclude = ("polymorphic_ctype",)


class SthStageExperienceLevelWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SthStageExperienceLevel
        exclude = ("polymorphic_ctype",)

class SthStageExperienceLevelReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = SthStageExperienceLevel
        exclude = ("polymorphic_ctype",)


class TeamWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        exclude = ("polymorphic_ctype",)

class TeamReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Team
        exclude = ("polymorphic_ctype",)

