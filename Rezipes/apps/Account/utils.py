from django.utils import timezone
from django.conf import settings
from base64 import urlsafe_b64encode, urlsafe_b64decode
from django.utils.encoding import force_bytes, force_str
from time import strftime
from datetime import datetime


class UrlSign:
    def urlsafe_encode(self,value:str):
        value_bytes = force_bytes(value)
        return urlsafe_b64encode(value_bytes).decode('utf-8', errors='strict')
    
    def urlsafe_decode(self,value:bytes):
        decoded_bytes = urlsafe_b64decode(value)
        return force_str(decoded_bytes)
    
    def time_to_str(self,value:datetime):
        return value.strftime('%Y-%m-%d %H:%M:%S')
    
    def str_to_time(self,value:str):
        return datetime.strptime('%Y-%m-%d %H:%M:%S')
    
    def url_encode(self, username):
        current_time = datetime.now()
        str_time = self.time_to_str(current_time)
        value = f'{username}!{str_time}'
        return self.urlsafe_encode(value)
    
    def url_decode(self, value):
        str_val = self.urlsafe_decode(value)
        print(str_val)
        username, time = str_val.split('!')
        return username