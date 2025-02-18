class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        vector<bool> visited(rooms.size(),false);
		dfs(rooms,0,visited);		
		for(auto isVisited :visited ){           
			if(!isVisited)
				return false;
		}
		return true;
    }	
	void dfs(vector<vector<int>>& rooms,int currRoomNumber,vector<bool> &visited) {
		if(visited[currRoomNumber])
			return;
		visited[currRoomNumber]	= true;
		for(auto roomNumber:rooms[currRoomNumber]){
			dfs(rooms,roomNumber,visited);			
		}		
	}
};