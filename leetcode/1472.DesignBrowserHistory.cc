class BrowserHistory {
    vector<string> history;
    int curPage = 0;
public:
    BrowserHistory(string homepage) {
        history.emplace_back(homepage);
    }
    
    void visit(string url) {
        curPage++;
        history.erase(history.begin() + curPage, myvector.end());
        history.emplace_back(url);
    }
    
    string back(int steps) {
        curPage -= (curPage < steps) ? curPage : steps;
        return history[curPage];
    }
    
    string forward(int steps) {
        curPage += ((history.size() - curPage - 1) < steps) ? (history.size() - curPage - 1) : steps;
        return history[curPage];
    }
};

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory* obj = new BrowserHistory(homepage);
 * obj->visit(url);
 * string param_2 = obj->back(steps);
 * string param_3 = obj->forward(steps);
 */