class LRUCache {
    private Map<Integer,Integer> map=new LinkedHashMap();
    private int capacity;
    private int count=0;
    public LRUCache(int capacity) {
        this.capacity=capacity;
    }
    
    public int get(int key) {
        if (map.containsKey(key)){
            int value=map.get(key);
            map.remove(key);
            map.put(key,value);
            return value;
        }else{
            return -1;
        }
    }
    
    public void put(int key, int value) {
        if (map.containsKey(key)){
            map.remove(key);
            count--;
        }else if (count>=capacity){
            int temp=map.entrySet().iterator().next().getKey();
            map.remove(temp);
            count--;
        }
        count++;
        map.put(key,value);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */