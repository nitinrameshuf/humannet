imgcount = 0
timecount = 0.0
percent = 0.0
percount = 0
with open("result.txt", "r") as res:
  myline = res.readlines()
  for line in myline:
    if(line == "\n"):
      continue
    else:
      spec = line.split()
      if(spec[0] == "Enter"):
        if(len(spec) == 3):
          continue
        else: 
          imgcount = imgcount + 1
          timecount = timecount + float(spec[6])             
      elif(spec[0] == "human:"):
        percount = percount + 1
        percent = int(spec[1].replace("%", "")) + percent 

if(percent!=0 and percount!=0):
  eff = percent/percount
  print("-------------------------------------------------------------------")
  print("Object detection efficiency is " + str(eff) + "%")
if(imgcount!=0 and timecount!=0):
  fps = imgcount/(timecount/1000)
  avgtime = timecount/imgcount
  print("Running at " + "{:.2f}".format(fps) + " FPS")
  print("Processed "+ str(imgcount)+" images in " + "{:.2f}".format(timecount/1000) + " seconds")
  print("Average timage process time: "+ "{:.2f}".format(avgtime) +" millisec each")
  print("-------------------------------------------------------------------")
