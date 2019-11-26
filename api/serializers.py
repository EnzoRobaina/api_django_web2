from rest_framework import serializers
from .models import Character, Skill


def clean_numerical_field(value):
    if value <= 0 or value > 20:
        raise serializers.ValidationError(
            'This value must be between 1 and 20.',
            code='invalid'
        )
    return value


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('__all__')
        read_only_fields = ['level']

    skills = serializers.SerializerMethodField()

    def get_skills(self, object):
        skills = SkillSerializer(
            Skill.objects.filter(character=object),
            many=True
        ).data
        for skill in skills:
            skill.pop('character')
        print(skills)
        return skills

    def validate_strength(self, value):
        return clean_numerical_field(value)

    def validate_dexterity(self, value):
        return clean_numerical_field(value)

    def validate_constitution(self, value):
        return clean_numerical_field(value)

    def validate_intelligence(self, value):
        return clean_numerical_field(value)

    def validate_wisdom(self, value):
        return clean_numerical_field(value)

    def validate_charisma(self, value):
        return clean_numerical_field(value)


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('__all__')
