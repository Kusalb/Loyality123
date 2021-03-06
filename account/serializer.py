from rest_framework import serializers




from .models import Waiter
from .models import offer
from .models import Partner
from .models import Trasaction
from .models import Promotion
from .models import Customer
from .models import Discount
from .models import UserId

class WaiterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Waiter
        fields = ('username', 'email')
        # fields = '__all__'
        # for returning all values



class offerSerializer(serializers.ModelSerializer):

    class Meta:
        model = offer
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = '__all__'

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trasaction
        fields = '__all__'

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model= Discount
        fields= '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Customer
        fields= '__all__'


class UserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserId
        fields= '__all__'