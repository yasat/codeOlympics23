import random

choices = {"77686174":["4920646F6E74206B6E6F773F", "77687920646F20796F7520636172653F", "57686174277320697420746F20796F753F"],
           "686F77":["57687920646F6E277420796F752074656C6C206D653F", "492068617665206E6F20696465612C2077687920646F6E277420796F752061736B20736F6D656F6E6520656C73653F", 
                              "5769746820677265617420646966666963756C7479", "4F6E65207374657020617420612074696D65", "427920736865657220666F726365206F662077696C6C"],
           "7768657265":["4E6F7768657265", "496E20796F757220647265616D73", "496E20612067616C617879206661722C206661722061776179", 
                              "49662049206B6E65772C204920776F756C646E27742074656C6C20796F75"],
           "776879":["426563617573652E20576879206E6F743F", "Because Adam and Eve messed up", "57687920646F20796F75207468696E6B3F"],
           "63616E":["4E6F7420696E746572657374656420696E20616E73776572696E6720796F75722064756D62207175657374696F6E73", "4162736F6C7574656C79206E6F74"],
           "77686F":["4920646F6E7420636172652121222C20", "77686F20646F20796F75207468696E6B3F"],
           "7768656E":["6D6179626520746F6461792C206F72206D61796265207965737465726461792E2E2070726F6261626C7920616E20796561722061676F", "4920776F6E742074656C6C20796F752E2E207768792073686F756C6420493F"],
           "7768696368":["4E6F7420696E746572657374656420696E20616E73776572696E6720796F75722064756D62207175657374696F6E73", "6E6F74207768617420796F7520617265207468696E6B696E6720666F72207375726521"],
           "77686F7365":["4E6F7420696E746572657374656420696E20616E73776572696E6720796F75722064756D62207175657374696F6E73", "4D696E6521"]}

generic = ["646F20796F75206B6E6F7720776861742061207175657374696F6E206D65616E733F", "706C6561736520617474656E6420626173696320456E676C69736820636C617373657320616E6420636F6D65206261636B20746F2061736B2061207175657374696F6E2E"]


def askmeanything(question):
    
    for word in question.split():
        if word.lower() in [ bytes.fromhex(i).decode("ascii") for i in choices.keys()]:
            return bytes.fromhex(random.choice(choices[list(choices.keys())[list(choices.keys()).index(word.lower().encode('utf-8').hex())]])).decode("ascii")
    
    return bytes.fromhex(random.choice(generic)).decode("ascii")

while True:
    #just in case. hit 5 to leave
    q = input("Ask any question: ")
    if(q=="5"):
        print(bytes.fromhex("6D6D2E204920616D207469726564206F662074616C6B696E6720746F20796F7520616E797761797321").decode("ascii"))
        break
    answer= askmeanything(q)
    print(answer)