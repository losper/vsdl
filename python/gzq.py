from functools import reduce
class Perceptron(object):
    def __init__(self,input_num,activator):
        self.activator=activator
        self.weights=[0.0 for _ in range(input_num)]
        self.bias=0.0

    def __str__(self):
        return "weights\t:%s\nbias\t:%f\n" %(self.weights,self.bias)

    # def predict(self,intput_vec):
    #     return self.activator(
    #         reduce(lambda a,b:a+b,map(lambda (x,w):x*w,zip(input_vec,self.weights)),0.0)+self.bias)
    #     )
def f(x):
    return 1 if x>0 else 0

p=Perceptron(2,f)
print(p)
y=zip([1,2,3,4],[1,2,3,4])
z=map(lambda x,w:x*w,[1,2],[2,3])
print(reduce(lambda a,b:a+b,z))
print(list(z))
