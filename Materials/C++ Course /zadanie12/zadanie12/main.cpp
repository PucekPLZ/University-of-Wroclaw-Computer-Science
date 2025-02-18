#include <iostream>
#include <vector>
#include <list>
#include <set>
using namespace std;

struct SumFunctor {
    double sum = 0;
    size_t count = 0;

    template<typename T> void operator()(const T& value) {
        sum += value;
        ++count;
    }

    double get_sum() const {
        return sum;
    }

    size_t get_count() const {
        return count;
    }

    double get_average() const {
        return count > 0 ? sum / count : 0.0;
    }
};

int main() {
    
    SumFunctor sumFunctor;
    set<int> set_values = {1, 2, 3, 4, 5};
    for_each(set_values.begin(), set_values.end(), ref(sumFunctor));
    cout << "Sum: " << sumFunctor.get_sum() << " Count: " << sumFunctor.get_count() << " Average: " << sumFunctor.get_average() << endl;

    sumFunctor = SumFunctor();
    list<float> list_values = {1.1f, 2.2f, 3.3f, 4.4f, 5.5f};
    for_each(list_values.begin(), list_values.end(), ref(sumFunctor));
    cout << "Sum: " << sumFunctor.get_sum() << " Count: " << sumFunctor.get_count() << " Average: " << sumFunctor.get_average() << endl;
    
    sumFunctor = SumFunctor();
    vector<double> vector_values = {1.11, 2.22, 3.33, 4.44, 5.55};
    for_each(vector_values.begin(), vector_values.end(), ref(sumFunctor));
    cout << "Sum: " << sumFunctor.get_sum() << " Count: " << sumFunctor.get_count() << " Average: " << sumFunctor.get_average() << endl;

    return 0;
}
