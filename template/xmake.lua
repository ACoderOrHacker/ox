set_xmakever("2.2.2")
set_project("$NAME$")
set_version("$VERSION$")

-- include directories
add_includedirs("include")

-- targets
target("$NAME$")
    set_kind("headeronly")
    add_headerfiles("include/(**.hpp)")
    add_rules("utils.install.cmake_importfiles")
    add_rules("utils.install.pkgconfig_importfiles")
target_end()

option("enable-tests")
    set_default(false)
    target("test-cpp")
        set_kind("binary")

        add_files("tests/test.cpp")
    target_end()

    target("test-d")
        set_kind("binary")

        add_files("tests/test.d")
    target_end()
option_end()
