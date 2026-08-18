# transfer-scheduling-optimiser

Welcome to my Missionary Transfer Scheduler project

While serving in the Mission Office of the Italy, Milan Mission for The Church of Jesus Christ of Latter-day Saints, I was responsible for planning and booking all travel for the missionaries in the mission. This included flights, trains, car rentals, taxis, and hotels.

Every six weeks, a transfer occurred. This is the minimum time a missionary is required to spend in one area. On transfer day (the first day of a new transfer), missionaries who were moving would travel, mostly by train, to their next area, which was usually a city. At the time, the mission had around 160 missionaries in it, and it was my job to schedule all of their travel efficiently, then buy the tickets.

The travel planners before me had developed (what I realised to be) an algorithm called the “snake method”. Its purpose was to ensure that, whenever possible, transferring missionaries travelled with another missionary. This was essential because missionaries often carried lots of luggage and did not have SIM cards, so traveling alone across northern Italy (from Arezzo and Siena up to the northern border, including Lugano in Switzerland) could be dangerous or logistically difficult.

The snake method works by creating sequences of dependent moves, known as “snakes.” Each snake begins with a missionary moving to a new location, which may trigger another missionary to move, and so on, forming a chain or cycle. I would manually draw these sequences on paper, ensuring that each missionary was paired, if possible, with a helper travelling along the same route.

At the time, I recognised that this process could potentially be automated, but I did not yet know how to code. I carefully planned all snakes and schedules by hand, buying the trains and making sure all timings were feasible.

**This project is here to make everything easier.**
