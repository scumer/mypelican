Title: Python any all函数用法
Date: 2016-07-31
Category: Python
Tags: python
Slug: python-any-all

python `any` `all` 函数用法

any()  
Return True if bool(x) is True for any x in the iterable.
If the iterable is empty, return False.  
当传入空可迭代对象时返回False，当可迭代对象中有任意一个不为False，则返回True


all()  
Return True if bool(x) is True for all values x in the iterable.
If the iterable is empty, return True.  
当传入空可迭代对象时返回True，当可迭代对象中有任意一个不为True，则返回False  

 
简单用法  
判断list中是否含有False或True值

	:::bash
	any([1,2,0])  => True
	any([0,''])   => False

	all([1,2,0])  => False
	all([1,2])    => True

判断字符串中是否包含指定list中的字符串

	:::bash
	any(x in 'ipad' for x in ['iphone', 'ipad'])  => True

list all in sepcified string
	
	:::bash
	all(x in 'ipadabciphone' for x in ['iphone', 'ipad'])  => True