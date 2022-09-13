import pexpect
import time


def main(ipaddr):
    child = pexpect.spawn("telnet " + ipaddr + " 3361")
    d = "0"
    t = 0
    while (True):
        if (d == "0"):
            child.sendline("150.65.230.114:029001:0xC0,0xFF0000")
            child.expect("OK")
            d = "1"
        elif (d == "1"):
            child.sendline("150.65.230.114:029001:0xC0,0x00FF00")
            child.expect("OK")
            d = "2"
            t = t + 1
            if (t > 10):
                break
        elif (d == "2"):
            child.sendline("150.65.230.114:029001:0xC0,0x0000FF")
            child.expect("OK")
            d = "0"

        else:
            break

        time.sleep(0.1)


if __name__ == '__main__':          # importされないときだけmain()を呼ぶ
    main("150.65.230.91")
