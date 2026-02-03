from flask import Flask, redirect, url_for, session,request,flash,jsonify
from authlib.integrations.flask_client import OAuth
import time
from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

app = Flask(__name__)
app.secret_key = "replace-this-with-a-random-secret"
mod = 1e9+7
oauth = OAuth(app)

google = oauth.register(
    name="google",
    client_id="150380567313-8ki00iqp47lnue56t8d6tmih10vk6g2f.apps.googleusercontent.com",
    client_secret="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",
    access_token_url="https://oauth2.googleapis.com/token",
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    api_base_url="https://www.googleapis.com/oauth2/v2/",
    client_kwargs={"scope": "email profile"},
)

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
table = db.collection('students-atd')

def getrow(sid):
    row = table.document(sid).get()

    row = row.to_dict()

    
    return row

@app.route("/")
def index():

    code = request.args.get('var',0)
    code = (int(time.time())-1)*47  
    t = int(time.time())
    try:
        code=int(code)
        code = code/47
        if not (t-code<=3 and code<=t):
            1/0
    except Exception as e:
        return redirect('https://memes.co.in/video/upload/photos/2022/05/UuVEbQW8cACeXtMDFz61_15_1a6c76af4ab4376e0b16c782cd152f27_image.jpg')
    



    if "email" not in session:
        return '<a href="/paaji">Sign in with Google</a>'
    
    


    email = session["email"]
    initial = email.split("@")[0]
    domain = email.split("@")[1]

    rw=getrow(str(initial))
  

    try:
        if domain != 'dau.ac.in' or len(initial)!=9 or int(initial)==-1 or rw==None:
            1/0
        elif rw.get('atd',True):
            logout()
            return redirect('https://pbs.twimg.com/media/E4QikdDX0AEVxcq.jpg')
            

    except Exception as e:
        logout()    
        return redirect('https://pbs.twimg.com/media/E4EJLGqVUAEkJIw.jpg')

    row=table.document(initial)
    row.set({
        'name' : rw.get('name',''), 
        'atd': True
    })

    return f"""
    <h1> YOUR ATTENDENCE IS MARKED! </h1>
    <h2>Signed in</h2>
    <p><b> student id: </b> {initial}</p>
    <p><b> Name: </b> {rw.get('name','')}</p>
    <a href="/logout">Logout</a>
    """

@app.route("/paaji")
def login():
    return google.authorize_redirect(
        redirect_uri=url_for("auth_callback", _external=True)
    )

@app.route("/auth/google/callback")
def auth_callback():
    token = google.authorize_access_token()
    user = google.get("userinfo").json()

    session["email"] = user["email"]
    session["google_id"] = user["id"]

    return redirect("/")    

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/test")
def test():
# Input data as a string
    # data = """202301005	ARYAN PATEL
    # 202301010	VARSHIL JAYESHBHAI PATEL
    # 202301018	TIRTH KORADIYA
    # 202301031	NEEV VEGADA
    # 202301034	JIYA PATEL
    # 202301036	SHAH AARYA NIRAJ
    # 202301038	KRISHNA KANODIA
    # 202301042	YAMMANURU SAI SREEPADHA
    # 202301044	SANGHANI KAVY MANISHBHAI
    # 202301045	YUNUS KOTHARI
    # 202301047	THUMMAR JEEL HARESHBHAI
    # 202301050	SIVA SUHAS THATAVARTHY
    # 202301051	YUG PATEL
    # 202301053	KARAN MAKASANA
    # 202301054	MANAV KALAVADIYA
    # 202301057	VASANI JENISH ASHOKBHAI
    # 202301061	MEHTA DHRUVIL VIMALKUMAR
    # 202301067	PRINCE CHOVATIYA
    # 202301069	YASHASVI ISHWARBHAI JADAV
    # 202301075	KANANI TIRTH
    # 202301078	PATEL KRISH BHAVESHKUMAR
    # 202301080	HARSHVIR SINGH
    # 202301083	DHAMELIYA UTSKER ARJANBHAI
    # 202301084	AYUSH PATEL
    # 202301088	SANTOKI TAPAS ASHOKBHAI
    # 202301094	PANCHAL YASHKUMAR KALPESHKUMAR
    # 202301102	HET LADANI
    # 202301105	VED PATEL
    # 202301116	KAVYA JITENDRA CHAUHAN
    # 202301118	MUDIT RUNGTA
    # 202301119	DHARVA BIREN PATEL
    # 202301123	BHANVADIYA BHAVYA HARESHBHAI
    # 202301124	PRASANNA GUPTA
    # 202301126	SOJITRA PRINCE PRAVINBHAI
    # 202301133	PARIKH KATHAN HASMUKHBHAI
    # 202301137	SHAH SANYAM TEJALBHAI
    # 202301138	SRI SAI MADHAVA TEJA YANDURI
    # 202301139	LIMBASIYA SMIT MUKESHBHAI
    # 202301145	AYUSH MITTAL
    # 202301167	RISHIT RAJ JAIN
    # 202301168	RATHOD DHRUVIKA MANOJBHAI
    # 202301174	RATHVA HARDIKKUMAR CHHABIRAM
    # 202301175	JETHVA MANTHAN MANISHBHAI
    # 202301176	BARASARA MEET JITENDRABHAI
    # 202301178	PATEL PRINCE JITUBHAI
    # 202301180	VALA SIDDHARTHSINH HARIBHAI
    # 202301182	SORATHIYA BRINDABEN DILIPBHAI
    # 202301186	DONDA VED VIPULBHAI
    # 202301193	GADHVI NANDINI INDRABHAI
    # 202301197	PATEL GAURAV RAKESHBHAI
    # 202301198	MISTRY HARSH RAKESHKUMAR
    # 202301199	JOLIYA VISHALBHAI PARSHOTTAMBHAI
    # 202301200	NADIYA NIHAR RAJESHBHAI
    # 202301204	DHAMECHA AYUSH VIJAYBHAI
    # 202301207	HIRAPARA TARANG RAKESHBHAI
    # 202301212	PATEL ISHTI UPENDRA
    # 202301219	MEET RUPESH GANDHI
    # 202301227	PATEL VEDANT DINESHKUMAR
    # 202301233	NAKUM AYUSH VIJAYBHAI
    # 202301239	AJUDIYA KASHYAP JAGDISHBHAI
    # 202301245	THAKKAR ISHAN MAHENDRA
    # 202301248	BHALARA MOHAMMAD FARZAN IDRISH
    # 202301249	SHAH JENIL SMITESHBHAI
    # 202301251	VASANI DEVARSH CHINTANBHAI
    # 202301254	JAYADITYA SHAH
    # 202301257	BHADARAKA KANU VIRABHAI
    # 202301260	MAHEK JIKKAR
    # 202301263	YUG SAVALIA
    # 202301267	ARAV PIYUSHBHAI VAITHA
    # 202301268	SIDDHANT SHEKHAR
    # 202301270	PATHAK ASHKA KALPESH
    # 202301273	JILL CHHAGNANI
    # 202301410	JOSHI RUCHIR KALPESH
    # 202301444	VAGH DIVYESHKUMAR HIRABHAI
    # 202301466	BHARGA JITEN NILESHBHAI
    # 202301469	GAMIT NEEL BALCHANDRA
    # 202301480	BHAGIYA JENISH RAMESHBHAI
    # 202301486	MAHARSHI PATEL"""

    # # Convert to list of tuples
    # student_list = []
    # lines = data.strip().split('\n')

    # for line in lines:
    #     parts = line.split('\t')
    #     if len(parts) == 2:
    #         student_id = parts[0].strip()
    #         student_name = parts[1].strip()
    #         student_list.append((student_id, student_name))

    # for st in student_list:
    #     row=table.document(str(st[0]))
    #     row.set({
    #         'name': str(st[1]),
    #         'atd': False
    #     })


    return "ok"


if __name__ == "__main__":
    app.run(debug=True)
