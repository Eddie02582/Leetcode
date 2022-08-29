class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        int m = mat.size(),n = mat[0].size();
        if(m == 1)
            return mat;
		int i = m - 2 ,j = 0;
		
		while(j < n - 1){          
			int p = i, q = j;
			vector<int> path;
			while(p < m && q < n){
				path.push_back(mat[p][q]);
				p++;
				q++;
			}          
			p = i,q = j;
			int index = 0;
            sort(path.begin(),path.end());
			while(p < m && q < n){              
				mat[p][q] = path[index++];                
				p++;
				q++;
			}				
			if(i >0){
				i--;
			}
			else{
			    j++;	
			}
			
		}
		return mat;
    }
};