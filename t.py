# -*- coding: utf-8 -*-
from ctypes import *

# -*- coding: utf-8 -*-
from ctypes import *

# 学生信息如下
stu_info = [("class", "A"),
            ("grade", 90),
            ("array", [1, 2, 3]),
            ("point", 4)]

# 创建结构提类
class Student(Structure):
    _fields_ = [("class", c_char),
            ("grade", c_int),
            ("array", c_long * 3),
            ("point", POINTER(c_int))]

print("sizeof Student: ", sizeof(Student))

# 实例化
long_array = c_long * 3
long_array_obj = long_array(1, 2, 3)
int_p = pointer(c_int(4))
stu_info_value = [c_char(b"A"), c_int(90), long_array_obj, int_p]

stu_obj = Student(*stu_info_value)
# 这样打印报错，因为字段名和python关键字class重名了，这是需要特别注意的点
# print("stu info:", stu_obj.class, stu_obj.grade, stu_obj.array[0], stu_obj.point[0])
print("stu info:", stu_obj.grade, stu_obj.array[0], stu_obj.point[0])



# 结构体指针数组
# 创建结构体数组类型
stu_array = Student * 2
# # 用Student类的对象实例化结构体数组
stu_array_obj = stu_array(stu_obj, stu_obj)
# 创建结构体指针数组
stu_p_array = POINTER(Student) * 2
# 使用pointer()初始化
stu_p_array_obj = stu_p_array(pointer(stu_obj), pointer(stu_obj))
# 曾接结构体指针成员,注意使用类型初始化指针是POINTER()
class NestStudent(Structure):
    _fields_ = [("rank", c_char),
                ("nest_stu", Student),
                ("strct_array", Student * 2),
                ("strct_point", POINTER(Student)),
                ("strct_point_array", POINTER(Student) * 2)]

# 实例化,对Student的对象包装为指针使用pointer()
nest_stu_info_list = [c_char(b"M"), stu_obj, stu_array_obj, pointer(stu_obj), stu_p_array_obj]
nest_stu_obj = NestStudent(*nest_stu_info_list)

# # 数组第二索引为结构体指针
# print(nest_stu_obj.strct_point_array[1])
# # 指针指向Student的对象
# print(nest_stu_obj.strct_point_array[1].contents)
# # Student对象的grade字段
# print(nest_stu_obj.strct_point_array[1].contents.grade)


# 实例化动态链接库的载入对象
so_obj = cdll.LoadLibrary("./libstruct.so.0")

# 准备入参
char_arg = c_char(b"Z")
int_arg = c_int(13)
float_arg = c_float(3.14159)

# 准备出参
out_buf = create_string_buffer(b"", sizeof(Student))

# 注意C语言源码中入参要求是指针，所以这里需要再次使用pointer()
# rest = so_obj.test_func(char_arg, int_arg, float_arg, pointer(stu_obj), pointer(nest_stu_obj), out_buf)
# 或者使用ctypes.bryef()方法自动转换，更快一点
rest = so_obj.test_func(char_arg, int_arg, float_arg, byref(stu_obj), byref(nest_stu_obj), out_buf)

# 打印函数返回值
print("func rest: ", rest)
# 打印出参
print("out buf: ", out_buf[0:sizeof(c_int) * 2])