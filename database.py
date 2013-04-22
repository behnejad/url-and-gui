'''
Created on Apr 22, 2013

@author: Maryachi
'''
'''
Created on Apr 22, 2013

@author: meraj
'''
import sqlite3


class RssDatabase:
    def __init__ (self, conn = sqlite3.connect('rss.db'), c = sqlite3.connect('rss.db').cursor()):
        
        self.conn = sqlite3.connect('rss.db')
        self.c = conn.cursor()
    
        self.c.execute('''CREATE TABLE IF NOT EXISTS rss
                 (date text, title text, link text, describtion text)''')
        
#        temp_conn = sqlite3.connect('dual.db')
#        temp_c = temp_conn.cursor()
#        temp_c.execute('''CREATE TABLE IF NOT EXISTS dual
#                 (date text, title text, link text, describtion text)''')
#        
#        temp_conn.commit()
        self.conn.commit()
        
        #temp_conn.close()
    
    def insertdata(self,data_list):
#        temp_conn = sqlite3.connect('dual.db')
#        temp_c = temp_conn.cursor()
        self.c.executemany('INSERT INTO rss  VALUES (?,?,?,?)', data_list)
#        self.c.executemany('''INSERT INTO rss
#                        (date, title, link, describtion)
#                        SELECT date, title, link, describtion
#                        FROM dual
#                        WHERE not exists (select * from rss
#                        where rss.title = ?)''', data_list)
        
        #temp_conn.commit()
        self.conn.commit()
    
    def showbydate(self,date):
        print date
        t = (date,)
        print t
        final =''
        for row in self.c.execute('SELECT * FROM rss WHERE date = ?',t):
            for data in row:
                final += "\n"
                final += data
                final += "\n"
            final += "################################################"
            final += "\n"
            
#            for i in range(len(row)):
#            final += "####################### rss no:" + str(i+1) + "#############################\n"
#            final += "date:\n"
#            final += data[i][0]
#            final += "\ntitle:\n"
#            final += data[i][1]
#            final += "\nlink:\n"
#            final += data[i][2]
#            final += "\ndescription:\n"
#            final += data[i][3]
#            final += "#############################################################\n"
        return final
    def closdb(self):
        self.conn.close()
        
