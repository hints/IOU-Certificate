import urlparse, urllib, httplib
 
#Example of AUTHENTICATION DETAILS
 
###################################################################
# THIS IS STRICTLY EXAMPLE SOURCE CODE. IT IS ONLY MEANT TO
# QUICKLY DEMONSTRATE THE CONCEPT AND THE USAGE OF THE ACCOUNT
# AUTHNETICATION SERVICE API. PLEASE NOTE THAT THIS IS # *NOT* # PRODUCTION-QUALITY CODE AND SHOULD NOT BE USED AS SUCH.
#
# THIS EXAMPLE CODE IS PROVIDED TO YOU ONLY ON AN "AS IS"
# BASIS WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, EITHER
# EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION ANY WARRANTIES
# OR CONDITIONS OF TITLE, NON-INFRINGEMENT, MERCHANTABILITY OR
# FITNESS FOR A PARTICULAR PURPOSE. PAYPAL MAKES NO WARRANTY THAT
# THE SOFTWARE OR DOCUMENTATION WILL BE ERROR-FREE. IN NO EVENT
# SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL,  EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT
# OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
# OF SUCH DAMAGE.
###################################################################
#TO DO
#The data contained in the request body and http headers are 
#sample test data.  Change the sample data with valid data 
#applicable to your application.
 
headers = {'Content-type':'text/html'}

# Sandbox.
headers['X-PAYPAL-APPLICATION-ID'] = 'APP-80W284485P519543T'

params = {'USER':'ricky@mobnotate.com',
'PWD':'yiggydyiggyd',
'SIGNATURE':'xxxxxxxxxxxxxxx',
'VERSION':'1.3.0',
'token':'HA-xxxxxxxxxx',
'METHOD':'GetAuthDetails'}
 
 
enc_params = urllib.urlencode(params)
 
#Connect to sand box and POST.
conn = httplib.HTTPSConnection("api-3t.sandbox.paypal.com")
conn.request("POST", "/nvp/",enc_params, headers)
 
#Check the response - should be 200 OK.
response = conn.getresponse()
print response.status, response.reason
 
#Get the reply and print it out.
data = response.read()
print urlparse.parse_qs(data)
 
#Close the Connection.
conn.close()

