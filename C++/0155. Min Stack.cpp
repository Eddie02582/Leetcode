#include<stack>

using namespace std;
class MinStack {
	private:
		std::stack<int> data;
		std::stack<int> minstack;    
	public:
    MinStack() {        
    }
    
    void push(int x) {
        data.push(x);
        if (minstack.empty() || x < minstack.top()) {
            minstack.push(x);
        }
        else {
            minstack.push(minstack.top());
        }
    }
    
    void pop() {
        if (data.empty()) {
            std::cout << "Stack is empty.\n";
            return;
        }
        data.pop();
        minstack.pop();
    }
    
    int top() {
        if (data.empty()) {
            std::cout << "Stack is empty.\n";   // sorry for the bad exception handling
            return -1;                          
        }

        return data.top();

    }
    
    int getMin() {
        if (data.empty()) {
            std::cout << "Stack is empty.\n";
            return -1;
        }

        return minstack.top();
    }
};