// #include <iostream>
// #include <vector>
// #include <cmath>
// using namespace std;

// #define PI 3.14159265

// vector<vector<float>> fft2d(vector<vector<float>> data) {
//     int height = data.size();
//     int width = data[0].size();
//     vector<vector<float>> realOut(height, vector<float>(width));
//     vector<vector<float>> imgOut(height, vector<float>(width));
//     vector<vector<float>> ampOut(height, vector<float>(width));

//     for (int yWave = 0; yWave < height; yWave++) {
//         for (int xWave = 0; xWave < width; xWave++) {
//             for (int ySpace = 0; ySpace < height; ySpace++) {
//                 for (int xSpace = 0; xSpace < width; xSpace++) {
//                     realOut[yWave][xWave] += (data[ySpace][xSpace] * cos(2 *
//                         PI * ((1.0 * xWave * xSpace / width) + (1.0 * yWave * ySpace /
//                         height)))) / sqrt(width * height);
//                     imgOut[yWave][xWave] -= (data[ySpace][xSpace] * sin(2 * PI
//                         * ((1.0 * xWave * xSpace / width) + (1.0 * yWave * ySpace / height)))) /
//                         sqrt(width * height);
//                 }
//                 ampOut[yWave][xWave] = sqrt(
//                     realOut[yWave][xWave] * realOut[yWave][xWave] +
//                     imgOut[yWave][xWave] * imgOut[yWave][xWave]);
//             }
//         }
//     }

//     return realOut;
// }

// int main(int argc, char **argv) {
//     int n;
//     cout << "Enter the size: ";
//     cin >> n;
//     vector<vector<float>> data = {{1,2},{3,4}};
//     cout << "Enter the 2D elements ";
//     // for (int i = 0; i < n; i++) {
//     //     for (int j = 0; j < n; j++) {
//     //         cin >> data[i][j];
//     //     }
//     // }
//     vector<vector<float>> realPart = fft2d(data);
//     cout << "Real part of 2D FFT:\n";
//     for (int i = 0; i < n; i++) {
//         for (int j = 0; j < n; j++) {
//             cout << realPart[i][j] << " ";
//         }
//         cout << endl;
//     }
// }



// #include <iostream>
// #include <fstream>
// #include <sstream>
// #include <cstring>
// #include <cstdio>
// #include <cstdlib>
// #include <cmath>
// #include <vector>
// #include <set>
// #include <iterator>
// #include <algorithm>
// #include <ctime>

// #include "mex.h"

// using namespace std;

// void vector2matrix(double *input, int nRows, int nCols, double **output) {
//     for (int i = 0; i < nRows; ++i) {
//         for (int j = 0; j < nCols; ++j) {
//             output[i][j] = input[j * nRows + i];
//         }
//     }
// }

// void matrix2vector(double **input, int nRows, int nCols, double *output) {
//     for (int i = 0; i < nRows; ++i) {
//         for (int j = 0; j < nCols; ++j) {
//             output[j * nRows + i] = input[i][j];
//         }
//     }
// }

// Fast Fourier Transform 1D for real signals
// void FFT_real(double *Signal, double *Re_F, double *Im_F, int N, int t) {
//     if (N == 1) {
//         Re_F[0] = Signal[0];
//         Im_F[0] = 0.0;
//         return;
//     }
    
//     int half = N / 2;
//     FFT_real(Signal, Re_F, Im_F, half, 2 * t);
//     FFT_real(Signal + t, Re_F + half, Im_F + half, half, 2 * t);
    
//     for (int k = 0; k < half; ++k) {
//         double r1 = Re_F[k];
//         double i1 = Im_F[k];
        
//         double r2 = Re_F[k + half];
//         double i2 = Im_F[k + half];
        
//         double alpha = - 2.0 * M_PI * (double)(k) / (double)(N);
//         double r3 = cos(alpha);
//         double i3 = sin(alpha);
        
//         double r4 = r2 * r3 - i2 * i3;
//         double i4 = r3 * i2 + r2 * i3;
        
//         Re_F[k] = r1 + r4;
//         Im_F[k] = i1 + i4;
        
//         Re_F[k + half] = r1 - r4;
//         Im_F[k + half] = i1 - i4;
//     }
// }

// int main() {
//     // Example usage
//     vector<vector<float>> data = {{1, 2},{ 3, 4}};
//     fft2d(data);
//     for (int i = 0; i < data.size(); i++) {
//         for (int j = 0; j < data[0].size(); j++) {
//             cout << data[i][j] << " ";
//         }
//         cout << endl;
//     }
//     return 0;
// }

// THIS WORKS DO NOT REMOVE

// #include <iostream>
// #include <complex>
// #include <vector>
// #include <cmath>

// std::vector<std::complex<double>> FFT(std::vector<std::complex<double>>& x) {
//     int N = x.size();
//     if (N == 1) {
//         return x;
//     } else {
//         std::vector<std::complex<double>> X_even, X_odd;
//         for (int i = 0; i < N; i += 2) {
//             X_even.push_back(x[i]);
//         }
//         for (int i = 1; i < N; i += 2) {
//             X_odd.push_back(x[i]);
//         }

//         X_even = FFT(X_even);
//         X_odd = FFT(X_odd);

//         std::vector<std::complex<double>> X(N);
//         std::complex<double> factor;
//         for (int i = 0; i < N; i++) {
//             factor = std::exp(std::complex<double>(0, -2.0 * M_PI * i / N));
//             if (i < N / 2) {
//                 X[i] = X_even[i] + factor * X_odd[i];
//             } else {
//                 X[i] = X_even[i - N / 2] + factor * X_odd[i - N / 2];
//             }
//         }
//         return X;
//     }
// }

// int main() {
//     // Define the input vector
//     std::vector<std::complex<double>> x = {{1, 0}, {2, 0}, {3, 0}, {4, 0}};

//     // Display the input vector
//     std::cout << "Input Vector:" << std::endl;
//     for (int i = 0; i < x.size(); i++) {
//         std::cout << "(" << x[i].real() << ", " << x[i].imag() << ") ";
//     }
//     std::cout << std::endl;

//     // Perform FFT
//     std::vector<std::complex<double>> X = FFT(x);

//     // Display the FFT result
//     std::cout << "FFT Result:" << std::endl;
//     for (int i = 0; i < X.size(); i++) {
//         std::cout << "(" << X[i].real() << ", " << X[i].imag() << ") ";
//     }
//     std::cout << std::endl;

//     return 0;
// }


#include <iostream>
#include <vector>
#include <complex>
#include <cmath>

std::vector<std::complex<double>> FFT(std::vector<double>& x) {
    int N = x.size();
    std::vector<std::complex<double>> X(N);
    
    if (N == 1) {
        X[0] = x[0];
        return X;
    } else {
        std::vector<double> x_even;
        std::vector<double> x_odd;
        for (int i = 0; i < N; i++) {
            if (i % 2 == 0) {
                x_even.push_back(x[i]);
            } else {
                x_odd.push_back(x[i]);
            }
        }
        
        std::vector<std::complex<double>> X_even = FFT(x_even);
        std::vector<std::complex<double>> X_odd = FFT(x_odd);
        
        std::complex<double> factor;
        for (int i = 0; i < N; i++) {
            factor = std::exp(std::complex<double>(0, -2.0 * M_PI * i / N));
            if (i < N / 2) {
                X[i] = X_even[i] + factor * X_odd[i];
            } else {
                X[i] = X_even[i - N / 2] + factor * X_odd[i - N / 2];
            }
        }
        
        return X;
    }
}

// int main() {
//     // Define the input vector
//     std::vector<double> x = {1, 2, 3, 4};

//     // Display the input vector
//     std::cout << "Input Vector:" << std::endl;
//     for (int i = 0; i < x.size(); i++) {
//         std::cout << x[i] << " ";
//     }
//     std::cout << std::endl;
    
//     // Perform FFT
//     std::vector<std::complex<double>> X = FFT(x);

//     // Display the FFT result
//     std::cout << "FFT Result:" << std::endl;
//     for (int i = 0; i < X.size(); i++) {
//         std::cout << X[i].real() << " ";
//     }
//     std::cout << std::endl;

//     return 0;
// }
