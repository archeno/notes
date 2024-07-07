MySql BasicSetup
================

install mysql server
--------------------

从官网 `mysql download <https://dev.mysql.com/downloads/mysql/>`_ 下载最新长期支持版本,建议msi installer

连接mysql 服务器
----------------

连接之前确保mysql服务器已经启动
输入以下命令连接服务器::
	
	mysql -u username -p [databaseName]

如果忘记登陆密码，执行以下步骤重置密码

#. 关闭服务器
#. 创建重置密码文件mysql-init.txt,内容如下::

	ALTER USER 'root'@'localhost' IDENTIFIED BY 'MyNewPass';

#. 以管理员身份运行cmd, 执行以下语句::

	C:\\> mysqld
         --defaults-file="C:\\ProgramData\\MySQL\\MySQL Server 8.4\\my.ini"
         --init-file=C:\\mysql-init.txt

.. note:: 
	
	可以将mysql 安装目录加入到系统环境变量中方便执行