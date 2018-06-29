from functools import reduce
def predict(input_vec,weights):
    return reduce(lambda a,b:a+b,map(lambda x,w:x*w,input_vec,weights),0.0)+0.1
print(predict([1,2],[1,1]))

