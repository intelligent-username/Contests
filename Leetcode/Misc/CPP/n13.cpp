// Daily problem for September 21st, 2025
// https://leetcode.com/problems/design-movie-rental-system/
// COMPLETE
#include <tuple>
#include <set>
#include <map>
#include <vector>
#include <utility>

class MovieRentingSystem {
public:
    // For comparing movies, prioritizes
    // Returns by lowest price. In case of a tie of price, 
    // we have: price > shop id > movie id
    struct Comparator {
        bool operator()(const tuple<int,int,int>& a, const tuple<int,int,int>& b) const {
            if (get<0>(a) != get<0>(b)){
                return get<0>(a) < get<0>(b); // Sort by price
            } else if (get<1>(a) != get<1>(b)) {
                return get<1>(a) < get<1>(b); // Sort by shopID
            }
            return get<2>(a) < get<2>(b); // If still a tie, by movie ID
        }

    };

    int shops;
    set<tuple<int,int, int>, Comparator > unavailable;
    map<int, set<pair<int,int>>> available;
    map<pair<int,int>, int> prices;  // (shop, movie) -> price lookup


    MovieRentingSystem(int n, vector<vector<int>>& entries) {
        // Initializes the MovieRentingSystem object with n shops and the movies in entries
        // entries has [shop, movie, price] in that order
        for (const auto& e : entries) {
            int shop = e[0];
            int movie = e[1];
            int price = e[2];

            prices[{shop, movie}] = price;                      // populate price lookup
            available[movie].insert({price, shop});    // insert into per-movie available set
        }
    }
    
    vector<int> search(int movie) {
        // Returns a list of shops that have an unrented copy of the given movie.
        // Find the 5 cheapest shops w/ an unrented copy of the movie
        // Sort them by price in ascending order
        // If two shops have the same price, pick the shop with the smaller id
        vector<int> results;

        auto iterator = available.find(movie);
        // See if we have matches
        if (iterator != available.end()) {
            const auto& s = iterator->second;
            int count = 0;
            // Then find the top 5 matches
            for (auto it = s.begin(); it != s.end() && count < 5; ++it) {
                results.push_back(it->second);  // push shop ID
                count++;
            }
        }

        return results;
    }
    
    void rent(int shop, int movie) {
        // Rents the given movie from the given shop.
        // Given: rent will only be called if the shop has an unrented copy of the movie
        
        // Just remove from available set and add to unavailable set

        auto price = prices[{shop, movie}];                        // look up the price
        available[movie].erase({price, shop});            // remove from available
        unavailable.insert(make_tuple(price, shop, movie));       // add to rented
    }
    
    void drop(int shop, int movie) {
        // Drops off a previously rented movie at the given shop.
        // Given:  will only be called if the shop had previously rented out the movie.

        auto price = prices[{shop, movie}];
        available[movie].insert({price, shop});
        unavailable.erase({price, shop, movie});
    }
    
    vector<vector<int>> report() {
        vector<vector<int>> res;
        int count = 0;
        for (const auto& t : unavailable) {       // unavailable is set<tuple<price,shop,movie>, Comparator>
            if (count == 5) break;
            res.push_back({get<1>(t), get<2>(t)}); // push {shop, movie}
            count++;
        }
        return res;
    }

};

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * MovieRentingSystem* obj = new MovieRentingSystem(n, entries);
 * vector<int> param_1 = obj->search(movie);
 * obj->rent(shop,movie);
 * obj->drop(shop,movie);
 * vector<vector<int>> param_4 = obj->report();
 */
