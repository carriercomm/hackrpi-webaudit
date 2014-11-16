import json

data = {
         'Adobe Marketing Cloud' : ['/adobe.*cloud/i'],
         'Analog' : ['analog'],
         'AWStats' : ['awstats'],
         'BBClone' : ['bbcclone', 'bbc'],
         'Chartbeat' : ['chartbeat'],
         'Clicky' : ['clicky'],
         'Cormetrics' : ['cometrics'],
         'Crazyegg' : ['crazy.*eggs'],
         'Deep Log Analyzer' : ['deep.*log'],
         'etracker' : ['etracker'],
         'eXTReMe Tracking' : ['extreme'],
         'FireStats' : ['firestats'],
         'FoxMetrics' : ['fox.*metrics'],
         'Gauges' : ['gauges'],
         'GoingUp' : ['going.*up'],
         'Google Analytics' : ['google.*analytics'],
         'GoStats' : ['go.*stats'],
         'Grape Web Statistics' : ['grape.*web.*statistiics', 'grape'],
         'Hitstats' : ['hitstats', 'hit.*stats'],
         'Hubspot' : ['hubspot'],
         'IceRocket Blog Tracker' : ['ice.*rocket.*blog', 'ice.*rocket'],
         'JAWStats' : ['jaw.*stats', 'jaw'],
         'Kissmetrics' : ['kiss.*metrics'],
         'Koego' : ['koego'],
         'Localytics' : ['localytics'],
         'Metrica' : ['metrica'],
         'Mint' : ['mint'],
         'Mixpanel' : ['mixpanel'],
         'mochibot' : ['mochibot'],
         'Nedstat' : ['nedstat'],
         'Open Web Analytics' : ['open.*web.*analytics'],
         'Piwik' : ['piwik'],
         'Reinvigorate' : ['reinvigorate'],
         'Site Meter' : ['site.*meter'],
         'Slim Stat' : ['slim.*stat'],
         'Splunk' : ['splunk.*storm'],
         'Stat24' : ['stat.*24'],
         'StatCounter' : ['stat.*counter'],
         'StuffedTracker' : ['stuffed.*tracker'],
         'TraceWatch' : ['trace.*watch'],
         'Unica' : ['unica'],
         'VisiStat' : ['visi.*stat'],
         'Visual Website Optimizer' : ['visual.*website.*optimizer'],
         'Webalizer' : ['webalizer'],
         'Weblog Expert' : ['weblog.*expert'],
         'Webtrends' : ['webtrends'],
         'Woopra' : ['woopra'],
         'Yahoo! Marketing Dashboard' : ['yahoo!.*marketing.*dashboard',
           "yahoo"]
         };

with open('tracking_services.json', 'w') as outfile:
  json.dump(data, outfile)