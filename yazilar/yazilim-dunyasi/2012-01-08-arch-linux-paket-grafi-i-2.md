<!--
.. date: 2012-01-08 01:07:35
.. slug: arch-linux-paket-grafigi-2
.. title: Arch Linux Paket Grafiği - 2
.. description: Düzenli ifadeler ile bir log dosyasından ayıklanan veriler, numpy ve matplotlib olarak görselleştiriliyor. Python ile grafik çizmenin güzel bir örneği.
-->
Bir önceki mesajımdaki kodu biraz değiştirerek, zaman içindeki toplam
paket sayısındaki değişikliği de elde edebiliriz. <!-- TEASER_END -->

![Arch Linux Packages Graph](/images/package-graph-2.png)

    :::python
    import re
    import datetime
    import time
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    
    from collections import Counter
    
    months    = mdates.MonthLocator()  # every month
    days      = mdates.DayLocator() # Every day
    monthsFmt = mdates.DateFormatter('%m-%Y')
    
    logfile = "/var/log/pacman.log"
    interesting_line = re.compile(
        r"\[(?P\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] "
        "(?Pinstalled|removed)")
    
    total = 0
    packs = Counter()
    with open(logfile) as logfile:
        for line in logfile:
            match = interesting_line.search(line)
            if match:
                struct = time.strptime(match.group("datetime"),"%Y-%m-%d %H:%S")
                date = datetime.date(struct.tm_year, struct.tm_mon, struct.tm_mday)
                if match.group("action") == "installed":
                    total += 1
                elif match.group("action") == "removed":
                    total -= 1
                packs[date] = total
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    datenumpairs = zip(packs.keys(), packs.values())
    datenumpairs = sorted(datenumpairs, key = lambda pair: pair[0])
    
    ax.plot([pair[0] for pair in datenumpairs],[pair[1] for pair in datenumpairs])
    
    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(monthsFmt)
    ax.xaxis.set_minor_locator(days)
    
    datemin = datetime.datetime(min(packs).year, min(packs).month -1, min(packs).day)
    mdate = max(packs)
    datemax = datetime.date(mdate.year, mdate.month + 1, mdate.day)
    ax.set_xlim(datemin, datemax)
    ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
    
    ax.grid(True)
    fig.autofmt_xdate()
    plt.xlabel("Date")
    plt.ylabel("# of packages")
    plt.show()