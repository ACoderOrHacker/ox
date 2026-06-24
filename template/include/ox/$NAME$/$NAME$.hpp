#pragma once

namespace ox {
namespace impl {
namespace $NAME$ {} // namespace $NAME$
} // namespace impl
} // namespace ox

#ifndef OX_$UPPER_NAME$_USE_MODULES
namespace ox {
using namespace impl::$NAME$;
}
#endif
