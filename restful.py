#導入Flask類別物件,此類別的實例就是WSGI應用
from flask import Flask, request


'''
實例化1個Flask物件,並傳入__name__參數(__name__是當前模組名稱)
讓 Flask 知道在哪裡尋找資源。
'''

app=Flask(__name__)

#這邊試著把app給印出,會發現是當前的檔名(<Flask 'hello'>)
print(__name__)

#使用 route（） 裝飾器告訴 Flask 哪個 URL 應該觸發我們的函式。
# 斜線代表網站的根目錄,可以疊加
@app.route("/")
def hello():
    return "<h1>Hello, This is a restful api server by Flask !</h1>"

#這段是使用Get的方式連線且傳遞name參數時的路由設定(如果用POST方式連線的話會出現Method Not Allowed的錯誤訊息)
@app.route("/data/<name>",methods=['GET'])
def queryDataMessageByName(name):
    print('type(name)',type(name))
    return '您使用的連線方式是{0}, 且傳入的參數是{1}'.format(request.method,name)


'''
下面這段路由設定不論是GET或POST都可以對應
POST會印出連線方式和參數內容
Get的話跑出寫好的HTML表單,可以自行填寫並提交要傳遞的內容
'''

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return '您使用的連線方式是{0}, 且傳入的參數是{1}'.format(request.method,request.values['content'])
    
   
    return "<form method='post' action='/login'>" \
    "輸入要傳送的內容: " \
    "<input type='text' name='content' id='content' />" \
    "</br>" \
    "<button type='submit'>Submit</button>" \
    "</form>"
    



#是想表示 main() 只有在當前腳本被直接執行時才執行，不希望被導入其它模組時執行。
#app.run()執行網頁伺服器的啟動動作
if __name__ == '__main__':
    app.run(debug=True)

