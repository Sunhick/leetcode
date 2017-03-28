/*
 * Complete the function below.
 */
#include <stack>

int findMatchingPair(string input) {
    stack<char> stk;
    int index = -1;
    
    for (int i = 0; i < input.length(); i++) {
        auto c = input[i];
        if (isupper(c)) {
            stk.push(c);
            continue;
        } 
        
        if (stk.empty()) {
            break;
        }
        
        // lower case, see if it matches.
        if (c == tolower(stk.top())) {
            // match
            index = i;
            stk.pop();
            continue;
        }
        
        // not a match.
        break;
    }

    return index;
}
