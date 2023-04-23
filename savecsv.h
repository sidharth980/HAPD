#include <iostream>
#include <fstream>
#include <vector>
#include <string>

// Function to save vector<vector<double>> as CSV
void saveAsCsv(const std::vector<std::vector<double>>& data, const std::string& filename) {
    std::ofstream file(filename); // Open the file for writing

    if (file.is_open()) {
        for (const auto& row : data) {
            for (size_t i = 0; i < row.size(); ++i) {
                file << row[i]; // Write the element

                if (i < row.size() - 1) {
                    file << ","; // Add a comma to separate values
                }
            }
            file << std::endl; // Add a newline character to separate rows
        }

        file.close(); // Close the file
        std::cout << "Data saved successfully to '" << filename << "'" << std::endl;
    } else {
        std::cerr << "Failed to open file '" << filename << "' for writing" << std::endl;
    }
}

// int main() {
//     // Example data
//     std::vector<std::vector<double>> data = {{1.2, 2.3, 3.4},
//                                              {4.5, 5.6, 6.7},
//                                              {7.8, 8.9, 9.0}};

//     std::string filename = "data.csv"; // Specify the filename
//     saveAsCsv(data, filename); // Call the function to save the data to CSV

//     return 0;
// }
