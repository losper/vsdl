#include "../src/matrix.hpp"
#include <gtest/gtest.h>

TEST(matrix, Demo)
{
	vsdl::matrix<int, 2, 2> tmp;
	EXPECT_EQ(1, tmp.at(1,1));
}

int main(int argc,char** argv) {
	testing::InitGoogleTest(&argc,argv);
	RUN_ALL_TESTS();
	return 0;
}