from drf_base64.serializers import Base64FileField
import base64

class ReturnBase64File(Base64FileField):
    def to_representation(self, value):
        encoded = base64.b64encode(value.file.file.read())
        return encoded
        # if not value:
        #     return None

        # use_url = getattr(self, 'use_url', api_settings.UPLOADED_FILES_USE_URL)
        # if use_url:
        #     try:
        #         url = value.url
        #     except AttributeError:
        #         return None
        #     request = self.context.get('request', None)
        #     if request is not None:
        #         return request.build_absolute_uri(url)
        #     return url

        # return value.name