from OpenstackLib.OpenstackLbaasConfig import OpenstackLbaasConfig


print "lb main start"

ops_lb = OpenstackLbaasConfig()

ops_lb.init()
ops_lb.create_lb()
ops_lb.create_member('192.168.2.5')
ops_lb.create_member('192.168.2.6')
