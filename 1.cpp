// reading a text file
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
  string line;
  ifstream myfile ("input/1.txt");
  string lines[1000];
  if (myfile.is_open())
  {
    int i = 0;
    while ( getline (myfile,line) )
    {
        // lines[i] = strcpy(line);
        i++;
    }
    myfile.close();
  }
  else cout << "Unable to open file"; 

  return 0;
}

