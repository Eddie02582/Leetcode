class Solution {
public:
    int nearestValidPoint(int x, int y, vector<vector<int>>& points) {
         ios::sync_with_stdio(false); cin.tie(nullptr);
        int index = -1;
        int distance = 9999;
        for(int i = 0; i < points.size();i++){  
            if(x ==  points[i][0] || y ==  points[i][1]){     
                int temp =  abs(y -  points[i][1]) + abs(x -  points[i][0]);               
                if(temp < distance){
                    index = i;
                    distance = temp;
                }              
            }
            
        }
        return index;
    }
};