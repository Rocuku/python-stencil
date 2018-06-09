# Game of life

## 命令行运行
```
python web/web/run.py
```

可选参数
```
--file_path=test_case/test_case_1
--height=9
--weight=9
--time_slot=1
```
height 与 weight 参数用于生成随机初始棋盘，设置file_path 的情况下，height 与 weight 设置无效，输入为 file_path 内保存的棋盘文件。

time_slot 为迭代速度，单位为秒。


## 网页显示
```
python manage.py runserver
```

浏览器转到 [127.0.0.1:8000](127.0.0.1:8000) 进行查看
