#cmake file for project association
#author: liuwenjun
#created:2014/02/20

CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

## 添加项目
if(PASSOA_COMPILER_MSVC)
ADD_EXECUTABLE(matrix_test
				${PROJECT_SOURCE_DIR}/test/matrix.cpp
				${PROJECT_SOURCE_DIR}/src/matrix.hpp
				)
target_link_libraries(matrix_test
				debug gtestd
				optimized gtest)

elseif(PASSOA_COMPILER_NDK)
endif()
