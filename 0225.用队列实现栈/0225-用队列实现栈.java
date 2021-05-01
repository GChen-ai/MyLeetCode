class MyStack {
    private Deque<Integer> deque1=new LinkedList();
    private Deque<Integer> deque2=new LinkedList();
    /** Initialize your data structure here. */
    public MyStack() {

    }
    
    /** Push element x onto stack. */
    public void push(int x) {
        while (!deque1.isEmpty()){
            deque2.add(deque1.peek());
            deque1.poll();
        }
        deque1.add(x);
        while (!deque2.isEmpty()){
            deque1.add(deque2.peek());
            deque2.poll();
        }
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        int result=deque1.peek();
        deque1.poll();
        return result;
    }
    
    /** Get the top element. */
    public int top() {
        return deque1.peek();
    }
    
    /** Returns whether the stack is empty. */
    public boolean empty() {
        return (deque1.isEmpty() && deque2.isEmpty());
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */