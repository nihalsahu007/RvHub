from django.db import models
import uuid
import qrcode
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.


class CandidateInfo(models.Model):
	candidate_unique_id = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
	name = models.CharField(max_length=255)
	phone_number = models.IntegerField(max_length=64)
	email = models.CharField(max_length=50, null=False)
	dob = models.DateField(blank=True, null=True)
	address = models.TextField()
	photo = models.FileField(upload_to ='photo', blank=True, null=True)
	aadhar_number = models.IntegerField(max_length=12)
	aadhar_pdf = models.FileField(upload_to ='aadhar', blank=True, null=True)
	qr_code = models.ImageField(upload_to='qrcode', blank=True, null=True)

	def generate_qr_code(self):
        # Create the QR code data using candidate's information
		qr_data = f"Unique Id:{self.candidate_unique_id} \nName: {self.name}\nPhone: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}\nAadhar Number: {self.aadhar_number}"

		# Generate the QR code image
		qr = qrcode.QRCode(
			version=1,
			error_correction=qrcode.constants.ERROR_CORRECT_L,
			box_size=10,
			border=4,
		)
		qr.add_data(qr_data)
		qr.make(fit=True)

		qr_img = qr.make_image(fill_color="black", back_color="white")

		# Save the QR code image to a BytesIO buffer
		buffer = BytesIO()
		qr_img.save(buffer, format='PNG')

		# Create an InMemoryUploadedFile
		qr_code_file = InMemoryUploadedFile(
			buffer,
			None,
			f"{self.name}_qr.png",
			'image/png',
			buffer.getbuffer().nbytes,
			None
		)

		# Set the qr_code field and save it
		self.qr_code.save(f"{self.name}_qr.png", qr_code_file, save=False)

	def save(self, *args, **kwargs):
		# Generate and save the QR code before saving the CandidateInfo instance
		self.generate_qr_code()
		super(CandidateInfo, self).save(*args, **kwargs)