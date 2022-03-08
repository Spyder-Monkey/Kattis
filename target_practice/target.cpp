#include <bits/stdc++.h>

using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::pair;

typedef long long ll;

bool is_line(pair<ll, ll>& p1, pair<ll, ll>& p2, pair<ll, ll>& p3)
{
    return (p2.first - p1.first) * (p3.second - p1.second) == (p2.second - p1.second) * (p3.first - p1.first);
}

int
main()
{
    std::ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n;
    cin >> n;

    if(n <= 4)
    {
        cout << "success" << endl;
        return 0;
    }

    vector<pair<ll, ll>> coords(n);
    for(auto& i : coords)
    {
        cin >> i.first >> i.second;
    }

    bool found = false;
    int p1, p2, p3;

    for(int i = 0; i < 5; ++i) {
        for(int j = i+1; j < 5; ++j) {
            for(int k = j+1; k < 5; ++k) {
                if(is_line(coords[i], coords[j], coords[k])) {
                    found = true;
                    p1=i;p2=j;p3=k;
                }
            }
        }
    }

    if(!found) {
        cout << "failure" << endl;
        return 0;
    }

    vector<pair<ll, ll>> r;
    for(auto i : coords) {
        if(!is_line(coords[p1], coords[p2], i)) {
            r.push_back(i);
        }
    }

    bool works = true;
    for(int i = 2; i < r.size(); ++i) {
        if(!is_line(r[i], r[i-1], r[i-2])) {
            works = false;
            break;
        }
    }

    if(works)
        cout << "success" << endl;
    else
        cout << "failure" << endl;
}