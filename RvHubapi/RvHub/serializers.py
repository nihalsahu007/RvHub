from rest_framework import serializers
from .models import *
from .utils import generate_qr_code
import qrcode
from io import BytesIO
# from PIL import Image

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateInfo
        fields = '__all__'
    