-- ox build script
set_xmakever("2.8.7")
set_project("ox")

set_description("The Ox Library Collection is a collection of C++ Libraries.")

for _, lib in ipairs(os.dirs("meta/libs/*"), path.basename) do
    option(lib)
        if has_config(lib) then
            includes(path.join(os.scriptdir(), lib, "xmake.lua")) -- load needed libs
        end
    option_end()
end
