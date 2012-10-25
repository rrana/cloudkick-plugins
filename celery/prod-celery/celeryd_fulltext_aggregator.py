#!/usr/bin/env python

import sys, os, time

#SET The maximum log freshness time here
DEFAULT_AGE=12000

def check_logs(*logs):
  out = []
  total = 0
  status = 'ok'
  msg = 'everything looks good'
  n = time.time()
  for l in logs:
    if isinstance(l, (list, tuple)):
      limit, l = l
    else:
      limit = DEFAULT_AGE
    try:
      s = os.stat(l)
    except Exception:
      status = 'err'
      msg = "file not found '%s'" % l
    else:
      diff = n - (s.st_mtime)
      msg = 'everything looks good, modified %d seconds ago' % diff
      if diff > limit:
        status = 'err'
        msg = '%s not modified in %d seconds' % (l, diff)

  out.insert(0, "status %s %s" % (status, msg))
  print '\n'.join(out)

if len(sys.argv) < 2:
  sys.exit('Usage: %s <log file to check>' % sys.argv[0])

if not os.path.exists(sys.argv[1]):
  sys.exit('status err file %s not found' % (sys.argv[1]))
else:
  check_logs(sys.argv[1])
