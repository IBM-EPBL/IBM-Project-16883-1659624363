import ibm_db
import func


try:
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=2f3279a5-73d1-4859-88f0-a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30756;Security=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=xrt84341;PWD=1btQTQlOXbistU6S;", "", "")
    print('Connected to Database')
except:
    print("Connection failed")


def register(name, email,  password,phonenumber,aadhar):
    func.register(name, email,  password,phonenumber, aadhar , conn)


def login(email, password):
    loginresult = func.login(email, password, conn)
    return loginresult


def adduserDetails(address, city, state, role, bloodgroup,donorstatus,email,age):
    result=func.addUserDetailsfunc(address, city, state, role, bloodgroup, donorstatus, email , age , conn)
    return result

def getuser(email):
    user = func.getUserDetails(conn)
    return user


def filterLocation(city):
    user = func.filterUsingLocation(city, conn)
    return user


def filterRole(role):
    user = func.filterUsingRole(role, conn)
    return user

def getplasma(bloodgroup , unitrequired , state ,city):
    user=func.getPlasma(bloodgroup , unitrequired, state, city, conn)
    return user

# admin privilages


def getapproveddonor():
    user = func.getapproveddonor(conn)
    return user
def getallusers():
    user = func.getallusers(conn)
    return user


def approverequest(email,status):
    func.approveRequest(email,status,conn)