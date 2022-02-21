# method that plot the gant chart of the application
def gant(cpus, tasks,l, H=50, M=5 ):
    import matplotlib.pyplot as plt  
    fig, axi = plt.subplots()  
    axi.set_ylim(0, H);      axi.set_xlim(0, l)        
    axi.set_xlabel('Time');  axi.set_ylabel('Processor')        
    axi.grid(True)
    
    # Setting ticks on y-axis
    dx =  int((H - 2*M)/ len(cpus))
    axi.set_yticks([dx + i*dx  for i in range(len(cpus))])           
    axi.set_yticklabels(cpus)
    
    # Declaring a bar in schedule
    for k,task in tasks.items():
        posH=(task['cpu']+1)*dx-M/2
        axi.broken_barh(task['length'], (posH, M) , facecolors = task['color'])       
        for t in task['length']:
            axi.annotate(k, (1,1), xytext=(t[0]+t[1]/2-1, posH+M+1))
    plt.show() 
    
