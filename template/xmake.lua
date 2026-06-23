set_xmakever("2.2.2")
set_project("$NAME$")

-- include directories
add_includedirs("include")

set_languages("c++$CPP_STANDARD$")

-- compile_commands generation
add_rules("plugin.compile_commands.autoupdate", {outputdir = "build"})

-- targets
target("$NAME$")
    if $HEADERONLY_BOOLEAN$ then
        set_kind("headeronly")
    else
        if has_config("is-static") then
            set_kind("static")
        else
            set_kind("shared")
        end
    end
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
