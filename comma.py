def comma(x):
    result =''
    for index,item in enumerate(x):
        if(index == len(x)-1):
            result =result +'and '+ item +' are soft'
        else:
            result = result + item +','
    print(result)

spam = ['marshmelo', 'bananas', 'tofu', 'sponge','gum','slime','ferhat']
comma(spam)