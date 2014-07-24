<!--
.. date: 2012-01-08 00:22:00
.. slug: arch-linux-paket-grafigi
.. title: Arch Linux Paket Grafiği
.. description: numpy ve matplotlib kullanarak görselleştirmek için, bir kayıt dosyasından veriler alınıyor. Python ile grafik çizme örneği görmek için okuyun.
-->


Şu aralar, Python'daki bilimsel araçlar ve grafik kütüphanelerini
inceliyorum. Bunlarla uğraşırken, merak edip, işletim sistemimi kurduğum
günden bu yana paket ekleme, kaldırma ve güncelleme sayılarımın
grafiğini çizdirdim. Bunlarla ilgilenenler, aşağıdaki örneğe göz atmak
isteyebilirler. <!-- TEASER_END -->


![Arch Linux Packages Graph](/images/package-graph.png)



    :::python
    import re
    import datetime
    import time
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    
    from collections import Counter
    
    months    = mdates.MonthLocator()  # every month
    days      = mdates.DayLocator() # Every day
    monthsFmt = mdates.DateFormatter('%m-%Y')
    
    logfile = "/var/log/pacman.log"
    interesting_line = re.compile(
        r"\[(?P\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] "
        "(?Pinstalled|upgraded|removed)")
    
    installs = Counter()
    upgrades = Counter()
    removes  = Counter()
    with open(logfile) as logfile:
        for line in logfile:
            match = interesting_line.search(line)
            if match:
                struct = time.strptime(match.group("datetime"),"%Y-%m-%d %H:%S")
                date = datetime.date(struct.tm_year, struct.tm_mon, struct.tm_mday)
                if match.group("action") == "installed":
                    installs[date] += 1
                elif match.group("action") == "upgraded":
                    upgrades[date] += 1
                elif match.group("action") == "removed":
                    removes[date] += 1
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    insdatenumpairs = zip(installs.keys(), installs.values())
    insdatenumpairs = sorted(insdatenumpairs, key = lambda pair: pair[0])
    
    upgdatenumpairs = zip(upgrades.keys(), upgrades.values())
    upgdatenumpairs = sorted(upgdatenumpairs, key = lambda pair: pair[0])
    
    remdatenumpairs = zip(removes.keys(), removes.values())
    remdatenumpairs = sorted(remdatenumpairs, key = lambda pair: pair[0])
    
    ax.plot([pair[0] for pair in insdatenumpairs],[pair[1] for pair in insdatenumpairs],"b")
    ax.plot([pair[0] for pair in upgdatenumpairs],[pair[1] for pair in upgdatenumpairs],"g")
    ax.plot([pair[0] for pair in remdatenumpairs],[pair[1] for pair in remdatenumpairs],"y")
    
    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(monthsFmt)
    ax.xaxis.set_minor_locator(days)
    
    datemin = datetime.datetime(min(installs).year, min(installs).month -1, min(installs).day)
    mdate = max([max(installs), max(upgrades), max(removes)])
    datemax = datetime.date(mdate.year, mdate.month + 1, mdate.day)
    ax.set_xlim(datemin, datemax)
    ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
    
    ax.grid(True)
    fig.autofmt_xdate()
    plt.legend(("installs","upgrades","removes"))
    plt.show()