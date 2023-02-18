while True:
  time = input()

  tens = ["zero","ten","twenty","thirty","forty","fifty","sixty"]
  ones = []
  ones = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","ninteen", "twenty"]

  if(":" not in time):
    hours = int(time[0:len(time)//2])
    minutes = 0
    ampm = time[2:]
  else:
    hours = int(time.split(":")[0])
    minutes = int(time.split(":")[1][0:2])
    ampm = time.split(":")[1][2:]

  time = ""

  if(ampm == "PM"):
    hours = hours + 12

  if(hours==12):
    hours = 0
  if(hours==24):
    hours = 12

  if(minutes==0):

    if(hours > 20):
      time = tens[2] + " " + ones[hours%20] + " hundred hours"
    else:
      time =  ones[hours] + " hundred hours"

  elif(hours>9 and minutes >9):

    if(hours > 20):
      time = tens[2] + " " + ones[hours%20] + " "
    else:
      time =  ones[hours] + " "

    if(minutes<21):
      time = time + ones[minutes]
    else:
      minutes_1 = minutes % 10
      minutes_2 = minutes // 10

      time = time + tens[minutes_2] +" "+ ones[minutes_1]

  else:
    
    if(hours<10):
      h = "zero " + ones[hours]
    else:
      if(hours > 20):
        h = tens[2] + " " + ones[hours%20]
      else:
        h =  ones[hours]
    if(minutes<10):
      m = "zero " + ones[minutes]
    else:
      if(minutes<21):
        m = ones[minutes]
      else:
        minutes_1 = minutes % 10
        minutes_2 = minutes // 10

        m = tens[minutes_2] +" "+ ones[minutes_1]


    
    

    time = h + " " + m


  print(time)
