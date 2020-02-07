print ("This Python based on ASCII_Base=33, Illumina v1.8 and later")
dic_qual={
    '"':'1', '#':'2', '$':'3', '%':'4', '&':'5',
    "'":"6", ')':'7', '(':'8', '*':'9', '+':'10',
    ',':'11', '-':'12', '.':'13', '/':'14', '0':'15',
    '1':'16', '2':'17', '3':'18', '4':'19', '5':'20',
    '6':'21', '7':'22', '8':'23', '9':'24', ':':'25',
    ';':'26', '<':'27', '=':'28', '>':'29', '?':'30',
    '@':'31', 'A':'32', 'B':'33', 'C':'34', 'D':'35',
    'E':'36', 'F':'37', 'G':'38', 'H':'39', 'I':'40', 
    'J':'41'}

def P_calculator(fr):
    print ("Okay, P_calculator starts")
    lis_lines=fr.readlines()
    seq_qual=''
    for line in lis_lines[3::4]:
        seq_qual+=line.strip()
    P_add=0
    count=0
    for qual in seq_qual:
        count+=1
        P_add+=10**(-(int(dic_qual[qual]))/10)
    P_result=round((P_add/count),6)
    return P_result

filename=input("Input the name of FASRQ file (for example, 'SRR10549530'): ")
try:
    fr=open('%s_1.fastq' % (filename), 'r')
    print (filename, 'is paired-end file.')
    print ("If you want to check the quality of both read, input 'A'")
    print ("If you want to check the quality of forward read, input 'B'")
    print ("If you want to check the quality of reverse read, input 'C'")
    option_select=input("Choose your option: ")
    if option_select == 'A':
        P_forward=P_calculator(open('%s_1.fastq'%(filename)))
        P_reverse=P_calculator(open('%s_2.fastq'%(filename)))
        print (1-(P_forward+P_reverse)/2)
    elif option_select == 'B':
        P_forward=P_calculator(open('%s_1.fastq'%(filename)))
        print (1-(P_forward))
    elif option_select == 'C':
        P_reverse=P_calculator(open('%s_2.fastq'%(filename)))
        print (1-(P_reverse))
    else:
        print ("[ERROR_paired_end] Please write the proper number")
        exit()      
except:
    try:
        fr=open('%s.fastq'%(filename))
        print (filename, 'is single-end file.')
        P_value=P_calculator(fr)
        print (1-(P_value))
    except:
        print ("[ERROR_single_end] Please write the proper name")
        exit() 