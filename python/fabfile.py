from fabric.api import run, env, task
# fab -H host1, host2, function name (Everything in script)
#fab -H host1, host2 … function:’command’ (command line argumet)

env.user = '-----'
env.password = '----'

class FabricException(Exception):
    pass

env.abort_exception = FabricException

def cmd(arg):
    s = run(arg)

@task
def scott(arg):
    try:
        run(arg)
    except FabricException:
        print("Something Missing")

@task
def ok(arg):
    run(arg)
