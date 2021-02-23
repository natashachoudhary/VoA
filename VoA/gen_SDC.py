import datetime,time
timeformat = "24"
def timenow():
    #now = datetime.now()
    #current_time = now.strftime("%H:%M:%S")
    hours = time.strftime("%H") + " hours" 
    minutes = time.strftime("%M") + " minutes"
    #print current_time
    output = hours + " and " + minutes
    return output

def date():
    month = time.strftime("%B")
    date = time.strftime("%d")
    output = month + " " +date
    return output


def day():
    today = time.strftime("%A")
    print today
    return today

def calc():
    list = ["+","-","/","*"]

    for i in range(len(list)):
        if list[i] in utt:
            print list[i]
            var1=utt.split(list[i])[-1]

            var2=utt.split(list[i])[1]
            print var1,var2
            if list[i]=="+":
                print int(var1)+int(var2)

            if list[i]=="-":
                print int(var1)-int(var2)
