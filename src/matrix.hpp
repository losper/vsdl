#include <stdint.h>

namespace vsdl {
	template<typename T, uint32_t row,uint32_t col>
	class matrix {
	public:
		T at(uint32_t row, uint32_t col){
			return value[row][col];
		}
	private:
		T value[row][col];
	};
}
