#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

// Function to split a string by a delimiter and store the substrings in a vector
std::vector<std::string> split(const std::string& s, char delimiter) {
    std::vector<std::string> tokens;
    std::istringstream iss(s);
    std::string token;
    while (std::getline(iss, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

// Function to read CSV file as vector<vector<double>>
std::vector<std::vector<double>> readCSV(const std::string& file_path) {
    // Open the CSV file for reading
    std::ifstream file(file_path);
    if (!file.is_open()) {
        std::cout << "Failed to open file: " << file_path << std::endl;
        return {};
    }

    // Read the CSV file line by line
    std::string line;
    std::vector<std::vector<double>> data;
    while (std::getline(file, line)) {
        // Split the line by commas
        std::vector<std::string> tokens = split(line, ',');

        // Convert the tokens to double and store in a vector
        std::vector<double> row;
        for (const std::string& token : tokens) {
            row.push_back(std::stod(token));
        }

        // Store the row in the data vector
        data.push_back(row);
    }

    // Close the CSV file
    file.close();

    return data;
}

// int main() {
//     std::string file_path = "data.csv";
//     std::vector<std::vector<double>> data = readCSV(file_path);
//     return 0;
// }
