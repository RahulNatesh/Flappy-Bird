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
      op=int(input('''[1]count tot. no. of words present in the file
[2]Print the palindrome  words present in the file
[3]Print the words ending and beginning with a vowel 
enter your choice:'''))
      print()

      if op==1:
         n=f.read()
         m=n.split()
         print('no. of words prensent in the file is:',len(m))
      elif op==2:
         n=f.read()
         m=n.split()
         c=0
         print('palindrome words. are')
         for i in m:
            a=i[::-1]
            if a==i:
               print(i)
               c+=1
         if c==0:
             print('not found')
         else:
            print('total no. of palindrome words are:',c)
      elif op==3:
         n=f.read()
         m=n.split()
         c=0
         print('words starting and ending with vowels are.')
         for i in m:
            if (i[0].lower() in "aeiou") and i[len(i)-1].lower() in 'aeiou':
               print(i)
               c+=1
         if c==0:
            print('not found')
         else:
            print('total no. words starting and ending with vowels are:',c)
            
         
      f.close()
      ch2=input('[y] to cont with diff. option:').lower()
   ch1=input('[y] to cont. with diff. txt file:').lower()
   print('=====================================================================')
