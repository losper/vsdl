from perceptron import Perceptron

def f(x):
    return 1 if x>0 else 0
def get_training_dataset():
    input_vecs=[[1,1],[0,0],[1,0],[0,1]]
    labels=[1,0,0,0]
    return input_vecs,labels

p=Perceptron(2,f)
input_vecs,labels=get_training_dataset()
p.train(input_vecs,labels,10,0.1)
print(p)
print(p.predict([1,1]))
print(p.predict([12,3]))
