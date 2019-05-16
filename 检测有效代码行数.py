#open file
#read one line contex,judge if code or comment
#   if '--' in the head this line is comment
#   if doesn’t has code this line is empty
#   else    this line is code line

filename = input('''要求文件编码格式为UTF-8
.vhd文件，支持识别 -- 注释，以及空行
.v  文件，支持识别 // 注释， /**/ 注释，以及空行
输入文件路径（包含文件名和扩展名）：''')
# open file
#file = open(filename,encoding='ANSI')
#file = open(filename,encoding='UTF-8')
#file = open(filename)


totalline = 0
validline = 0
emptyline = 0
commentline = 0

commentcnt = 0
commentflag = 0
validcharcnt= 0

# .vhd => 1 .v => 2
FileType = 0

#file is .v or .vhd(.VHD)

#get filename length
length = len(filename)

if filename[length-3:length] == 'vhd' or filename[length-3:length] == 'VHD':
    FileType = 1
elif filename[length-1:length] == 'v' or filename[length-3:length] == 'V':
    FileType = 2
else:
    FileType = 3
    print('不支持该文件类型')
    exit()

# open file with auto close
with open(filename,encoding='UTF-8') as file:

    if FileType == 1 :

        for line in file.readlines():
            totalline = totalline +1
            commentcnt = 0
            commentflag = 0
            validcharcnt = 0
            #print(line)
            for char in line:                       
                if char == '-' and validcharcnt == 0:                     #if - over 2 means this line is comment line
                    commentcnt = commentcnt +1
                    #print('find - ,commentcnt =',commentcnt)
                elif commentcnt == 1 and char == '-' and validcharcnt == 1: #because - is also validchar
                    commentflag = 1
                    #print('注释行+1')
                    break

                if char !='' and char != ' ' and char !='\n' and char != '\r' :                       #if this line is not empty and not comment line so it is validline
                    validcharcnt = validcharcnt +1
                    #print('validcharcnt + 1',validcharcnt)

            if validcharcnt==0:                     # 1 line for complete and validchar still = 0 so this line is empty line
                emptyline = emptyline +1    
            elif commentflag == 0:
                validline = validline +1            # 1 line for complete and validchar > 0  so this line is valid line
            else:
                commentline = commentline + 1

            #print('one line compelte ,now validcharcnt is',validcharcnt)

        print('总行数为：',totalline)
        print('有效行数为：',validline)
        print('空行数为：',emptyline)
        print('注释行为：',commentline)

    # when file type is verilog
    else :
        BlockCommentFlag1 =0     # for /**/ and # if 0 #endif

        for line in file.readlines():
            totalline = totalline +1
            commentcnt = 0
            commentflag = 0
            validcharcnt = 0
            #print(line)    #for debug
            for char in line:                                          
                if char == '/' and validcharcnt == 0:                    # the first valid char is '/'  #if / over 2 means this line is comment line
                    commentcnt = commentcnt +1
                    #print('find - ,commentcnt =',commentcnt)
                elif commentcnt == 1 and char == '/' and validcharcnt == 1:     #because / is also validchar    //
                    commentflag = 1
                    #print('注释行+1')
                    break
                elif commentcnt == 1 and char =='*' and validcharcnt == 1:        # /*  start
                    BlockCommentFlag1 = 1
                    break

                if char =='*' and validcharcnt == 0:  # the first valid char is '*'
                    commentcnt = commentcnt +1
                elif commentcnt == 1 and char =='/' and validcharcnt == 1 :      # */ complete
                    BlockCommentFlag1 = 0
                    commentline = commentline +1        # because this line is also comment line
                    break

                if char !='' and char != ' ' and char !='\n' and char != '\r' :                       #if this line is not empty and not comment line so it is validline
                    validcharcnt = validcharcnt +1
                    #print('validcharcnt + 1',validcharcnt)
                
            if validcharcnt==0:                     # 1 line check complete and validchar still = 0 so this line is empty line
                emptyline = emptyline +1    
            elif commentflag == 0 and BlockCommentFlag1 == 0 :
                validline = validline +1            # 1 line check complete and validchar != 0 and it isn't comment line, so this line is valid line
            else:
                commentline = commentline +1
            #print('one line compelte ,now validcharcnt is',validcharcnt)

        print('总行数为：',totalline)
        print('有效行数为：',validline)
        print('空行数为：',emptyline)
        print('注释行为：',commentline)

# close file
#file.close()

str = input('push any key exit')