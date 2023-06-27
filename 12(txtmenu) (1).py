ch1='y'
while ch1=='y':
   f=open('sample.txt','w')
   n=int(input('enter no. of lines you want to implement:'))
   for i in range(n):
      print('line',i+1,':',end='')
      n=input()
      f.write(n+'\n')
      
   ch2='y'
   while ch2=='y':
      print()
      f=open('sample.txt','r')
      op=int(input('''[1]Check no of lines starting with a vowel
[2]no of lines containing u and write such lines into another file 'Sample2'
[3]To convert upper to lowercase and viceversa and write it in another file:
    enter your choice'''))
      print()

      if op==1:
         n=f.readlines()
         cnt=0
         t=""
         for i in n:
            if i[0].lower() in 'aeiou':
               cnt+=1
               t+=i+"\n"
         print('no. of lines starting with a vowel are:',cnt)
         print("they are :\n",t)      
      elif op==2:
         cnt=0
         t=open('sample2.txt','w')
         n=f.readlines()
         y=""
         for i in n:
            for j in i:
               if j.lower()=='u':
                  cnt+=1
                  t.write(i)
                  y+=i
                  break
         print('no of lines containing u are:',cnt)      
         t.close()     
      elif op==3:
         n=f.readlines()
         f=open('sample.txt','w')   
         a=''
         print("new txt file:")
         for j in n:
            txt=''
            for i in j:
               if i.isspace():            
                  if a!='':
                     txt+=a+" "
                     a=''
               else:
                  if i.isupper():
                     i=i.lower()
                  else:
                     i=i.upper()
                  a+=i
            print("\n",txt)
            f.write(txt+'\n')
      f.close()
      print()
      ch2=input('[y] to cont with different choice:').lower()
   ch1=input('[y] to cont. with different txt file:').lower()
   print('=====================================================================')
