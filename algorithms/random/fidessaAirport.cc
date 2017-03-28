/*
 * Complete the function below.
 */
#include <algorithm>

using namespace std;

int findMinGates(vector < int > arrivals, vector < int > departures, int flights) {
    auto mingates = 1, gates = 1;
    sort(begin(arrivals), end(arrivals));
    sort(begin(departures), end(departures));
    
    auto aindex = 1, dindex = 0;
    while (aindex < flights && dindex < flights) {
        if (arrivals[aindex] <= departures[dindex]) {
            gates++;
            aindex++;
            mingates = (mingates < gates) ? gates : mingates;
        } else {
            gates--;
            dindex++;
        }
    }
   
    return mingates;
}
