
from django.contrib import admin
from asset.models import Rcs_db
from asset.models import Rcs_hardware
from asset.models import Rcs_software
from asset.models import V_Rcs_asset

#class RcsAdminSite(admin.AdminSite):
#    site_header = 'RCS Administration'
#admin.site = RcsAdminSite(name='admin')

class RcsBaseModelAdmin(admin.ModelAdmin):
    list_per_page = 100


class RcsdbModelAdmin( RcsBaseModelAdmin ):
    list_column = ('id','Instance','db_name','Hostaddress','LBaddress','Port','Location','isFetionResource')
    list_display = list_column
    #list_display_filelds = list_column
    #list_editable = list_column
    search_fields = list_column
    list_display_links = list_column
admin.site.register(Rcs_db,RcsdbModelAdmin)

class RcsHardwareModelAdmin( RcsBaseModelAdmin ):


    list_display = ('id','SN','PN','HostName','UnitType','Hardware','EngineRoom','Place','UPlace','Zone',
                    'Hostaddress','NetMask','GateWay','System','DeviceName','DevicePort','Project',
                    'PutUnder','IsFetionResource','Role','LastTime','Inputer','Other')
    search_fields = list_display
    list_display_links = list_display




admin.site.register(Rcs_hardware,RcsHardwareModelAdmin)


class RcsSoftwareModelAdmin( RcsBaseModelAdmin):
    list_display = ('id','business','ServiceName','AppType','ServiceType','summary','Place','HostName','Hostaddress',
                    'LocalPort','LBaddress','LBway','LocalNAT','NATsummary','LBNAT','BearVPN','VPNtype','VPNload',
                    'OutIP','Targetsummary','Target','Visitsummary','VisitIP','LocalIN','mapped','domain','strategy',
                    'interface','IsFetionResource','project','LastTime','Inputer','Other')
    search_fields = list_display
    list_display_links = list_display

admin.site.register(Rcs_software,RcsSoftwareModelAdmin)

class V_RcsAssetsInfo( RcsBaseModelAdmin):
    list_display = ('hardware_id','Hostaddress','HostName','Hardware','EngineRoom','System','Project','IsFetionResource',
                   'DeviceName','DevicePort','software_id','business','ServiceName','AppType','ServiceType',
                   'summary','LocalPort','LBaddress','LBway','LocalNAT','NATsummary','LBNAT','BearVPN','VPNtype',
                   'VPNload','OutIP','Targetsummary','Target','Visitsummary','VisitIP','LocalIN','mapped','domain',
                   'strategy','interface','db_id','dbHostaddress','Instance','db_name','dbLBaddress','Port')
    search_fields = list_display
    fields = ('hardware_id',)



admin.site.register(V_Rcs_asset,V_RcsAssetsInfo)


