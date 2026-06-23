-- ox build script
set_xmakever("2.8.7")
set_project("ox")

set_description("The Ox Library Collection is a collection of C++ Libraries.")

for _, lib in ipairs(os.dirs("*"), path.basename) do
    if not lib:startswith(".") and lib ~= "res" and lib ~= "meta" and lib ~= "scripts" and lib ~= "template" then
        option(lib)
            if has_config(lib) then
                includes(path.join(os.scriptdir(), lib, "xmake.lua")) -- load needed libs
            end
        option_end()
    end
end
