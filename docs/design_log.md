WELCOME TO THE DESIGN LOG OF THE **transfer-scheduling-optimiser** PROJECT

JANUARY–MAY 2025 — Introduction & Snake Method

While serving in the Mission Office of the Italy, Milan Mission for The Church of Jesus Christ of Latter-day Saints, I was responsible for planning and booking all travel for the missionaries in the mission. This included flights, trains, car rentals, taxis, and hotels.

Every six weeks, a transfer occurred. This is the minimum time a missionary is required to spend in one area. On transfer day (the first day of a new transfer), missionaries who were moving would travel, mostly by train, to their next area, which was usually a city. At the time, the mission had around 160 missionaries in it, and it was my job to schedule all of their travel efficiently, then buy the tickets.

The travel planners before me had developed (what I realised to be) an algorithm called the “snake method”. Its purpose was to ensure that, whenever possible, transferring missionaries travelled with another missionary. This was essential because missionaries often carried lots of luggage and did not have SIM cards, so traveling alone across northern Italy (from Arezzo and Siena up to the northern border, including Lugano in Switzerland) could be dangerous or logistically difficult.

The snake method works by creating sequences of dependent moves, known as “snakes.” Each snake begins with a missionary moving to a new location, which may trigger another missionary to move, and so on, forming a chain or cycle. I would manually draw these sequences on paper, ensuring that each missionary was paired, if possible, with a helper travelling along the same route.

At the time, I recognised that this process could potentially be automated, but I did not yet know how to code. I carefully planned all snakes and schedules by hand, buying the trains and making sure all timings were feasible.


19th JANUARY 2026 - Code Development

After completing a term of Computer Science at university, I have learned Python and feel ready to tackle automating this process myself. The goal is now to translate the snake method into code, generate the sequences programmatically, and automatically assign optimal travel arrangements based on train schedules.

This is not the end however. The snake algorithm only handles the pairing of missionaries. I would then have to find suitable trains and match up the schedules so that, if possible, missionaries could ALWAYS travel together. This ensures they are not alone and can be helped along the way.

But I will start with just developing the main 'snake method' algorithm first! I have big plans for this, such as adding a GUI and also giving the program to the Italy, Milan mission to see if it works!


19th JANUARY 2026 - snake_plan_testing.py Created

26th JANUARY 2026 - test_environment.csv
I realised that in order to be able to make the algorithm, I need to create a test environment or a test transfer with all of the usual changes so that I can design the algorithm around it. This will take some time


