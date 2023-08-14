

#################open
####一般读取文件
def read_text(path):
    lines=[]
    with open(path,'r',encoding='utf-8') as file:
        for line in file.readlines():
            line=line.strip('\n')
            lines.append(line)
    return lines



#################多重列表推到式
lines=['车标','电机舱','发动机','格栅','雨刮','大灯','行李箱']
tages_lines=[[].append(y)  for x in lines for y in x.lower().replace('/','')]


##################动态的创建变量名
###使用globals
var_name = "temp"
globals()[var_name] = "Hello, World!"
print(temp)  # 输出: Hello, World!

####使用local
var_name = "temp"
locals()[var_name] = "Hello, World!"
print(temp)  # 输出: Hello, World!



