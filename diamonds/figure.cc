#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

void createRow(int side, int number_of_pre_spaces){
    string space = " ";
    string symbol = "*";
    string row = "";
    
    for(int i = 0; i < side*2; i++){
        if(i == 0){
            for(int j = 0; j< number_of_pre_spaces; j++){
              row = row + space;
            }
        }
        else if(i % 2 == 0){
            row = row + space;
        }
        else{
            row = row + symbol;
        }
    }
    cout << row << endl;
}

int main() {
    int side;

    printf("Numero de * en un lado: ");
    scanf("%d", &side);

    for(int i = side-1; i >= 0; i--){
        createRow(side-i, i);
    }
    for(int i = 1; i < side; i++){
        createRow(side-i, i);
    }
}