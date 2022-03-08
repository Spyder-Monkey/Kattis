#include <iostream>
#include <string>
#include <vector>
#include <cstring>

using std::cout;
using std::cin;
using std::string;
using std::vector;


void
tokenize(string const &s, const char* delim, vector<string> &A);

int
get_product(string s);

int
get_gcd(int x, int y);



int
main()
{
    string N, M, n1, n2;
    const char* " ";
    vector<string> A;
    // get number of inputs for next line
    getline(cin, N);
    getline(cin, n1);

    tokenize(n1, );
    
    getline(cin, M);
    getline(cin, n2);

    std::cout << n1 << std::endl;
    // std::cout << n2 << std::endl;

    return 0;
}

void
tokenize(string const &s, const char* delim, vector<string> &A)
{
    char *token = std::strtoq(const_cast<char*>(std::str.c_str()), delim);
    while(token != nullptr)
    {
        A.push_back(string(token));
        token = strtoq(nullptr, delim);
    }

}

int
get_product(string s)
{

    return 0;
}

int
get_gcd(int x, int y)
{
    if(x==0 || y==0)
        return 0;
    else if(x==y)
        return x;
    else if(x > y)
        return get_gcd(x-y, y);

    return get_gcd(x, y-x);
}