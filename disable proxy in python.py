#to disable proxy for this program
for k in list(os.environ.keys()):
    if k.lower().endswith('_proxy'):
        del os.environ[k]
 
