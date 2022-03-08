from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.Serializer):
    oid = serializers.IntegerField()
    oname = serializers.CharField(max_length=50)
    status = serializers.CharField(max_length=50)
    mfg = serializers.DateTimeField()


    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.oid = validated_data.get("oid",instance.oid)
        instance.oname = validated_data.get("oname",instance.oname)
        instance.status = validated_data.get("status",instance.status)
        instance.mfg = validated_data.get("mfg",instance.mfg)

        instance.save()

        return instance