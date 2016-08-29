from django.db import models
from django.utils.html import format_html

class Rcs_db(models.Model):
    Instance = models.CharField(max_length=255,blank=True)
    db_name = models.CharField(max_length=255,blank=True)
    Hostaddress = models.CharField(max_length=255,blank=True)
    LBaddress = models.CharField(max_length=255,blank=True)
    Port = models.CharField(max_length=255,blank=True)
    Location = models.CharField(max_length=255,blank=True,
                                choices=(('YHG','雍和宫'),('FT','丰台'),('CSK','菜市口'),('ZYC','南方资源池')))
    isFetionResource = models.SmallIntegerField(blank=True,choices=((0,'否'),(1,'是'))) #,verbose_name = "是否借用飞信资产"

    class Meta:
        db_table = 'RCS_DB'
        verbose_name = '数据库资产'
        verbose_name_plural = '数据库资产'
        managed = False

    def __unicode__(self):
        return self.name


class Rcs_hardware(models.Model):

    SN = models.CharField(max_length=255,blank=True)
    PN = models.CharField(max_length=255,blank=True) #广东移动资产编号
    HostName = models.CharField(max_length=255,blank=True)
    UnitType = models.CharField(max_length=255,blank=True) #设备型号
    Hardware = models.CharField(max_length=255,blank=True) #服务器配置
    EngineRoom = models.CharField(max_length=255,blank=True) #机房地址
    Place = models.CharField(max_length=255,blank=True)
    UPlace = models.CharField(max_length=255,blank=True) #U位
    Zone = models.CharField(max_length=255,blank=True) #区域
    Hostaddress = models.CharField(max_length=255,blank=True)
    NetMask = models.CharField(max_length=255,blank=True)
    GateWay = models.CharField(max_length=255,blank=True)
    System = models.CharField(max_length=255,blank=True) #操作系统
    DeviceName = models.CharField(max_length=255,blank=True) #网络设备名称
    DevicePort = models.CharField(max_length=255,blank=True) #网络设备端口
    Project = models.CharField(max_length=255,blank=True,
                               choices=(('1.5','1.5'),('1.x','1.x'))) #归属项目
    PutUnder = models.CharField(max_length=255,blank=True) #资产规划
    IsFetionResource = models.IntegerField(blank=True,choices=((0,'否'),(1,'是')))
    Role = models.CharField(max_length=255,blank=True)
    LastTime = models.DateTimeField(auto_now=True) #last_update_time"
    Inputer = models.CharField(max_length=255,blank=True)
    Other = models.TextField(blank=True) #备注

    class Meta:
        db_table = 'RCS_Hardware'
        verbose_name = '硬件资产'
        verbose_name_plural = '硬件资产'
        managed = False

    def __unicode__(self):
        return self.name

class Rcs_software(models.Model):

    business = models.CharField(max_length=255,blank=True) #平台
    ServiceName = models.CharField(max_length=255,blank=True) #服务名称
    AppType = models.CharField(max_length=255,blank=True) #应用实例名称
    ServiceType = models.CharField(max_length=255,blank=True,
                                   choices=(('J','自开发JAVA'),('T','第三方厂家'),('M','中间件'),('N','.net'),('I','IISweb')))
                                    #服务类型
    summary = models.CharField(max_length=255,blank=True) #服务功能概述
    Place = models.CharField(max_length=255,blank=True,
                             choices=(('YHG','雍和宫'),('FT','丰台'),('CSK','菜市口'),('ZYC','南方资源池')))
                                    #服务器部署位置
    HostName = models.CharField(max_length=255,blank=True)
    Hostaddress = models.CharField(max_length=255,blank=True)
    LocalPort = models.TextField(blank=True) #verbose_name = "本机端口")
    LBaddress = models.CharField(max_length=255,blank=True) #verbose_name = "负载地址")
    LBway = models.CharField(max_length=255,blank=True) #verbose_name="负载方式"
    LocalNAT = models.CharField(max_length=255,blank=True)
    NATsummary = models.CharField(max_length=255,blank=True) #verbose_name = "NAT地址功能概述")
    LBNAT = models.CharField(max_length=255,blank=True)
    BearVPN = models.TextField(max_length=255,blank=True) #verbose_name = "承载网地址")
    VPNtype = models.CharField(max_length=255,blank=True) #verbose_name = "承载网类型")
    VPNload = models.CharField(max_length=255,blank=True) #verbose_name = "承载网负载地址")
    OutIP = models.TextField(max_length=255,blank=True) #verbose_name = "出访携带IP")
    Targetsummary = models.CharField(max_length=255,blank=True) #verbose_name = "目标地址概述")
    Target = models.TextField(max_length=255,blank=True) #verbose_name = "目标地址")
    Visitsummary = models.TextField(max_length=255,blank=True) #verbose_name = "入访地址概述")
    VisitIP = models.TextField(max_length=255,blank=True) #verbose_name = "入访地址")
    LocalIN = models.CharField(max_length=255,blank=True) #verbose_name = "入访到本方地址及端口")
    mapped = models.TextField(max_length=255,blank=True) #verbose_name = "负载及火墙映射关系")
    domain = models.CharField(max_length=255,blank=True) #verbose_name = "所用域名")
    strategy = models.IntegerField(choices=((0,'没有'),(1,'出访'),(2,'入访'),(3,'出入访'))) #verbose_name = "出入访策略")
    interface = models.IntegerField(blank=True,
                                    choices=((0,'没有'),(1,'南北互访'),(2,'第三方'),(3,'第三方和南北')))
                                    #verbose_name = "出入访接口类型",
    IsFetionResource = models.IntegerField(blank=True,choices=((0,'否'),(1,'是')))
    project = models.CharField(max_length=255,blank=True) #verbose_name = "归属项目")
    LastTime = models.DateTimeField(auto_now=True) #verbose_name = "最后修改时间")
    Inputer = models.CharField(max_length=255,blank=True) #verbose_name = "最后修改人")
    Other = models.TextField(max_length=255,blank=True) #verbose_name = "备注")



    class Meta:
        db_table = 'RCS_SoftWare'
        verbose_name = '软件资产'
        verbose_name_plural = '软件资产'
        managed = False

    def __unicode__(self):
        return self.name

class V_Rcs_asset(models.Model):
    #hardwareId
    hardware_id = models.IntegerField(blank=True,primary_key=True)
    Hostaddress = models.CharField(max_length=255, blank=True)
    HostName = models.CharField(max_length=255, blank=True)
    Hardware = models.CharField(max_length=255, blank=True)# verbose_name="服务器配置")
    EngineRoom = models.CharField(max_length=255, blank=True)# verbose_name="机房地址")
    System = models.CharField(max_length=255, blank=True)# verbose_name="操作系统")
    Project = models.CharField(max_length=255, blank=True,
                               choices=(('1.5', '1.5'), ('1.x', '1.x'))) #verbose_name="归属项目"
    IsFetionResource = models.IntegerField(blank=True, choices=((0, '否'), (1, '是')))
    DeviceName = models.CharField(max_length=255, blank=True) # verbose_name="网络设备名称")
    DevicePort = models.CharField(max_length=255, blank=True) # verbose_name="网络设备端口")

    #software
    software_id = models.IntegerField(blank=True,primary_key=True)
    business = models.CharField(max_length=255, blank=True)#verbose_name="平台")
    ServiceName = models.CharField(max_length=255, blank=True)# verbose_name="服务名称")
    AppType = models.CharField(max_length=255, blank=True)# verbose_name="应用实例名称")
    ServiceType = models.CharField(max_length=255, blank=True,
                                   choices=(('J', '自开发JAVA'), ('T', '第三方厂家'),
                                            ('M', '中间件'), ('N', '.net'), ('I', 'IISweb')))
                                    #verbose_name = "服务类型"
    summary = models.CharField(max_length=255, blank=True)# verbose_name="服务功能概述")
    LocalPort = models.TextField(blank=True)# verbose_name="本机端口")
    LBaddress = models.CharField(max_length=255, blank=True)#verbose_name="负载地址")
    LBway = models.CharField(max_length=255, blank=True)#verbose_name="负载方式")
    LocalNAT = models.CharField(max_length=255, blank=True)
    NATsummary = models.CharField(max_length=255, blank=True)# verbose_name="NAT地址功能概述")
    LBNAT = models.CharField(max_length=255, blank=True)
    BearVPN = models.TextField(max_length=255, blank=True)# verbose_name="承载网地址")
    VPNtype = models.CharField(max_length=255, blank=True)# verbose_name="承载网类型")
    VPNload = models.CharField(max_length=255, blank=True)# verbose_name="承载网负载地址")
    OutIP = models.TextField(max_length=255, blank=True)# verbose_name="出访携带IP")
    Targetsummary = models.CharField(max_length=255, blank=True)# verbose_name="目标地址概述")
    Target = models.TextField(max_length=255, blank=True)# verbose_name="目标地址")
    Visitsummary = models.TextField(max_length=255, blank=True)# verbose_name="入访地址概述")
    VisitIP = models.TextField(max_length=255, blank=True)# verbose_name="入访地址")
    LocalIN = models.CharField(max_length=255, blank=True)# verbose_name="入访到本方地址及端口")
    mapped = models.TextField(max_length=255, blank=True)# verbose_name="负载及火墙映射关系")
    domain = models.CharField(max_length=255, blank=True)# verbose_name="所用域名")
    strategy = models.IntegerField(choices=((0, '没有'), (1, '出访'), (2, '入访'), (3, '出入访')))# verbose_name="出入访策略")
    interface = models.IntegerField(blank=True,
                                    choices=((0, '没有'), (1, '南北互访'), (2, '第三方'), (3, '第三方和南北')))
                                    #verbose_name = "出入访接口类型"
    #db
    db_id=models.IntegerField(blank=True)# primary_key=True)
    dbHostaddress=models.CharField(max_length=255,blank=True)
    Instance = models.CharField(max_length=255, blank=True)
    db_name = models.CharField(max_length=255, blank=True)
    dbLBaddress = models.CharField(max_length=255, blank=True)
    Port = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'V_RCS_Assets'
        verbose_name = '资产综合视图'
        verbose_name_plural = '资产综合视图'
        managed = False

    def __unicode__(self):
        return self.name



