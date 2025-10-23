 nums=[2,3,4,5,6,7,8,9,10]
 e=sum(n%2==0 for n in nums)
 o=sum(n%2 for n in nums)
 print(f"Even:{e} Odd:{o}")
