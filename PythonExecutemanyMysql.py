# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: PythonExecutemany.py

import pymysql

# 数据库连接信息
host = ''
username = ''
password = ''
db = ''
connect = pymysql.connect(host=host, user=username, password=password, database=db, charset="utf-8")
cursors = connect.cursor()

xing_lists = ['pan', 'lang', 'jiang', 'gong', 'gan', 'yu', 'hao', 'xia', 'que', 'tian', 'zhang', 'long', 'dou', 'guo',
              'wen', 'wei', 'ren', 'jiao', 'gu', 'sang', 'chen', 'xu', 'zhuo', 'bing', 'zhen', 'ding', 'ye', 'wo',
              'feng', 'wan', 'zhuang', 'zui', 'liang', 'heng', 'mei', 'huan', 'xue', 'dang', 'bu', 'yuan', 'liu',
              'chai', 'qin', 'liao', 'lin', 'xing', 'bei', 'dong', 'yun', 'wu', 'gui', 'fu', 'qiang', 'ling', 'huo',
              'jia', 'pei', 'lao', 'mo', 'qiu', 'ning', 'xian', 'shu', 'chang', 'zi', 'tu', 'you', 'ying', 'hong',
              'duan', 'zhai', 'han', 'sha', 'gou', 'tan', 'shui', 'kan', 'zhan', 'kuang', 'kui', 'sun', 'xun', 'hang',
              'tai', 'geng', 'leng', 'zu', 'lai', 'zai', 'peng', 'ben', 'ni', 'che', 'tang', 'ping', 'bao', 'mao',
              'shan', 'hu', 'zhi', 'kang', 'sheng', 'min', 'xiong', 'zou', 'cong', 'neng', 'zuo', 'mi', 'nie', 'ji',
              'kuai', 'shou', 'xie', 'ba', 'ju', 'ke', 'zan', 'fan', 'lan', 'xin', 'hou', 'mong', 'shuang', 'chong',
              'ru', 'su', 'yang', 'kou', 'ran', 'du', 'qian', 'zhao', 'yi', 'zhu', 'pu', 'bai', 'zong', 'miao', 'suo',
              'li', 'cheng', 'cen', 'song', 'di', 'tou', 'jing', 'pi', 'hua', 'yong', 'zhou', 'he', 'yin', 'chao', 'qi',
              'jian', 'teng', 'zheng', 'yan', 'qiao', 'kong', 'lu', 'deng', 'zhong', 'xuan', 'lou', 'pang', 'zang',
              'yao', 'shi', 'shen', 'fei', 'xi', 'quan', 'cao', 'zha', 'tong', 'meng', 'fang', 'wang', 'tao', 'ruan',
              'gao', 'chi', 'rong', 'lei', 'niu', 'shao', 'qu', 'bi', 'ge', 'luan', 'chu', 'jin', 'lian', 'ming',
              'shang', 'mu', 'bian', 'nong', 'xiao', 'guan', 'man', 'na', 'dai', 'diao', 'rao', 'ban', 'she', 'ma',
              'xiang', 'yue', 'huang', 'huai', 'cang', 'cui', 'cai', 'an', 'ou', 'ai', 'ao', 'e', 'weng']

ming_lists = ['ai', 'an', 'ang', 'ao', 'ba', 'bai', 'ban', 'bang', 'bao', 'be', 'bei', 'ben', 'beng', 'bi', 'bian',
              'biao', 'bie', 'bin', 'bing', 'bo', 'bu', 'ca', 'cai', 'can', 'cang', 'cao', 'ce', 'cen', 'ceng', 'cha',
              'chai', 'chan', 'chang', 'chao', 'che', 'chen', 'cheng', 'chi', 'chong', 'chou', 'chu', 'chuai', 'chuan',
              'chuang', 'chui', 'chun', 'chuo', 'ci', 'cong', 'cou', 'cu', 'cuan', 'cui', 'cun', 'cuo', 'da', 'dai',
              'dan', 'dang', 'dao', 'de', 'deng', 'di', 'dian', 'diao', 'die', 'ding', 'diu', 'dong', 'dou', 'du',
              'duan', 'dui', 'dun', 'duo', 'e', 'en', 'er', 'fa', 'fan', 'fang', 'fei', 'fen', 'feng', 'fou', 'fu',
              'zhuang', 'ga', 'gai', 'gan', 'gang', 'gao', 'ge', 'gei', 'gen', 'geng', 'gong', 'gou', 'gu', 'gua',
              'guai', 'guan', 'guang', 'gui', 'gun', 'guo', 'ha', 'hai', 'han', 'hang', 'hao', 'he', 'hei', 'hen',
              'heng', 'hong', 'hou', 'hu', 'hua', 'huai', 'huan', 'huang', 'hui', 'hun',
              'huo', 'ji', 'jia', 'jian', 'jiang', 'jiao', 'jie', 'jin', 'jing', 'jiong', 'jiu', 'jou', 'ju', 'juan',
              'jue', 'jun', 'ka', 'kai', 'kan', 'kang', 'kao', 'ke', 'ken', 'keng', 'kong', 'kou', 'ku', 'kua', 'kuai',
              'kuan', 'kuang', 'kui', 'kun', 'kuo', 'la', 'lai', 'lan', 'lang', 'lao', 'le', 'lei', 'leng', 'li',
              'lian', 'liang', 'liao', 'lie', 'lin', 'ling', 'liu', 'long', 'lou', 'lu', 'luan', 'lue', 'lun', 'luo',
              'ma', 'mai', 'man', 'mang', 'mao', 'me', 'mei', 'men', 'meng', 'mi', 'mian', 'miao', 'mie', 'min', 'ming',
              'miu', 'mo', 'mou', 'mu', 'na', 'nai', 'nan', 'nang', 'nao', 'nei', 'nen', 'neng', 'ni', 'nian', 'niang',
              'niao', 'nie', 'nin', 'ning', 'niu', 'nong', 'nou', 'nu', 'nuan', 'nue', 'nun', 'nuo', 'ou', 'pa', 'pai',
              'pan', 'pang', 'pao', 'pei', 'pen', 'peng', 'pi', 'pian', 'piao', 'pie', 'pin', 'ping', 'po', 'pou', 'pu',
              'qi', 'qia', 'qian', 'qiang', 'qiao', 'qie', 'qin', 'qing', 'qiong', 'qiu', 'qu', 'quan', 'que', 'qun',
              'ran', 'rang', 'rao', 're', 'ren', 'reng', 'ri', 'rong', 'rou', 'ru', 'ruan', 'rui', 'run', 'ruo', 'sa',
              'sai', 'san', 'sang', 'sao', 'se', 'sei', 'sen', 'seng', 'sha', 'shai', 'shan', 'shang', 'shao', 'she',
              'shen', 'sheng', 'shi', 'shou', 'shu', 'shua', 'shuai', 'shuan', 'shuang', 'shui', 'shun', 'shuo', 'si',
              'song', 'sou', 'su', 'suan', 'sui', 'sun', 'suo', 'ta', 'tai', 'tan', 'tang', 'tao', 'te', 'teng', 'ti',
              'tian', 'tiao', 'tie', 'ting', 'tong', 'tou', 'tu', 'tuan', 'tui', 'tun', 'tuo', 'wa', 'wai', 'wan',
              'wang', 'wei', 'wen', 'weng', 'wo', 'wu', 'xi', 'xia', 'xian', 'xiang', 'xiao', 'xie', 'xin', 'xing',
              'xiong', 'xiu', 'xu', 'xuan', 'xue', 'xun', 'ya', 'yan', 'yang', 'yao', 'ye', 'yi', 'yin', 'ying', 'yong',
              'you', 'yu', 'yuan', 'yue', 'yun', 'za', 'zai', 'zan', 'zang', 'zao', 'ze', 'zei', 'zen', 'zeng', 'zha',
              'zhai', 'zhan', 'zhang', 'zhao', 'zhe', 'zhen', 'zheng', 'zhi', 'zhong', 'zhou', 'zhu', 'zhua', 'zhuai',
              'zhuan', 'zhui', 'zhun', 'zhuo', 'zi', 'zong', 'zou', 'zu', 'zuan', 'zui', 'zun', 'zuo', 'nv', 'nve',
              'lia', 'lv']
              
def executemany_sql():
    sqls = f'insert ignore into table_name (username) values (%s)'
    usersvalues = []
    for xing_list in xing_lists:
        for ming_list1 in ming_lists:
            for ming_list2 in ming_lists:
                emails = xing_list + ming_list1 + ming_list2 + '@163.com'
                usersvalues.append((emails))
                if len(usersvalues) == 1000:
                    cursor = connect.cursor()
                    ursor.executemany(sqls, usersvalues)
                    connect.commit()
                    usersvalues = []

    cursor = connect.cursor()
    cursor.executemany(write_sql, usersvalues)
    connect.commit()


if __name__ == '__main__':
    executemany_sql()
    connect.close()
