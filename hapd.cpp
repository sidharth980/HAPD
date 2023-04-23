#include "radar.h"
#include <iostream>
#include <string>

using namespace std;

int main(){
    int num = 180;
    string s = "csv/"+to_string(num)+".csv";
    radar(s);
}