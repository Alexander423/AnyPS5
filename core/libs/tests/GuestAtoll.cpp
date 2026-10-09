#include "SceTypes.hpp"
#include <cstdlib>
#include <limits>

extern "C" long long APS5_VABI atoll_nid_postfix(const char* string);

int main() {
    static_assert(sizeof(long long) == 8);
    struct Case { const char* input; long long expected; };
    const Case cases[] = {
        {"0", 0}, {"", 0}, {"not-a-number", 0}, {"+", 0}, {"-", 0},
        {" \t\n\r\v\f-42tail", -42}, {"+2147483648", 2147483648LL},
        {"-2147483649", -2147483649LL}, {"000019", 19}, {"0x10", 0},
        {"9223372036854775807", std::numeric_limits<long long>::max()},
        {"-9223372036854775808", std::numeric_limits<long long>::min()}
    };
    for (const auto& entry : cases) {
        if (atoll_nid_postfix(entry.input) != entry.expected)
            std::abort();
    }
}
