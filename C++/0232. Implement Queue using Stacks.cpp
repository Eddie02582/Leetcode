class MyQueue {
public:
    
    stack<int>st;
    
    MyQueue() {
        
    }
    void push(int x) {
        
        stack<int>temp;
        
        while(!st.empty()){
            temp.push(st.top());
            st.pop();
        }
        st.push(x);
        
        while(!temp.empty()){
            st.push(temp.top());
            temp.pop();
        }
    }
    
    int pop() {
        int k = st.top();
        st.pop();
        return k;
    }
    
    int peek() {
        int k = st.top();
        return k;
    }
    
    bool empty() {
        return st.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */