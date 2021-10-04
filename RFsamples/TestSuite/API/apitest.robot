***Settings***
Library  RequestsLibrary
Library  OperatingSystem

***Variables***
${url}  http://10.0.131.21/
${uri}  GCRevenueAppointment/apiappointment/api/token/create


***Test Cases***
### robot -d ./Report -s apitest Testsuite/api

TestAPIOne
    api_token

***Keywords***

api_token
    ###  create session  aliasname  URL
    create session  aliastoken  ${url}
    ###  Read json from file
    ${json_data}=  Get Binary File  ${EXECDIR}/Pages/API/TestData/json/abc.json
    ###  Headers
    &{headers}=  Create Dictionary  Content-Type=application/json
    ###  post Request
    ${response}=  POST On Session  aliastoken  ${uri}  data=${json_data}  headers=${headers}
    ### Assertion
    Should Be Equal As Strings  ${response.status_code}  200
    ### fetch response data
    ${token}=  Set variable  ${response.text}