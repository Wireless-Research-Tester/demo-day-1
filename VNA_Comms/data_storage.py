def append_data(filename,data):
    file=open(filename,'a')
    for i in range(0,len(data)):
        file.write('%s,%d,%d,%d,%d,\n' % (data[i].measurement_type,data[i].freq,data[i].theta,data[i].phi,data[i].value))
    file.close()

def create_file(filename):
    file=open(filename,'w')
    file.write('measurement_type,freq,theta,phi,value,\n')
    file.close()
