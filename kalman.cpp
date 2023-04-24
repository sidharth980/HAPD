#include <iostream>

using namespace std;

class KFilter {
public:
    KFilter() : vel_(0), n_(1), pos_(0) {}

    double Update(double x = -1) {
        if (x == -1) {
            return Predict(n_);
        } else {
            if (vel_ == 0) {
                if (pos_ != 0) {
                    vel_ = x - pos_;
                }
                pos_ = x;
                return Predict();
            } else {
                double est_pos = Predict();
                double dif = (est_pos - x) / 1.25;
                vel_ = vel_ - dif;
                pos_ = x;
                return Predict();
            }
        }
    }

    double Predict(double pos = -1) {
        if (vel_ == 0) {
            return 0;
        }
        if (pos == -1) {
            n_ = 0;
            return vel_ + pos_;
        } else {
            pos_ = pos_ + vel_;
            return pos_ + vel_;
        }
    }

private:
    double vel_; // Velocity
    int n_;      // Counter
    double pos_; // Position
};

int main() {
    KFilter kf;
    double measurement[] = {5,6,8,10,12,14,16,20,24,28};
    for(int i = 0;i<10;i++){
        double pred = kf.Update(measurement[i]);
        cout<<measurement[i]<<" : "<<pred<<endl;
    }
    // Update with x = 5
    return 0;
}
