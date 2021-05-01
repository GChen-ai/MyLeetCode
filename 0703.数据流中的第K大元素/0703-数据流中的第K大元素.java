class KthLargest {
    PriorityQueue<Integer> pq;
    int k;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        pq = new PriorityQueue<Integer>();
        for (int x : nums) {
            add(x);      
        }
    }
    
    public int add(int val) {
        pq.offer(val);
        if (pq.size() > k) {     // 维持 队列的大小与kk值相等
            pq.poll();    //弹出元素   
        }
        return pq.peek();
    }
}
