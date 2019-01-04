class MedianFinder {

  PriorityQueue<Long> large = new PriorityQueue<>();
  PriorityQueue<Long> small = new PriorityQueue<>();



  /** initialize your data structure here. */
  public MedianFinder() {


  }

  public void addNum(int num) {
    large.offer(long(num));
    small.offer(-(long)(large.poll()));
    if(large.size() < small.size()){
      large.offer(-small.poll());
    } // END of if


  }

  public double findMedian() {

  }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
