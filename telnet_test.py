import pexpect

def main(ipaddr):
    child = pexpect.spawn("telnet " + ipaddr + " 3361")
    while (True):
        d = input("ON = 0 , OFF = 1 , finish = 2:")
        if (d == "0"):
            child.sendline("150.65.230.114:029000:0x80,0x30")
            child.expect("OK,150.65.230.114:029003:0x80")
        elif (d == "1"):
            child.sendline("150.65.230.114:029000:0x80,0x31")
            child.expect("OK,150.65.230.114:029003:0x80")
        else:
            break

if __name__ == '__main__':          # importされないときだけmain()を呼ぶ
    main("150.65.230.91")
