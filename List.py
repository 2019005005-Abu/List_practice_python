###List
number=[10,20,30,40];
sum=0;
for i in range(len(number)):
    sum=sum+number[i];
    print(sum);
lst1=[5,16.0,'Python 3.6'];
print(id(lst1))
ls2=[34,56,90,'Rifat'];
ls2.append(100);
ls2.append(200);
print(ls2);
print(f"Memory address {ls2}",id(ls2));
print(ls2[-2]);
print(ls2[-1]);
print(ls2[:]);
print(ls2[0:3]);
print(ls2[1:3]);
print(ls2[:3]);
print(ls2[1:]);
print(ls2[:]);
print(ls2[0:]);
lsit3=[2,4,6,8,10];
print(lsit3[::-1]);
lIst4=[-5,-6,-7,2,4,8,9];
list5=[x for x in lIst4];
print(list5);
list6=[y for y in list5];
print(list6);
list7=[(x**2) for x in list6];
print(list7);
list8=[(x**2) for x in list7 if x>0];
list9=[(x**3) for x in list8 if x>0];
###[Object.method()]
list10=[5,7,9,10,2,5,7,30,4];
list10.append([8,23,45]);
print(list10);
###Object.extend()
List11=list9.extend('dog');
print(List11);
##
List12=list5+list6;
print(List12);

first_List=[10,20,30,40,50];
last_List=[60,70,80,90,100];
##List.insert()
print(first_List.insert(0,'dog'));
print(first_List)
##List.remove();
print(first_List.remove(10));
print(first_List.remove(30));
print(first_List);
##List.index()
print(even_Number.index(4));
##List.count()
print(last_List.count(4));
##List.push()
print(LL2.push(1000))
##List.pop()
print(last_List.pop());
##List Reverse();
even_Number=[2,4,6,8,10]
print(even_Number.reverse());
##List.sort
N=[8,4,90,34,76,1];
print(N.sort());
#List.copy;
print(N.copy());
##List.clear
print(N.clear());

L1=[10,20,30];
L2=L1;
print(L1 is L2);
L2.append(100);
print(L2);
##List.copy();
L3=L2.copy();
print(L3);

############################
L4=[10,20,30,40,50,60];
LL1=['Have','a','good','day'];
print(''.join(LL1));
LL2=['I','am','working','as' ,'a','software','enginner' ];
print(''.join(LL2));

Nested_List=[[10,20,30],[40,50,60]];
print(Nested_List);

Nested_List1=[[10,20,30,40],[78,90,56],[56,90,67]];
print(Nested_List1[2]);

Nested_List3=[1,23,45,[67,90,56],[34,90,90]];
print(Nested_List3);








