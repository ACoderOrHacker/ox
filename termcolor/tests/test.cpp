#include <iostream>
#include <ox/termcolor/termcolor.hpp>
using namespace ox;

struct range_item {
    int begin;
    int end;
    const char *name;
};

const range_item ranges[5] = {
    {30, 37, "normal"},
    {40, 47, "bg"},
    {90, 97, "bright"},
    {100, 107, "bright bg"},
    {1, 9, "styles"}
};

template <class Color>
void print_group(const range_item &item, const char *group) {
    std::cout << "#group " << item.name << ": " << std::endl;
    for (int i = item.begin; i <= item.end; ++i) {
        std::cout << Color(i) << i << reset() << "\t";
        if (i % 3 == 0 && i != item.begin)
            std::cout << std::endl;
    }
    std::cout << std::endl;
}

void print_legacy() {
    for (int i = 0; i < 5; ++i)
        print_group<legacy16>(ranges[i], "legacy");
}

int main() {
    print_legacy();
    return 0;
}
