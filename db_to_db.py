# -*- coding: utf-8 -*-
# @Time     : 2022/7/16 10:00
# @File     : db_2_db.py
import json
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import pymysql as pymysql
from tkinter import END
from pymysql.cursors import DictCursor

# dev数据库
dev_connect = "xxxx"
dev_user = "xxxx"
dev_password = "xxxxxx"
dev_port = "xxxxx"
dev_db_name = "xxxxx"
dev_table = "xxxxx"

# 测试数据库
test_connect = "xxxxxx"
test_user = "xxxxx"
test_port = "xxxxx"
test_password = "xxxxxx"
test_table = "xxxxxxx"

# 创建一个窗口
window = tk.Tk()
window.title("数据库同步工具")
window.geometry('600x600')

# 将new_user_data变量初始化
new_user_data = None


def data_synchronization():
    # 定义一个全局变量new_user_data
    global new_user_data
    # 每次触发操作之前，清空多行文本框的内容
    text.delete("1.0", "end")
    # 定义两个变量name和phone，用来获取用户在文本框输入的内容
    update_time = entry1.get()
    # phone = entry2.get()
    # 连接dev数据库数据库
    conn_dev_sql = pymysql.connect(host=dev_connect, user=dev_user, cursorclass=DictCursor, password=dev_password, database=dev_db_name)
    curs_dev = conn_dev_sql.cursor()
    # 通过字典去读取不同的测试环境
    db_config = radio.get()
    config = {"0": "0", "test1环境": "test1", "test2环境": "test2", "test3环境": "test3"}
    test_db_name = config[db_config]
    try:
        if not entry1.get():
            tk.messagebox.showinfo(title="提示", message="更新时间为必填项！")
        if radio.get() == "0":
            tk.messagebox.showinfo(title="提示", message="请选择数据库")
        elif radio.get() == "test3环境":
            tk.messagebox.showinfo(title="提示", message="目前没有该测试数据库")
        else:
            # 连接测试数据库数据库"
            conn_test2_sql = pymysql.connect(host=test_connect, user=test_user, password=test_password, database=test_db_name)
            curs2 = conn_test2_sql.cursor()
            # 读取dev数据库的用户信息
            read_dev_sql = f'''select * from `{dev_db_name}`.`{dev_table}` where `update_time` = "{update_time}";'''
            # 读取测试数据库的用户信息
            read_test2_sql = f'''select * from `{test_db_name}`.`{test_table}` where `update_time` <> "{update_time}"; '''
            # 执行sql查询，查询dev数据库，将查询出来的结果保存在dev_user_data中
            curs_dev.execute(read_dev_sql)
            # dev_user_data = curs_dev.fetchone()
            dev_user_datas = curs_dev.fetchall()
            for dev_user_data in dev_user_datas:
                # 执行下面这句后data为{"content": "x", "created_time": "xxx"}，是str类型
                data = json.dumps(dev_user_data, default=str, ensure_ascii=False)
                # 把data转换为字典类型
                data_result = json.loads(data)
                print("转换为dict类型后的数据为：", '\n', data_result, '\n')
                # 把data再次转为json类型
                json_result = json.dumps(data_result)
                print("转换为json类型后的数据为：" + '\n' + json_result + '\n')
                # 获取返回字典data_result值的所有value的列表
                new_user_data = tuple(data_result.values())
                print(new_user_data)

                # 执行sql查询，查询测试数据库，将查询出来的结果保存在test_user_data中
                curs2.execute(read_test2_sql)
                test2_user_data = curs2.fetchone()
                # 提交数据至dev数据库
                conn_dev_sql.commit()
                # # 判断测试数据库是否有该用户
                # if test2_user_data:
                #     text.insert("insert", "测试数据库已存在该用户数据！" + '\n')
                # 如果dev数据库有该用户，测试数据库没有该用户，则执行同步操作
                if dev_user_data and (not test2_user_data):
                    try:
                        # 插入的SQL语句
                        insert_sql = f'''insert ignore into `{test_db_name}`.`{test_table}` VALUES {new_user_data}'''
                        # 执行SQL，向测试数据库中插入数据
                        curs2.execute(insert_sql)
                        print(insert_sql)
                        text.insert("insert", "数据同步成功！" + '\n')
                    except IOError:
                        text.insert("insert", "数据同步失败！" + '\n')
                conn_test2_sql.commit()
            curs_dev.close()
            curs2.close()
    except IOError:
        print("数据插入失败")
        conn_dev_sql.rollback()
        tkinter.filedialog.Directory()
    conn_dev_sql.close()


# 清空按钮函数：用来清空输入文本框中的内容
def clear():
    entry1.delete(0, END)  # 清空Entry文本框中的内容
    # entry2.delete(0, END)  # 清空Entry文本框中的内容
    text.delete("1.0", "end")  # 清空text多行文本框中的内容
    radio.set("0")  # 清空Radiobutton标签选项框


def selection():
    text.delete("1.0", "end")
    choose = str(radio.get())
    text.insert("insert", "您选择的是：" + choose + '\n')


# 创建一个标签
tk.Label(window, text="dev更新时间：").place(x=10, y=50)
tk.Label(window, text="dev创建时间：").place(x=10, y=120)
# 创建一个Entry文本框：用来输入一行文本字符串
entry1 = tk.Entry(window, bd=3, width=62, highlightcolor='red')
entry1.place(x=120, y=50)
entry2 = tk.Entry(window, bd=3, width=62, highlightcolor='green')
entry2.place(x=120, y=120)
# 创建一个可以输入多行文字的文本框
text = tk.Text(window, height=20, width=75, bg='white', highlightcolor='blue', highlightthickness=1)
text.place(x=35, y=240)
# 创建两个按钮：选择文件夹、退出窗口
tk.Button(window, text='开始同步', bg='grey', fg='white', command=data_synchronization).place(x=130, y=520)
tk.Button(window, text='清空', bg='grey', fg='white', command=clear).place(x=290, y=520)
tk.Button(window, text='退出', bg='grey', fg='white', command=window.quit).place(x=430, y=520)

radio = tk.StringVar()
radio.set("0")
tk.Label(window, text='请选择数据库：', bg='green', fg='white', width=12).place(x=10, y=180)
# 创建3个radiobutton选项
radio1 = tk.Radiobutton(window, text='test1环境', variable=radio, command=selection, value="test1环境")
radio1.place(x=140, y=180)
radio2 = tk.Radiobutton(window, text='test2环境', variable=radio, command=selection, value="test2环境")
radio2.place(x=290, y=180)
radio3 = tk.Radiobutton(window, text='test3环境', variable=radio, command=selection, value="test3环境")
radio3.place(x=440, y=180)

# 主循环
window.mainloop()
