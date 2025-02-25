class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        vector<int> ret;
        sort(potions.begin(), potions.end());
        
        for (int spell : spells) {
            // Calculate the threshold n = success / spell
            long long n = (success + spell - 1) / spell; // We use this to avoid floating-point operations
            int successCount = binarySearch(potions, n);
            ret.push_back(successCount);
        }
        
        return ret;
    }
	//第一個大於等於n的數字
	int binarySearch(vector<int>& potions, long long n) {
        int start = 0, end = potions.size() - 1;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (potions[mid] >= n) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }        
        // After the loop, start points to the first potion >= n
        return potions.size() - start; // Return the number of successful pairs
	}
	
	vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        sort(potions.begin(), potions.end());
        vector<int> res;
        for (int a: spells) {
            long need = (success + a - 1) / a;
            auto it = lower_bound(potions.begin(), potions.end(), need);
            res.push_back(potions.end() - it);
        }
        return res;
    }
	
};
