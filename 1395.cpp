#define ll int
// My Segment Tree Template (inspired from Pashka)
class item {
    public:
    ll val;
    
    item() {
        val = 0;
    }
    
    item(ll v) {
        val = v;
    }
};
 
class SegTree {
    public:
    ll size;
    vector<item> values;
 
    item NEUTRAL_ELEMENT = item();
 
    item merge(item l,item r) {
        return item(l.val + r.val);
    }
 
    item single(ll v) {
        return item(v);
    }
 
    void init(ll n) {
        size = 1;
        while(size < n) size *= 2; //for last level array with some extra nodes for complete binary tree
        values.resize(2*size -1);  //for complete binary tree
    }
    
    void build(vector<int> &a,ll x,ll lx,ll rx) {
        //base case
        if(rx-lx == 1) {
            if(lx < int(a.size())) {
                values[x] = single(a[lx]);
            }
            return; 
        }
 
        ll m = (lx+rx)/2;
        build(a,2*x +1,lx,m);
        build(a,2*x +2,m,rx);
        values[x] = merge(values[2*x +1],values[2*x +2]);
    }
 
    void build(vector<int> &a) {
        build(a,0,0,size);
    }
 
    void set(ll i,ll v,ll x,ll lx,ll rx) {
        //base case
        if(rx-lx == 1) {
            values[x] = single(v);
            return;
        }
 
        ll m = (lx+rx)/2;
        if(i < m) {
            set(i,v,2*x +1,lx,m);
        }
        else {
            set(i,v,2*x +2,m,rx);
        }
        values[x] = merge(values[2*x+1],values[2*x+2]);
    }
 
    void set(ll i,ll v) {
        set(i,v,0,0,size);
    }

    item calc(ll l,ll r,ll x,ll lx,ll rx) {
        //base cases
        if(lx >= r || l >= rx) return NEUTRAL_ELEMENT;
        if(lx >= l && rx <= r) return values[x];
 
        ll m = (lx+rx)/2;
        item s1 = calc(l,r,2*x+1,lx,m);
        item s2 = calc(l,r,2*x+2,m,rx);
        return merge(s1,s2);
    }   
 
    item query(ll l,ll r) {
        return calc(l,r+1,0,0,size);
    }
};

class Solution {
public:
    int numTeams(vector<int>& rating) {
        int mx = 1e5;
        SegTree st1, st2;
        st1.init(mx), st2.init(mx);
        
        int n = rating.size();
        for(int i=0; i<n; ++i) st2.set(rating[i], 1);

        int res = 0;
        for(int i=0; i<n; ++i) {
            int lefti = st1.query(0,rating[i]-1).val;
            int leftd = st1.query(rating[i]+1,mx).val;
            int righti = st2.query(rating[i]+1,mx).val - leftd;
            int rightd = st2.query(0,rating[i]-1).val - lefti;
            st1.set(rating[i], 1);
            res += lefti * righti + leftd * rightd;
        }
        return res;

    }
};
