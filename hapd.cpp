#include "radar.h"
#include <iostream>
#include <string>
#include "kalman.hpp"

using namespace std;

int main(){
    KFilter kf;
    for(int i = 30;i<80;i++){
    string s = "csv/"+to_string(i)+".csv";
    // cout<<i<<endl;
    double val = radar(s)*50/256;
    if(val!=0){
    double pred = kf.Update(val);
    cout<<i<<" Distance : "<<pred<<" , "<<val<<endl;

    // cout<<val<<endl;

    }
}
}