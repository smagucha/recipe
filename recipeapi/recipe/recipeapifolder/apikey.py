import os
#import requests
id_app=os.environ.get('id_app')  
Api_key=os.environ.get('Api_key')
# values=request.POST.get('q')
url='https://api.edamam.com/search?q=avacado&app_id='+ id_app +'&app_key='+Api_key+''
