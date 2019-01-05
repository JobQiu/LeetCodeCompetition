

public boolean areSentencesSimilarTwo(String[] a, String[] b, String[][] pairs){

  if(a.length != b.length ){
    return false;
  } // END of if

  Map<String, String> map = new HashMap();

  for(String[] pair: pairs){
    String p1 = find(m, pair[0]), p2 = find(m, pair[1]);
    if(! p1.equals(p2)){
      m.put(p1, p2);
    } // end of if

  } // END of for

  for(int i = 0; i < a.length ; i++){
    if(!a[i].equals(b[i]) && !find(m,a[i]) .equals(m, b[i])){
      return false;

    } // END of if
  } // END of for i

  return  true;
}

public String find(Map<String, String> m, String s){
  if(! m.containsKey(s)){
    m.put(s, s);
  } // END of if

// find the root
  return s.equals(m.get(s)) ? s: find(m, m.get(s));
}
