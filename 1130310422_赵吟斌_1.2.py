num = eval(raw_input())     	    	#输入一个温度
if num == 1:                	    	#判断模式，如果输入1，为华氏转摄氏度
    F1 = eval(raw_input())              #输入华氏度   
    if   F1<=-459.4:                	#如果温度低于绝对零度
         print "Error"                  #输出错误
         print "hahahaha"
         exit()                         #并退出
    elif F1>=9999.9:                    #如果温度过高，没有实际意义
         print "Error"                  #输出错误
         exit()                         #并退出
    else:                        
         C2 = (F1 - 32) / 1.8           #温度有意义，就进行转换运算
         print(format(C2,".2f"))        #输出摄氏度，并取两位小数
elif num==2:                            #如果输入的是2，为摄氏度转华氏度
    C1 = eval(raw_input())          	#输入摄氏度
    if   C1<=-273.0:                	#如果温度低于绝对零度
         print "Error"              	#输出错误  
         exit()                     	#并退出
    elif C1>=9999.0:                    #如果温度过高，没有实际意义
         print "Error"      	    	#输出错误
         exit()                         #并退出
    else:       	                
         F2 = 32 + C1 * 1.8 	    	#如果是有意思的温度，就进行转换运算
         print(format(F2,".2f"))        #输出华氏度，并取两位小数
         print "hello"
else:   	    	    	    	#如果是其他数字
         print "Error"                  #输出错误
         exit() 	    	    	#并退出
