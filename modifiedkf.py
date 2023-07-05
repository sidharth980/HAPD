import numpy as np

class KalmanFilterM:
    def __init__(self):
        self.velocity = None
        self.position = None

    def update(self, position = [None,None,None]):
        if self.velocity is None:
            if self.position is not None:
                self.velocity = position - self.position
            self.position = position
            return self.predict()
        else:
            estimated_position = self.predict()
            difference = (estimated_position - position) * 0.75
            self.velocity -= difference
            self.position = position
            return [self.predict(),estimated_position]

    def predict(self):
        if self.velocity is None:
            return 0
        else:
            return self.position + self.velocity

# k = KalmanFilterM()
# pos = np.array([[0,0,0,],[0,2,2],[0,4,5],[0,6,5],[0,8,8]],dtype=float)
# for x in pos:
#     ret = k.update(x)
#     print(f"Current Position is : {ret}")
 


def update(x,position,velocity): # int update(position,velocity)
    estimated_position = predict(position,velocity)
    difference = (estimated_position - x) * 0.75
    velocity = velocity - difference
    position = x
    return position,velocity

def predict(position,velocity): # int predict(position,velocity){
    return position + velocity
#}



if __name__ == '__main__': # int main(){
    x = [1,2,3,4,5]
    position = 0
    velocity = 0
    for y in x:
        position,velocity = update(y,position,velocity)
        print(predict(position,velocity))
    #return 0;
#}