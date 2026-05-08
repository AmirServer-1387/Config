import sys
sys.path.insert(0, '/opt/hiddify-manager')
from hiddifypanel import create_app
from hiddifypanel.models import db, Proxy, ProxyTypes
import uuid

app = create_app()
with app.app_context():
    proxy = Proxy(
        name='NPV_Ready',
        proxy_type=ProxyTypes.vmess,
        port=443,
        network='ws',
        security='tls',
        host='vless.loguvo.com',
        path='/m8Xk9Lp2Qw5RtY7',
        cdn=True,
        user_uuid=str(uuid.uuid4())
    )
    db.session.add(proxy)
    db.session.commit()
    print('Link:', proxy.link)
