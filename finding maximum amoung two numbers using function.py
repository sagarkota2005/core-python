#finding maximum amoung two numbers using function

#creating a function called maximum  
def maximum(num1,num2):
    #here we are comparing num1 with num2
    if num1 > num2:
        print(f"num1 is maximum number {num1}")
        #here if 'if' statement gets true then it will print if block 
    else:
        print(f"num2 is maximum number {num2}")
        #here if 'if' statement gets false then it will print else block 
obj=maximum(23,30)#here we are assining the values
