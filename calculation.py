utt= "what is 2 - 2"
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

