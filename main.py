import demo
import utils
from demo.vpork import vpork
from demo.pucloud import pucloud

try:
    demo1=vpork().run()
except Exception:
    print('error')

try:
    demo2=pucloud().run()
except Exception:
    print('error')