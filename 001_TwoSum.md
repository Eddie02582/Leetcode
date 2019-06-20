# Deploy Django


    
## Appache+wsgi


### For Windows

**安裝 mod_wsgi**
首先到 <href> https://www.lfd.uci.edu/~gohlke/pythonlibs/#mod_wsgi</href> 下載對應的版本<br>
本範例使用mod_wsgi-4.6.5+ap24vc14-cp36-cp36m-win_amd64.whl
```
pip install mod_wsgi-4.6.5+ap24vc14-cp36-cp36m-win_amd64.whl
```



**Appache 設定**

首先到官網下載 <href>https://httpd.apache.org/download.cgi</href><br/>

找到 Apache24\conf\httpd.conf 並依序修改<br/>

1.確認SRVROOT 路徑正確
```
> Define SRVROOT "D:/Apache24"
> ServerRoot "${SRVROOT}"
```

2.設定port Listen:8008
```
# prevent Apache from glomming onto all bound IP addresses.
#
#Listen 12.34.56.78:80
Listen 8008
```

3.設定python 路徑 和 wsgi路徑

LoadFile "D:\Python\Python_Venv\Python36\djsc\Scripts\python36.dll" <br/>
LoadModule wsgi_module "D:\Python\Python_Venv\Python36\djsc\Lib\site-packages\mod_wsgi\server\mod_wsgi.cp36-win_amd64.pyd"<br/>

```
#
# Dynamic Shared Object (DSO) Support
#
# To be able to use the functionality of a module which was built as a DSO you
# have to place corresponding `LoadModule' lines at this location so the
# directives contained in it are actually available _before_ they are used.
# Statically compiled modules (those listed by `httpd -l') do not need
# to be loaded here.
#
# Example:
# LoadModule foo_module modules/mod_foo.so
#

LoadFile "D:\Python\Python_Venv\Python36\djsc\Scripts\python36.dll"  
LoadModule wsgi_module "D:\Python\Python_Venv\Python36\djsc\Lib\site-packages\mod_wsgi\server\mod_wsgi.cp36-win_amd64.pyd"

LoadModule access_compat_module modules/mod_access_compat.so
LoadModule actions_module modules/mod_actions.so
```


4.設定python 路徑 和 django路徑

```
WSGIPythonHome D:/Python/Python_Venv/Python36/djsc
WSGIPythonPath D:/Desktop/Web/AutoMation/mydjango

DocumentRoot "D:/Desktop/Web/AutoMation/mydjango/mydjango"
<Directory D:/Desktop/Web/AutoMation/mydjango/mydjango/>
<Files wsgi.py>
    Require all granted
</Files>
</Directory>
Include "D:/Desktop/Web/AutoMation/mydjango/mydjango/apache_setting.conf"
```



**Django 設定**

**wsgi.py**
```python
import os
import sys
from django.core.wsgi import get_wsgi_application
sys.path.append(r"D:\Desktop\Web\AutoMation\mydjango\mydjango")
sys.path.append(r"D:\Desktop\Web\AutoMation\mydjango")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mydjango.settings')

application = get_wsgi_application()
```



**setting.py**
修改 DEBUG = False,將ALLOWED_HOSTS 改成local ip

```python
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['192.168.1.1']
```

apache_setting.conf 放置與setting 同目錄
VirtualHost *:設定port
CustomLog,ErrorLog :可自行修改log 路徑
WSGIScriptAlias: 指定wsgi.py 路徑


```python
<VirtualHost *:8008>
 
    ServerName abc.dd.ee
    ServerName abc123.dd.ee
    #ServerAlias www.example.com
    
    #access_log 命名結果為 access_log.2013-06-06 
    #86400 代表記錄一天 
    CustomLog "|./bin/rotatelogs.exe ./logs/djangoProject/access_%Y-%m-%d.log 86400" common
    ErrorLog "|./bin/rotatelogs.exe ./logs/djangoProject/error_%Y-%m-%d.log 86400"
		
    
    ###設定gzip
    
	SetOutputFilter DEFLATE
	#AddOutputFilterByType DEFLATE text/html text/css text/plain text/xml application/x-javascript application/x-httpd-php

	#exclude the following file types
	SetEnvIfNoCase Request_URI \.(?:exe|t?gz|zip|iso|tar|bz2|sit|rar|png|jpg|gif|jpeg|flv|swf|mp3)$ no-gzip dont-vary

	#set compression level
	DeflateCompressionLevel 6

	#Handle browser specific compression requirements
	BrowserMatch ^Mozilla/4 gzip-only-text/html
	BrowserMatch ^Mozilla/4.0[678] no-gzip
	BrowserMatch bMSIE !no-gzip !gzip-only-text/html
	SetEnvIf User-Agent ".*MSIE.*" nokeepalive ssl-unclean-shutdown downgrade-1.0 force-response-1.0
	
	###設定gzip End
    
    
    # 指定包含服務腳本的目錄
    WSGIScriptAlias / D:/Desktop/Web/AutoMation/mydjango/mydjango/wsgi.py	
	
	
    <Directory D:/Desktop/Web/AutoMation/mydjango/mydjango>
    <Files wsgi.py>
        Require all granted
    </Files>
    </Directory>
 
    # 指定靜態文件的目錄
    Alias /static D:/Desktop/Web/AutoMation/mydjango/static
    <Directory D:/Desktop/Web/AutoMation/mydjango/static>
        Options Indexes  FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>
    
    # 指定 media 文件的目錄
    Alias /media D:\Desktop\Web\AutoMation\mydjango\media
    <Directory D:\Desktop\Web\AutoMation\mydjango\media>
        Options Indexes  FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>	
 
</VirtualHost>






```



