
import json


msg = '''{
"end_time": 10
}
'''



def main(msg):
    msg = json.loads(msg)
    time = 0
    while time < msg['end_time']:
        time=time+1
        print(time)

    return


main(msg)