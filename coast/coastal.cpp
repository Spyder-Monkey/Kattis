#include <iostream>
#include <tuple>
#include <string>

using std::cout;
using std::cin;
using std::endl;
using std::tuple;

int
get_coast();

int
main()
{

    return 0;
}

int
get_coast()
{
    auto unvisted = {tuple<int, int> (0, 0)};
    int coast_length = 0;


    while(std::tuple_size<decltype(unvisted) > 0)
    {
        
    }

    return coast_length;
}