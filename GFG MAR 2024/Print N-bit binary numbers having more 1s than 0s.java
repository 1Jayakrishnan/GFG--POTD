class Solution {
    ArrayList<String> NBitBinary(int N) {
        ArrayList<String> al=new ArrayList<>();
        if(N==1){
            al.add("1");
            return al;
        }
        for(int i=(int)Math.pow(2,N);i>0;i--){
            String x=Integer.toBinaryString(i);
            boolean b=funct(x);
            if(b==true & x.length()==N){
                al.add(x);
            }
        }
       
        
        return al;
    }
    boolean funct(String s){
        int o=0;int z=0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='0'){z++;}else{o++;}
            if(z>o){
                return false;
            }
        }
        return true;
    }
}
