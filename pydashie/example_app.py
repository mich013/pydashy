from example_samplers import *
from smartthings import SmartTings


def run(app, xyzzy):
    st = SmartTings()
    
    samplers = [
        SynergySampler(xyzzy, 3),
        BuzzwordsSampler(xyzzy, 2), # 10
        ConvergenceSampler(xyzzy, 1),
    ]

    try:
        app.run(debug=True,
                host="127.0.0.1",
                port=5000,
                threaded=True,
                use_reloader=False,
                use_debugger=True
                )
    finally:
        print "Disconnecting clients"
        xyzzy.stopped = True
        
        print "Stopping %d timers" % len(samplers)
        for (i, sampler) in enumerate(samplers):
            sampler.stop()

    print "Done"
