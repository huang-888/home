import streamlit as st
from PIL import Image,ImageFilter
import base64
import time

#背景
def bar_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        [data-testid='stSidebar'] > div:first-child {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )
bar_bg("背景.jpg")


page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '图片处理工具', '音乐分享','网站整理',"智能词典","猜谜语",'我的留言区'])

def page_1():
    '我的兴趣推荐'
    #音乐
    with open("青藤色仲夏.mp3","rb") as m:
        music1=m.read()
    st.audio(music1,format="audio/mp3",start_time=0)
    #图文
    st.image("图片.jpg")
    st.title(':sparkles:_兴趣推荐_:sparkles:')
    #如果按钮被点击
    if st.button("展开"):
    # 进度条
        roading = st.progress(0, '开始加载')
        for i in range(1, 101, 1):
            time.sleep(0.02)
            roading.progress(i, '正在加载'+str(i)+'%')
        roading.progress(100, '加载完毕！')
        a = ':rainbow[---------------------------------------------------------------------★---------------------------------------------------------------------]'
        st.write("  ")
        st.write("  ")
        st.write("  ")
        st.write("书籍推荐")
        st.write(a)
        st.write("  ")
        st.write("电影推荐")
        st.write(a)
        st.write("  ")
        st.write("纪录片推荐")
        st.write(a)

def page_2():
    #复选栏
    tab1,tab2,tab3,tab4,tab5,tab6,tab7=st.tabs(["原图","旋转图片","转成黑白图像","图片缩放","模糊滤镜","浮雕滤镜","轮廓滤镜"])
    st.write(':star:图片处理工具:star:')
    file = st.file_uploader("上传图片",type=["png","jpg","jpeg"])
    #图片上传
    if file:
        file_name = file.name
        file_size = file.size
        file_type = file.type
        img = Image.open(file)
        #复选栏
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_rotate(img))
        with tab3:
            st.image(img_black(img))
        with tab4:
            st.image(img_resize(img))
        with tab5:
            st.image(img_blur(img))
        with tab6:
            st.image(img_emboss(img))
        with tab7:
            st.image(img_contour(img))

#图片处理
def img_rotate(img):
    angle = st.number_input("请输入旋转角度",value=90)
    if angle !=" ":
        angle=int(angle)
        img_change1 = img.rotate(angle)
        return img_change1

def img_resize(img):
    big= st.number_input("请输入图片尺寸",value=200)
    if big !=" ":
        big=int(big)
        img_change2 = img.resize((big,big))
        return img_change2

def img_black(img):
    img_change3= img.convert("L")
    return img_change3

def img_blur(img):
    img_change4=img.filter(ImageFilter.BLUR)
    return img_change4

def img_emboss(img):
    img_change5=img.filter(ImageFilter.EMBOSS)
    return img_change5

def img_contour(img):
    img_change6=img.filter(ImageFilter.CONTOUR)
    return img_change6

def page_3():
    '音乐分享'
    st.title(':musical_note:音乐分享:musical_note:')   
    st.write(" ")
    #1
    st.write("1. 海の見える街（临海小镇）")
    with open("海の見える街（临海小镇）.mp3","rb") as a:
        music_a=a.read()
    st.audio(music_a,format="audio/mp3",start_time=0)
    st.write(" ")
    #2
    st.write("2. fish in the pool")
    with open("fish in the pool.mp3","rb") as b:
        music_b=b.read()
    st.audio(music_b,format="audio/mp3",start_time=0)
    st.write(" ")
    #3
    st.write("3. 春を知らせるもの~続 夏目友人帳のテーマ（春之信使）")
    with open("春を知らせるもの~続 夏目友人帳のテーマ（春之信使）.mp3","rb") as c:
        music_c=c.read()
    st.audio(music_c,format="audio/mp3",start_time=0)
    st.write(" ")
    #4
    st.write("4. ふるさとの匂い（故乡的味道）")
    with open("ふるさとの匂い（故乡的味道）.mp3","rb") as d:
        music_d=d.read()
    st.audio(music_d,format="audio/mp3",start_time=0)
    st.write(" ")
    #5
    st.write("5. 那个夏天")
    with open("那个夏天.mp3","rb") as e:
        music_e=e.read()
    st.audio(music_e,format="audio/mp3",start_time=0)

def page_4():
    '网站整理'
    st.write('----')
    go = st.selectbox('选择想要查看的网页', ['百度', 'bilibili',"streamlit","github","numpy","matplotlib","pandas"])
    if go == "百度":
        st.link_button('跳转到'+go,"https://www.baidu.com/")
    elif go == "bilibili":
        st.link_button('跳转到'+go,"https://www.bilibili.com/")
    elif go=="streamlit":
        st.link_button("跳转到"+go ,"https://streamlit.io/")
    elif go=="github":
        st.link_button("跳转到"+go ,"https://github.com/")
    elif go=="numpy":
        st.link_button("跳转到"+go ,"https://numpy.org/")
    elif go=="matplotlib":
        st.link_button("跳转到"+go ,"https://matplotlib.org/")
    elif go=="pandas":
        st.link_button("跳转到"+go ,"https://pandas.pydata.org/")

def page_5():
    '智能词典'
    st.write("智能词典")
    #读取词典信息
    with open("words_space.txt","r",encoding="utf-8")as f:
        words_list=f.read().split("\n")
    #分割内容
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split("#")
    #导入字典
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    #读取查询次数
    with open("check_out_times.txt","r",encoding="utf-8")as g:
        times_list=g.read().split("\n")
    #列表转为字典
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split("#")
    times_dict={}
    for i in times_list:
        times_dict[i[0]]=int(i[1])
    
    #输入框
    word=st.text_input("请输入查询的单词(例：abandon)")
    if word in words_dict:
        st.write(words_dict[word])
        n=words_dict[word][0]
        if n in times_dict:
            times_dict[n]+=1
        else:
            times_dict[n]=1
        with open("check_out_times.txt","w",encoding="utf-8")as h:
            message=" "
            for k, v in times_dict.items():
                message+=str(k)+"#"+str(v)+"\n"
            message=message[:-1]
            h.write(message)
        st.write("查询次数：",times_dict[n])
        #彩蛋
        if word=="snow"or word=="snowman"or word=="snowy":
            st.snow()
        if word=="balloon":
            st.balloons() 

def page_6():
    '猜谜语'
    st.title("猜谜语")
    miyu= ":blue[恭喜你，回答正确！]"
    miyuu= ":blue[不对哦，再想一想]"
    st.write("谜面:丰收")
    level = st.radio('选择答案：',['移', '禾', '秧',"秸"])
    if st.button("确认答案"):
        if level=="移":
            st.write(miyu)
        else:
            st.write(miyuu)
    st.write(" ")
    st.write(" ")
    st.write("谜面:痴")
    level = st.radio('选择答案：',['疗', '化', '保',"仲"])
    if st.button("确认答案 "):
        if level=="保":
            st.write(miyu)
        else:
            st.write(miyuu)
    st.write(" ")
    st.write(" ")
    st.write("谜面:圆周")
    level = st.radio('选择答案：',['圈', '口', '弧',"图"])
    if st.button(" 确认答案"):
        if level=="口":
            st.write(miyu)
        else:
            st.write(miyuu)
    st.write(" ")
    st.write(" ")
    st.write("谜面:九十九")
    level = st.radio('选择答案：',['一', '白', '口',"日"])
    if st.button(" 确认答案 "):
        if level=="白":
            st.write(miyu)
        else:
            st.write(miyuu)
    st.write(" ")
    st.write(" ")
    st.write("谜面:座中无人")
    level = st.radio('选择答案：',['空', '广', '坐',"庄"])
    if st.button("  确认答案 "):
        if level=="庄":
            st.write(miyu)
        else:
            st.write(miyuu)
    st.write(" ")
    st.write(" ")
    st.write("谜面:傍晚")
    level = st.radio('选择答案：',['夕', '映', '晒',"昏"])
    if st.button("  确认答案  "):
        if level=="晒":
            st.write(miyu)
        else:
            st.write(miyuu)
    st.write(" ")
    st.write(" ")
    st.write("谜面:头重脚轻")
    level = st.radio('选择答案：',['高', '胼', '炭',"鸿"])
    if st.button("  确认答案   "):
        if level=="炭":
            st.write(miyu)
        else:
            st.write(miyuu)
    st.write(" ")
    st.write(" ")
    st.write("谜面:林海无边")
    level = st.radio('选择答案：',['梅', '沐', '波',"林"])
    if st.button("  确认答案    "):
        if level=="梅":
            st.write(miyu)
        else:
            st.write(miyuu)
    st.write(" ")
    st.write(" ")
    st.write("谜面:少小离家老大回")
    level = st.radio('选择答案：',['思', '尖', '夭',"易"])
    if st.button("   确认答案    "):
        if level=="夭":
            st.write(miyu)
        else:
            st.write(miyuu)

def page_7():
    '我的留言区'
    st.write("我的留言区")
    #加载内容
    with open("leave_messages.txt","r",encoding="utf-8")as n:
        messages_list=n.read().split("\n")
    for i in range(len(messages_list)):
        messages_list[i]=messages_list[i].split("#")
    for i in messages_list:
        if i[1]=="阿短":
            with st.chat_message("🎲"):
                st.write(i[1],":",i[2])
        elif i[1]=="编程猫":
            with st.chat_message("🎀"):
                st.write(i[1],":",i[2])
        elif i[1]=="学生":
            with st.chat_message("🎓"):
                st.write(i[1],":",i[2])
        elif i[1]=="老师":
            with st.chat_message("✏️"):
                st.write(i[1],":",i[2])
    name=st.selectbox("我是......",["阿短","编程猫","学生","老师"])
    new_message=st.text_input("想要说的话......")
    if st.button("留言"):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open("leave_messages.txt","w",encoding="utf-8")as t:
            message=""
            for i in messages_list:
                message+=i[0]+"#"+i[1]+"#"+i[2]+"\n"
            message=message[:-1]
            t.write(message)

if (page == '我的兴趣推荐'):
    page_1()
elif (page == '图片处理工具') :
    page_2()
elif (page == '音乐分享') :
    page_3()
elif (page == '网站整理') :
    page_4()
elif (page == '智能词典') :
    page_5()
elif (page == '猜谜语') :
    page_6()
elif (page == '我的留言区') :
    page_7()
else :
    pass
