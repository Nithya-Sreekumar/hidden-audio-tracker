from django.shortcuts import render,HttpResponseRedirect
import pymysql
#import pyaudio
import wave
import speech_recognition as spreg
import datetime
from django.core.files.storage import FileSystemStorage


db=pymysql.connect("localhost","root","","hat_image")
c=db.cursor()

# Create your views here.
def guest_home(request):
    return render(request,'guest/guest_home.html')
def guest_reg(request):
    data=""
    if request.POST:        
        name=request.POST.get("name")
        address=request.POST.get("address")
        email=request.POST.get("email")
        number=request.POST.get("number")
        gender=request.POST.get("gender")
        dob=request.POST.get("dob")
        uname=request.POST.get("uname")
        password=request.POST.get("password")
        cpass=request.POST.get("cpassword")
        request.session["uname"]=uname
        if(cpass==password):       
        
            utype="user"
            status="pending"
            c.execute("insert into userreg(name,address,email,number,gender,dob,username) values('"+ name +"','"+ address +"','"+ email +"','"+ number +"','"+ gender +"','"+ dob +"','"+ uname +"')")
            db.commit()
            c.execute("insert into login values('"+ uname +"','"+ password +"','"+ utype +"','"+ status +"')")
            db.commit()
            data="Successfully completed registartion"
            
        else:
            data="Password donot match"
    return render(request,'guest/guest_reg.html',{"msg":data})
def guest_login(request):
    data=""
  
    if request.POST:
        
        uname=request.POST.get("uname")
        passw=request.POST.get("password")
        c.execute("select * from login where username='"+ uname +"' and password='"+ passw +"'")
        log=c.fetchone()
        
        if log :
            request.session["uname"]=log[0]
            if log[2]=='user':           
                return HttpResponseRedirect('/uhome')
            # elif log[2]=='admin':           
            
            #     return HttpResponseRedirect('/ahome')
            else:            
                return HttpResponseRedirect('/login')
        else:
             return HttpResponseRedirect('/login')

    return render(request,'guest/guest_login.html',{"data":data})
def user_home(request):
    return render(request,'user/user_home.html')
def user_profile(request):
    name=request.session["uname"]
    c.execute("select * from userreg where username='"+ name +"'")
    udata=c.fetchall()
    if request.POST:
        for i in udata:
            id=i[0]
            request.session['id']=id
            return HttpResponseRedirect('/profileedit/')
    return render(request,'user/user_profile.html',{"udata":udata})
def profileedit(request):
    if request.session['id']:
        c.execute("select * from userreg where uid='"+ str(request.session['id']) +"'")
        udata=c.fetchall() 
        if request.POST:
            name=request.POST.get("name")
            address=request.POST.get("address")
            email=request.POST.get("email")
            number=request.POST.get("number")
            gender=request.POST.get("gender")
            dob=request.POST.get("dob")
            uname=request.POST.get("uname")
            c.execute("update userreg set name='"+ name +"',address='"+ address +"',email='"+ email +"',number='"+ number +"',gender='"+ gender +"',dob='"+ dob +"',username='"+ uname +"' where uid='" + str(request.session["id"]) + "'")
            db.commit()
            return HttpResponseRedirect('/uprofile/')
    return render(request,'user/profileedit.html',{"udata":udata})
def user_compose(request):
    if 'rec' in request.POST:
        #record and get audio
        print("hi")
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = 5
        WAVE_OUTPUT_FILENAME = "sample_audio.wav"

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()


        sound_file = 'sample_audio.wav'
        recog = spreg.Recognizer()
        with spreg.AudioFile(sound_file) as source:
            speech = recog.record(source) #use record instead of listning
            try:
                text = recog.recognize_google(speech)
                print('The file contains: ' + text)
            except spreg.UnknownValueError:
                print('Unable to recognize the audio')
            except spreg.RequestError as e: 
                print("Request error from Google Speech Recognition service; {}".format(e))

                                  



       
    if 'send' in request.POST:
        to=request.POST.get("to")
        com=request.POST.get("compose")
        fil=request.POST.get("file")
        pas=request.POST.get("pas") 
        #file=requset.Files.get("file")       
        c.execute("insert into compose(from,to,messages,file,pas) values('"+ request.session["uname"] +"',,'"+ to +"','"+ com +"','"+ fil +"','"+ pas +"')")
        db.commit()
    

    if 'draft' in request.POST:
        s=''

    return render(request,'user/user_compose.html')
def edit(request):
    if 'sent' in request.POST and request.FILES.get("file"):
        frommail=request.session["uname"]
        data=request.POST.get("msg")
        to=request.POST.get("to")
        sub=request.POST.get("sub")
        pasw=request.POST.get("pass")

        myfile=request.FILES.get("file")
        fs=FileSystemStorage()
        filename=fs.save(myfile.name , myfile)              
        uploaded_file_url = fs.url(filename)





        date=datetime.datetime.now()
        status="sent"
        c.execute("insert into messages(frommail,tomail,sub,msg,date,status,password,path) values('"+ frommail +"','"+ to +"','"+ sub +"','"+ data +"','"+ str(date) +"','"+ status +"','"+ pasw +"','"+ uploaded_file_url +"')")
        db.commit()
    if 'save' in request.POST and request.FILES.get("file"):
        frommail=request.session["uname"]
        data=request.POST.get("msg")
        to=request.POST.get("to")
        sub=request.POST.get("sub")
        pasw=request.POST.get("pass")
        date=datetime.datetime.now()

        myfile=request.FILES.get("file")
        fs=FileSystemStorage()
        filename=fs.save(myfile.name , myfile)              
        uploaded_file_url = fs.url(filename)


        status="save"
        c.execute("insert into messages(frommail,tomail,sub,msg,date,status,password,path) values('"+ frommail +"','"+ to +"','"+ sub +"','"+ data +"','"+ str(date) +"','"+ status +"','"+ pasw +"','"+ uploaded_file_url +"')")
        db.commit()      
    return render(request,'user/edit.html')
def user_inbox(request):
    sent='sent'
    name=request.session["uname"]
    c.execute("select * from messages where tomail='"+ request.session["uname"] +"' and status='"+ sent +"' order by date desc ")
    print("select * from messages where tomail='"+ request.session["uname"] +"' and status='"+ sent +"'  order by date desc ")
    co=c.fetchall()
    if request.GET:
            msgidd=request.GET.get("msgid")
            if msgidd:
                request.session["msgid"]=msgidd
                return HttpResponseRedirect("/inbox1/")
    return render(request,'user/user_inbox.html',{"udata":co})
def inbox1(request):
    co=""
    c.execute("select path from messages where id='"+ request.session["msgid"] +"'")
    path=c.fetchone()
    path=path[0]
    if request.POST:
        pass1=request.POST.get("pass")
        c.execute("select * from messages where id='"+ request.session["msgid"] +"' and password='"+ pass1 +"' order by date desc")
        co=c.fetchall()
    return render(request,'user/inbox1.html',{"udata":co,"path":path})
def draft(request):
    save='save'
    c.execute("select * from messages where status='"+ save +"' and frommail='"+ request.session["uname"] +"'")
    co=c.fetchall()
    if request.GET:
            msgidd=request.GET.get("msgid")
            if msgidd:
                request.session["msgid"]=msgidd
                return HttpResponseRedirect("/inbox1/")
    return render(request,'user/user_draft.html',{"udata":co})