# Genrate a subproject template for the ox project

import os
import sys
import shutil
import argparse

# Create ArgParser
parser = argparse.ArgumentParser()
parser.add_argument("project", help = "Your project name")
parser.add_argument("-p", "--path", help = "Your subproject's path", default = str(os.getcwd()))
parser.add_argument("-d", "--desc", help = "Add description for it", default = "")
parser.add_argument("-v", "--version", help = "Add version for it", default = "0.1.0")
parser.add_argument("-s", "--cppstd", help = "Set your c++ standard", default = "03")

if __name__ == "__main__":
    args = parser.parse_args()
    path = args.path
    project = args.project
    desc = args.desc
    ver = args.version
    std = args.cppstd

    os.makedirs(path, exist_ok = True)
    os.makedirs(os.path.join(path, "tests"), exist_ok = True)
    os.makedirs(os.path.join(path, "include", "ox", project), exist_ok = True)
    os.makedirs(os.path.join(path, "meta"), exist_ok = True)
    
    xmake_lua = open(os.path.join(path, "xmake.lua"), "w")
    xmake_lua.write(f"""set_xmakever("2.2.2")
set_project("{project}")
set_version("{ver}")
set_languages("c++{std}")


includes("@builtin/xpack")
add_includedirs("include")

add_rules("mode.debug", "mode.release")

target("{project}")
--[[ A header only example
    set_kind("headeronly")

    add_headerfiles("include/**")
    add_rules("utils.install.cmake_importfiles")
    add_rules("utils.install.pkgconfig_importfiles")
--]]
target_end()

option("enable-tests")
    set_default(false)
    target("test")
        set_kind("binary")

        add_files("tests/test.cpp")
    target_end()
option_end()

xpack("{project}")
    set_description("{desc}")

    add_targets("{project}")
xpack_end()
""")
    xmake_lua.close()

    libraries_json = open(os.path.join(path, "meta", "libraries.json"), "w")
    libraries_json.write(f"""{{
    "libraries": [
        {{
            "name": "{project}",
            "description": "{desc}",
            "version": "0.1.0",
            "cpp_standard": "{std}"
        }}
    ]
}}
""")
    libraries_json.close()

    test_cpp = open(os.path.join(path, "tests", "test.cpp"), "w")
    test_cpp.write("""
int main() {
    return 0;
}
""")
    test_cpp.close()

    # root library entry
    project_root_file = open(os.path.join(path, "include", "ox", project + ".hpp"), "w")
    project_root_file.close()
    
