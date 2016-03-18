__author__ = 'sergey'


# AttributeError: 'unicode' object has no attribute 'keys'

import sys

SERVER_IP = "192.168.1.10"

def get_json_loads(str_interval):

    import httplib
    import json

    conn = httplib.HTTPConnection(SERVER_IP, timeout=10) #
    link = "/nodes.json?interval=" + str_interval

    try:
        conn.request("GET", link)
    except:
        m_subject = u"["+config_NHM.SERVER_NAME+u"] Network health monitor"
        str_res = "Connection error.<br>"
        str_res += "Unexpected error:" + str(sys.exc_info()[0]) + str(sys.exc_info()[1])
        print str_res
        m_plain, m_html = (str_res, str_res)
        sys.exit()


    res = conn.getresponse()

    if res.status == 200:

        data = res.read()
        # print "\ndata=", data

        json_loads = json.loads(data)
        print "\njson_loads=", json_loads

        return json_loads

    else:
        m_subject = u"["+config_NHM.SERVER_NAME+u"] Network health monitor"
        str_res = "Connection error.<br>"
        str_res += u"problem : the query returned %s because %s" % (res.status, res.reason)
        print str_res
        m_plain, m_html = (str_res, str_res)
        sys.exit()


def _proc_dict(nd):

    filtered_dict = {}

    try:
        for k in nd.keys():

            print k
            # if k in config_NHM.USED_FIELDS:
            #     filtered_dict[k] = unicode(nd[k])
    except:
        print "error"

    return filtered_dict


get_json_loads("0s")

_proc_dict(u"")