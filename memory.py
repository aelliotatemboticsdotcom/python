import psutil
import pprint
print ("Here are the disks: ")
disk_part = psutil.disk_partitions()
print ("data type: ")
print (type(disk_part))
print (disk_part)
print ("here is the network connections")
net_counters = psutil.net_io_counters(pernic=True)
print (net_counters)
print (type(net_counters))
print ("="*30)
print ("printout out key/value pairs in dict")

# for key, value in net_counters.iteritems():
#    print (key, value)

pprint.pp(net_counters.items())
