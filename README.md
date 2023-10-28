# Overview

I saw a reddit post that the 2023 Atlanta Braves were using some kind of 'sign stealing' which allowed the Braves Ronald Acuna and Matt Olsen to have MVP caliber seasons. The accusation is this, The Braves are 'stealing signs' and are relaying this information through a wistle to their batters. This is hard to prove because one its the automatic response of butt hurt teams and two do to the new pitch com system (bluetooth device that allows catchers and pitchers to communicate). To get enough evidence to prove that something is going on I came up with 3 ways you could try prove this:

1. Rewatch the games, note every time a whistle is heard on offense, the pitch thrown, and the result.
1. Bring a whistle to the game an blow it randomly and see if the hitters get confused.
1. Intercept and decode the pitch com signals

As much as I would like to do all three of those I do not have the time to. Instead I am going to compare the 2017 Huston Astros home and away batting averages with every other teams averages to see if there is a noticeable difference and then see if the 2023 Atlanta Braves experienced a similar benefit. If they did I might look into the above options.

[Software Demo Video Coming](http://youtube.link.goes.here)
[Report](./main.html)

# Data Analysis Results

The 2023 Braves were not experiencing the same advantages that the 2017 Astros at least in the regular season. There is a possibilty that like the Astros they only used this device in important situations that without looking into specific examples filtered by specific condition, which is beyond the scope of this investigation. Due to the Braves postseason performace in the 2023 postseason I do not think that they were cheating in the postseason without building a dataframe and going through it.

I did do some research into you could intercept a pitchcom device in theory. The pitchcon uses radio signals between the catcher and pitcher. These are the same signals that a device like the popular flipper zero uses. I think that it totaly possible that someone could intercept these signals. While I couldn't prove that the Braves (or any other team) was using such a device, I would like to personally do it just for fun.

# Development Environment

IDE - Vissual Studio Code

Libraries -

* Pybaseball
* Pandas
* Altair
* Scipy
* venv 

AI Tools Used -

* Github CoPilot
* ChatGpt 4

Language - 
* Python
* Qmd

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [pybaseball](https://github.com/jldbc/pybaseball)
* [The Base Ball Cube](https://www.thebaseballcube.com/content/playoff_year/2017/)
* [ESPN](espn.com)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* The [Baseball Cube](https://www.thebaseballcube.com/content/playoff_year/2017/) has every pitch that a batter saw in their box office scoring. It would be interesting to dive into this data more.
* Create conditions that would flag certain at bats at home and then look for similar conditions on the road. For example, off speed pitches with runners in scoring position.
* Build a flipper zero like device and experiment with a pitchcom
* blow a whistle randomly at a braves home game
