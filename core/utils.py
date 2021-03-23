import os

class Domen_Create_Delete():
    def create_domen_nginx(self,domen):
        with open('/var/domens/temlates2.conf', 'r') as f:
            new_file = f.read().replace('###domen###', '%s' % domen)
        os.popen('sudo /usr/bin/mkdir /var/domens/nginx/%s' % domen).read()
        os.popen('echo "%s" > /var/domens/nginx/%s/index.html' % (domen,domen)).read()
        with open('/etc/nginx/sites-available/%s.conf' % domen, 'w') as f:
            f.write(new_file)
        os.popen('ln -s /etc/nginx/sites-available/%s.conf /etc/nginx/sites-enabled/' % domen).read()
        os.popen('/etc/init.d/nginx restart').read()
        return True
        
    def delete_domen_nginx(self,domen):
        os.popen('rm -rf /var/domens/nginx/%s' % domen).read()
        os.popen('rm -rf /etc/nginx/sites-available/%s.conf' % domen).read()
        os.popen('rm -rf /etc/nginx/sites-enabled/%s.conf' % domen).read()
        return True
        
    def create_domen_apache2(self,domen):
        with open('/var/domens/temlates1.conf', 'r') as f:
            new_file = f.read().replace('###domen###', '%s' % domen)
        os.popen('sudo /usr/bin/mkdir /var/domens/apache2/%s' % domen).read()
        os.popen('echo "%s" > /var/domens/apache2/%s/index.html' % (domen,domen)).read()
        with open('/etc/apache2/sites-available/%s.conf' % domen, 'w') as f:
            f.write(new_file)
        os.popen('ln -s /etc/apache2/sites-available/%s.conf /etc/apache2/sites-enabled/' % domen).read()
        os.popen('/etc/init.d/apache2 restart').read()
        return True
        
    def delete_domen_apache2(self,domen):
        os.popen('rm -rf /var/domens/apache2/%s' % domen).read()
        os.popen('rm -rf /etc/apache2/sites-available/%s.conf' % domen).read()
        os.popen('rm -rf /etc/apache2/sites-enabled/%s.conf' % domen).read()
        return True
        