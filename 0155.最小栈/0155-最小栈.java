class MinStack {
    private List<Integer> stack=new ArrayList();
    private List<Integer> min=new ArrayList();
    /** initialize your data structure here. */
    public MinStack() {

    }
    
    public void push(int x) {
        if(min.isEmpty() || x<=min.get(min.size()-1)) min.add(x); 
        stack.add(x);
    }
    
    public void pop() {
        if ((min.get(min.size()-1)).equals(stack.get(stack.size()-1))) min.remove(min.size()-1);
        stack.remove(stack.size()-1);
    }
    
    public int top() {
        return stack.get(stack.size()-1);
    }
    
    public int getMin() {
        return min.get(min.size()-1);
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */