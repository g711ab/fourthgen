from django.shortcuts import render
from .models import Assetmanage
from .models import Hostinfo
# Create your views here.
def asset_table(request):
    a=[]
    asset_list = Assetmanage.objects.all()
    for asset in asset_list:
        asset_dict = {'asset_num': '%s' % (asset.asset_num),'type': '%s' % (asset.type),
                'server_ip': '%s' % (asset.server_ip),'remote_ip': '%s' % (asset.remote_ip),
                'data_center': '%s' % (asset.data_center),
                'room_num': '%s' % (asset.room_num),'rack_num': '%s' % (asset.rack_num),
                'system_type': '%s' % (asset.system_type),'cputype_num': '%s' % (asset.cputype_num),
                'disksize_num': '%s' % (asset.disksize_num),'memsize_num': '%s' % (asset.memsize_num),
                'disk_raid': '%s' % (asset.disk_raid),'card_type_num': '%s' % (asset.card_type_num),
                'power_num': '%s' % (asset.power_num),'service_num': '%s' % (asset.service_num),
                'buy_time': '%s' % (asset.buy_time),'expiration_time': '%s' % (asset.expiration_time),
                'note': '%s' % (asset.note)}
        a.append(asset_dict)
    return render(request, 'assetmanage/asset_table.html', {'a' : a})

def asset_table_detail(request):
    a=[]
    asset_list_detail = Assetmanage.objects.all()
    for asset in asset_list_detail:
        asset_dict_detail = {'asset_num': '%s' % (asset.asset_num),'type': '%s' % (asset.type),
                'server_ip': '%s' % (asset.server_ip),'remote_ip': '%s' % (asset.remote_ip),
                'data_center': '%s' % (asset.data_center),
                'room_num': '%s' % (asset.room_num),'rack_num': '%s' % (asset.rack_num),
                'system_type': '%s' % (asset.system_type),'cputype_num': '%s' % (asset.cputype_num),
                'disksize_num': '%s' % (asset.disksize_num),'memsize_num': '%s' % (asset.memsize_num),
                'disk_raid': '%s' % (asset.disk_raid),'card_type_num': '%s' % (asset.card_type_num),
                'power_num': '%s' % (asset.power_num),'service_num': '%s' % (asset.service_num),
                'buy_time': '%s' % (asset.buy_time),'expiration_time': '%s' % (asset.expiration_time),
                'note': '%s' % (asset.note)}
        a.append(asset_dict_detail)
    return render(request, 'assetmanage/asset_table_detail.html', {'a' : a})

def asset_add(request):
    asset_num = request.GET['asset_num']
    type = request.GET['type']
    server_ip = request.GET['server_ip']
    remote_ip = request.GET['remote_ip']
    data_center = request.GET['data_center']
    room_num = request.GET['room_num']
    rack_num = request.GET['rack_num']
    system_type = request.GET['system_type']
    cputype_num = request.GET['cputype_num']
    disksize_num = request.GET['disksize_num']
    memsize_num = request.GET['memsize_num']
    disk_raid = request.GET['disk_raid']
    card_type_num = request.GET['card_type_num']
    power_num = request.GET['power_num']
    service_num = request.GET['service_num']
    buy_time = request.GET['buy_time']
    expiration_time = request.GET['expiration_time']
    note = request.GET['note']
    Assetmanage.objects.create(asset_num="%s" % (asset_num),type="%s" % (type),
                               server_ip="%s" % (server_ip),remote_ip="%s" % (remote_ip),
                               data_center="%s" % (data_center),room_num="%s" % (room_num),
                               rack_num="%s" % (rack_num),system_type="%s" % (system_type),
                               cputype_num="%s" % (cputype_num),disksize_num="%s" % (disksize_num),
                               memsize_num="%s" % (memsize_num),disk_raid="%s" % (disk_raid),
                               card_type_num="%s" % (card_type_num),power_num="%s" % (power_num),
                               service_num="%s" % (service_num),buy_time="%s" % (buy_time),
                               expiration_time="%s" % (expiration_time),note="%s" % (note))
    return render(request, 'assetmanage/asset_add.html')

def asset_add_html(request):
    return render(request, 'assetmanage/asset_add.html')

'''def asset_del(request):
    asset_num = request.GET['asset_num']
    Assetmanage.objects.get(asset_num="%s" % (asset_num)).delete()
    a=[]
    post_list = Assetmanage.objects.all()
    for post in post_list:
        dict = {'asset_num': '%s' % (post.asset_num),'device_type': '%s' % (post.device_type),'local_ip': '%s' % (post.local_ip),'remote_ip': '%s' % (post.remote_ip),'system_type': '%s' % (post.system_type)}
        a.append(dict)
    return render(request, 'assetmanage/asset_table1.html', {'a' : a})

def asset_update(request):
    asset_num = request.GET['asset_num']
    device_type = request.GET['device_type']
    local_ip = request.GET['local_ip']
    remote_ip = request.GET['remote_ip']
    system_type = request.GET['system_type']
    update = Assetmanage.objects.get(asset_num="%s" % (asset_num))
    if device_type != '':
        update.device_type = "%s" % (device_type)
        update.save()
    if local_ip != '':
        update.local_ip = "%s" % (local_ip)
        update.save()
    if remote_ip != '':
        update.remote_ip = "%s" % (remote_ip)
        update.save()
    if system_type != '':
        update.system_type = "%s" % (system_type)
        update.save()
    a=[]
    post_list = Assetmanage.objects.all()
    for post in post_list:
        dict = {'asset_num': '%s' % (post.asset_num),'device_type': '%s' % (post.device_type),'local_ip': '%s' % (post.local_ip),'remote_ip': '%s' % (post.remote_ip),'system_type': '%s' % (post.system_type)}
        a.append(dict)
    return render(request, 'assetmanage/asset_table1.html', {'a' : a})'''