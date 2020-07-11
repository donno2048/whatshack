import os;from selenium import webdriver;import chromedriver_autoinstaller;from qrcode import make;chromedriver_autoinstaller.install();op = webdriver.ChromeOptions();op.add_experimental_option('excludeSwitches', ['enable-logging']);brow = webdriver.Chrome(options=op);brow.get('https://web.whatsapp.com/');j = None;logic = True;from flask import Flask,render_template
while logic:
    try:
        while j is None:j = brow.find_element_by_xpath("//div[@class=\"_1QMFu\"]").get_attribute("data-ref");logic = False
    except:logic = True
i = make(j);os.remove(os.path.join(os.path.join('static', 'pics'), 'im.png'));i.save(os.path.join(os.path.join('static', 'pics'), 'im.png'), format='PNG');app = Flask(__name__)
@app.route('/')
def index():return render_template('index5.html',user_image=os.path.join(os.path.join('static','pics'),'im.png'),what=os.path.join(os.path.join('static','pics'),'what.png'))
if __name__=='__main__':app.run(debug=True)
