module;

#define OX_$UPPER_NAME$_USE_MODULES
#include <ox/$NAME$.hpp>

export module $NAME$;

export namespace ox {
using namespace ox::impl::$NAME$;
}
