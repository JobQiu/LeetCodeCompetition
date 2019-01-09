class ExamRoom{
  PriorityQueue<Interval> pq ;
  int N;

  class Interval{
    int x, y, distance;
    public Interval(int x, int y){
      this.x = x;
      this.y = y;
      if(x==-1){
        this.distance = y;
      } // END of if
      else if(y==N){
        this.distance = N - 1 - x;

      } // END of if
      else{
        this.distance = Math.abs(y-x) / 2;
      }

    }
  }

  public ExamRoom(int N){
    this.pq = new PriorityQueue<>((a,b) -> a.distance != b.distance? b.distance - a.distance : a.x - b.x);
    this.N = N;
    pq.add(new Interval(-1, N));


  }

  public int seat(){
    
  }

}
