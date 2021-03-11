import os
id_app=os.environ.get('id_app')  
Api_key=os.environ.get('Api_key')
url='https://api.edamam.com/search?q=pizza&app_id='+ id_app +'&app_key='+Api_key+''
