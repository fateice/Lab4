num = eval(raw_input())     	    	#����һ���¶�
if num == 1:                	    	#�ж�ģʽ���������1��Ϊ����ת���϶�
    F1 = eval(raw_input())              #���뻪�϶�   
    if   F1<=-459.4:                	#����¶ȵ��ھ������
         print "Error"                  #�������
         print "hahahaha"
         exit()                         #���˳�
    elif F1>=9999.9:                    #����¶ȹ��ߣ�û��ʵ������
         print "Error"                  #�������
         exit()                         #���˳�
    else:                        
         C2 = (F1 - 32) / 1.8           #�¶������壬�ͽ���ת������
         print(format(C2,".2f"))        #������϶ȣ���ȡ��λС��
elif num==2:                            #����������2��Ϊ���϶�ת���϶�
    C1 = eval(raw_input())          	#�������϶�
    if   C1<=-273.0:                	#����¶ȵ��ھ������
         print "Error"              	#�������  
         exit()                     	#���˳�
    elif C1>=9999.0:                    #����¶ȹ��ߣ�û��ʵ������
         print "Error"      	    	#�������
         exit()                         #���˳�
    else:       	                
         F2 = 32 + C1 * 1.8 	    	#���������˼���¶ȣ��ͽ���ת������
         print(format(F2,".2f"))        #������϶ȣ���ȡ��λС��
         print "hello"
else:   	    	    	    	#�������������
         print "Error"                  #�������
         exit() 	    	    	#���˳�
