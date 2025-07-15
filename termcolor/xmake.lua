set_xmakever("2.2.2")
set_project("termcolor")
set_version("0.1.0")

includes("@builtin/xpack")
add_includedirs("include")

add_rules("mode.debug", "mode.release")

target("termcolor")
    set_kind("headeronly")

    add_headerfiles("include/**")
    add_rules("utils.install.cmake_importfiles")
    add_rules("utils.install.pkgconfig_importfiles")
target_end()

option("enable-tests")
    set_default(false)
    target("test")
        set_kind("binary")

        add_files("tests/test.cpp")
    target_end()
option_end()

xpack("termcolor")
    set_description("A library that supports setting color flags to print colorful character")

    add_targets("termcolor")
xpack_end()
