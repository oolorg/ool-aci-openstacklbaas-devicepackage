# ●このプロジェクトについて  
このプロジェクトは2016年度に取り組んだ「CiscoACIオープンソース デバイスパッケージ開発 プロジェクト」にて開発したACIからOpenstackのLbaasをコントロールするためのDevicePackageのサンプルコードです。  
  
# ●動作環境(バージョン)  
Openstack・・・・Liberty  
LBaas・・・・・・v1  
APIC・・・・・・ 1.2  
  
# ●開発構成  
![ConstitutionImage](https://cloud.githubusercontent.com/assets/11345275/25370784/f99d2c8a-29c7-11e7-883c-529a9e6a0eab.png)
# ●使用方法  
1.DevicePackageの設定  
OpenstackLib\OpenstackLbaasConfig.pyの21行目からの下記の記述を構築したOpenstackの設定に合わせて記述します。  
  
    self.opbase_obj.password = 'password'#Openstackのadminパスワード
    #opbase_obj.password = 'okinawa1940'
    self.opbase_obj.username = 'admin' #Openstackのadminユーザ名
    self.opbase_obj.tenantname = 'admin' #対象となるテナント名
    
    #opbase_obj.openstack_ip = '192.168.1.29'
    self.opbase_obj.openstack_ip = '192.168.99.53' #OpenstackのMnagementPlaneのIP
    self.lb_pool_name = 'test_pool2' #Lbaasで使用するPool名
    self.subnet_name = 'test-aci2-nw-sb' #Lbaasで使用するSubnet名
    self.lb_vip_name = 'test_vip' #Lbaasで使用するVIP名
  
2.Windows上でソースコードをzipで任意の名前で圧縮します  
3.ACIの手順に従い、インストールして使用してください。  
