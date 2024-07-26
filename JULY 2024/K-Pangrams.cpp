class Solution {
  public:

    bool kPangram(string str, int k) {
        // code here
        unordered_map<char,int>m;
        int count = 0;
        for(auto it:str){
            if(it==' '){
                continue;
            }
            else if(m.find(it)!=m.end()){
                count++;
            }
            else{
                m[it]++;
            }
        }
        int req = 26-m.size();
        if(req-k<=0 && count-req>=0){
            return true;
        }
        return false;
    }
};
