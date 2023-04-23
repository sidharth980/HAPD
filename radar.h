#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cmath>
#include "readcsv.h"
#include "fft.h"
#include "savecsv.h"

using namespace std;


// int main() {
//     std::string file_path = "data.csv";
//     std::vector<std::vector<double>> data = readCSV(file_path);
    
    
//     std::vector<std::vector<double>> dataout;
    // vector<vector<double>> data = {
    // {1,2,2,1},
    // {1,2,3,1},
    // {1,2,4,2},
    // {1,2,2,2},
    // {1,2,3,3},
    // {1,1,1,1}};
    // for(int i = 0;i<data.size();i++){
    //     vector<double> x = data[i];
    //     std::vector<std::complex<double>> X = FFT(x);
    //     std::vector<double> temp;
    //     for (int j = 0; j < X.size(); j++) {
    //         temp.push_back(X[j].real());
    //     }
    //     dataout.push_back(temp);
    //     // print 2d vector 
        
    // }
    // saveAsCsv(dataout, "dataout.csv");

    // for(int i = 0;i<dataout.size();i++){
    //     for (int j = 0; j < dataout[i].size(); j++) {
    //         std::cout << dataout[i][j] << " ";
    //     }
    //     std::cout << std::endl;
    //     // print 2d vector 
        
    // }
    // int modi = 96;
    // for (int j = 0; j < data[modi].size(); j++) {
    //         std::cout << data[j][modi] << endl;
    //     }
    //     std::cout << std::endl;
    // cout<< data.size();
// }

// void checkAndPrintLocation(const vector<double>& vec, double value) {
//     bool found = false;
//     int index = -1;

//     // Iterate through the vector to find the value
//     for (int i = 0; i < vec.size(); i++) {
//         if (vec[i] > 10000) {
//             found = true;
//             index = i;
//             break;
//         }
//     }

//     if (found) {
//         cout << "Value " << value << " is greater than 10000 at index " << index << endl;
//     } else {
//         cout << "Value " << value << " is not found in the vector" << endl;
//     }
// }

void radar(string file_path){
    // std::string file_path = "data.csv";
    std::vector<std::vector<double>> data = readCSV(file_path);

    for(int l = 0;l<256;l+=5){
        for(int j = 5;j<221;j++){
            vector<double> temp;
            for(int k = 0;k<5;k++)
            temp.push_back(data[j][l+k]);
            vector<complex<double>> x = FFT(temp);
            if(x[0].real()>12000){
                    cout<<x[0].real()<<" ("<<(l*180/256)-90<<","<<j*50/256<<")"<<endl;
                }
            }
        }
}