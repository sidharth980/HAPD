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
int findMaxPosition(const std::vector<double>& numbers) {
    int maxPos = 0; // Assume the first element as the maximum
    for (int i = 1; i < numbers.size(); i++) {
        if (numbers[i] > numbers[maxPos]) {
            maxPos = i; // Update maxPos if a larger element is found
        }
    }
    return maxPos;
}

int findMaxPositionof2d(const std::vector<vector<double>>& numbers) {
    int maxPos = 0; // Assume the first element as the maximum
    for (int i = 1; i < numbers.size(); i++) {
        if (numbers[i][1] > numbers[maxPos][1]) {
            maxPos = i; // Update maxPos if a larger element is found
        }
    }
    return maxPos;
}

double radar(string file_path){
    // std::string file_path = "data.csv";
    std::vector<std::vector<double>> data = readCSV(file_path);
    vector<vector<double>> poss;
        for(int l = 0;l<256;l+=5){
        vector<double> temp;
        for(int j = 5;j<221;j++){
            
            double t=0;
            for(int k = 0;k<5;k++)
            t+=data[j][l+k];
            // temp.push_back(data[j][l+k]);
            // vector<complex<double>> x = FFT(temp);
            temp.push_back(t/5);
            // if(x[0].real()>12000){
                    // cout<<x[0].real()<<" ("<<(l*180/256)-90<<"deg ,"<<j*50/256<<"m)"<<endl;
                    // return (j*50/256);
                // }
            }
            int pos = findMaxPosition(temp);
            vector<double> ap;
            ap.push_back(pos);
            ap.push_back(temp[pos]);
            poss.push_back(ap);
            // return pos;
        }
    int pos = findMaxPositionof2d(poss);

    if(poss[pos][1]>4000){
    return poss[pos][0];}
    else return 0;
}