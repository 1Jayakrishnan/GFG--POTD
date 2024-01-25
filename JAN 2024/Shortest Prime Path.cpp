class Solution {
public:
    std::vector<bool> generate_primes() {
        const int max_limit = 10000;
        std::vector<bool> is_prime(max_limit, true);
        is_prime[0] = is_prime[1] = false;

        for (int i = 2; i * i < max_limit; ++i) {
            if (is_prime[i]) {
                for (int j = i * i; j < max_limit; j += i) {
                    is_prime[j] = false;
                }
            }
        }

        return is_prime;
    }

    std::vector<int> get_adjacent_primes(int current, const std::vector<bool>& is_prime) {
        std::vector<int> primes;
        std::vector<int> digits;
        while (current > 0) {
            digits.push_back(current % 10);
            current /= 10;
        }
        std::reverse(digits.begin(), digits.end());

        for (int i = 0; i < 4; ++i) {
            int original_digit = digits[i];
            for (int j = 0; j < 10; ++j) {
                if (j != original_digit) {
                    digits[i] = j;
                    int new_num = 0;
                    for (int digit : digits) {
                        new_num = new_num * 10 + digit;
                    }
                    if (is_prime[new_num]) {
                        primes.push_back(new_num);
                    }
                }
            }
            digits[i] = original_digit;
        }

        return primes;
    }

    int solve(int num1, int num2) {
        if (num1 == num2) {
            return 0;
        }

        std::vector<bool> is_prime = generate_primes();

        std::unordered_set<int> visited;
        std::queue<std::pair<int, int>> bfs_queue;
        bfs_queue.push({num1, 0});

        while (!bfs_queue.empty()) {
            int current = bfs_queue.front().first;
            int distance = bfs_queue.front().second;
            bfs_queue.pop();

            if (current == num2) {
                return distance;
            }

            if (visited.find(current) == visited.end()) {
                visited.insert(current);
                std::vector<int> adjacent_primes = get_adjacent_primes(current, is_prime);
                for (int neighbor : adjacent_primes) {
                    bfs_queue.push({neighbor, distance + 1});
                }
            }
        }

        return -1;  // If no path is found
    }
};
