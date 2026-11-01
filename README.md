# The-Zon
The Zon.

Predictors to use:
1. Pickup season
2. Pickup day of week
3. Pickup hour
4. Pickup location ID
5. Dropoff location ID
6. Passenger count
7. Trip distance
8. RateCodeID
9. Total fare amount
10. Airport trip status

List of things we need to do:

- Research Question:
  - "Where/when/how do taxi drivers get tipped the most in NYC"
- Write the data cleaning code in Rmd:
  - Luca
- Fit a MLR model to the data
- Determine interaction terms (at least one between a categorical variable and a numerical variable)
- Check assumptions.
  - Plot residuals of fitted vs response, predictors vs each others.
- Evaluate if there are any assumption violations.
- Find peer reviewed articles relating to our research question.
  - Sandro
- Write Proposal
  - Luca

# Baseball Reference Section- Courtesy of my good friend Claude
## The basic idea

Two teams of nine players take turns batting (offense) and fielding (defense). The batting team scores a **run** when a player goes around all four bases (first, second, third, and back to home plate) without being put out. The fielding team tries to get three **outs**, which ends the batting team's turn. Whoever has more runs at the end wins.

## Structure of a game

- A game has **9 innings**. Each inning has two halves: the visiting team bats in the **top**, and the home team bats in the **bottom**.
- A half-inning ends after **three outs**, however long that takes. Baseball has no game clock.
- If the home team is ahead after the top of the 9th, the bottom of the 9th isn't played, since they've already won.
- If the home team takes the lead in the bottom of the 9th or later, the game ends right away. This is a **walk-off**.
- If the score is tied after 9 innings, the teams play **extra innings** until one side leads at the end of a full inning. In MLB, each extra half-inning starts with a runner already on second base (the "ghost runner") to speed things up.

## The field

- The **infield** is a 90-foot square called the **diamond**, with home plate, first, second, and third base at its corners.
- The **pitcher's mound** sits in the middle, 60 feet 6 inches from home plate.
- The **outfield** is the large grass area beyond the infield, bounded by a fence or wall.
- **Foul lines** run from home plate past first and third base out to the outfield wall. A ball landing between them is **fair**. Outside them, it's **foul**.

## The defensive positions

1. **Pitcher (P):** throws the ball to the batter
2. **Catcher (C):** crouches behind home plate and receives pitches
3. **First baseman (1B)**
4. **Second baseman (2B)**
5. **Third baseman (3B)**
6. **Shortstop (SS):** plays between second and third
7. **Left fielder (LF)**
8. **Center fielder (CF)**
9. **Right fielder (RF)**

The numbers are used in scorekeeping. A "6-4-3 double play" means shortstop to second baseman to first baseman.

## The pitcher vs. batter matchup

Every play starts with a pitch, and each batter's turn is called a **plate appearance** (or "at-bat," which in statistics has a narrower meaning).

### The strike zone
The strike zone is an imaginary box over home plate. It runs from roughly the hollow below the batter's kneecap up to the midpoint between the shoulders and the top of the pants. The home plate umpire calls each pitch.

### Balls and strikes
- A **strike** is a pitch in the zone that the batter doesn't swing at, any pitch the batter swings at and misses, or a **foul ball**.
- A **ball** is a pitch outside the zone that the batter doesn't swing at.
- The **count** is always stated balls first, so "2–1" means 2 balls and 1 strike.

### How the plate appearance ends
- **Strikeout:** 3 strikes and the batter is out. The exception: a foul ball can't be strike three (unless it's a bunt). With two strikes, a batter can keep fouling pitches off indefinitely.
- **Walk (base on balls):** 4 balls and the batter goes to first base for free.
- **Hit by pitch:** the batter goes to first base.
- **Ball in play:** the batter hits a fair ball and the play is on.

**Dropped third strike:** if the catcher doesn't catch strike three cleanly, the batter can try to run to first. This only applies when first base is empty, or when there are two outs. Otherwise the batter is simply out.

## Hitting and running

When a batter hits a fair ball, he becomes a **runner** and must head for first base. Outcomes include:

- **Single, double, triple:** the batter reaches first, second, or third safely on a hit.
- **Home run:** the ball goes over the outfield fence in fair territory. The batter and every runner on base score. A **grand slam** is a home run with the bases loaded, worth 4 runs.
- **Inside-the-park home run:** the batter circles all the bases without the ball leaving the field. This is rare.
- **Ground-rule double:** a fair ball bounces over the fence. The batter gets second base and runners advance two bases.

Runners may also advance on their own:
- **Stolen base:** running to the next base while the pitcher is delivering, and getting there before being tagged.
- **Wild pitch / passed ball:** the pitch gets away from the catcher, and runners can advance.
- **Errors:** a fielder's mistake lets a runner advance or reach base.

Only one runner can occupy a base at a time, and runners must touch the bases in order.

## How outs are made

1. **Strikeout:** see above.
2. **Fly out / line out / pop out:** a fielder catches a batted ball in the air before it touches the ground. This counts whether the ball is fair or foul, so a caught foul ball is an out.
3. **Force out:** a runner is forced to advance when the batter becomes a runner and the base behind him needs to be cleared. A fielder holding the ball only needs to touch the base before the runner gets there. The most common example is a ground ball thrown to first.
4. **Tag out:** if a runner isn't forced (for example, trying to stretch a single into a double), the fielder has to tag the runner with the ball while the runner is off a base.
5. **Other ways:** running more than three feet out of the baseline to avoid a tag, interfering with a fielder, being hit by a batted ball, or passing another runner.

**Double play / triple play:** getting two or three outs on a single play. The classic is a ground ball with a runner on first: the fielders throw to second (force out), then to first (force out).

### Tagging up
When a fly ball is caught, runners have to return to (or stay on) their base until the moment the ball is first touched. Only then can they try to advance. A **sacrifice fly** is a fly ball caught for an out that lets a runner on third tag up and score.

### Ties go to the runner
If the runner and the throw arrive at the base at the same time, the runner is safe. (Strictly, the rulebook says the fielder has to beat the runner.)

## Some of the trickier rules

- **Infield fly rule:** with fewer than two outs and runners on first and second (or the bases loaded), a routine pop-up in the infield makes the batter out automatically, whether or not it's caught. Without this rule, a fielder could drop the ball on purpose and turn it into an easy double play, because the runners would have stayed near their bases.
- **Balk:** an illegal motion by the pitcher with runners on base, such as faking a pitch or not coming to a stop in the set position. Every runner advances one base. The rule exists to keep pitchers from deceiving runners.
- **Fair vs. foul:** a ball that passes first or third base is judged by where it crosses the line. A ball that stops short of those bases is judged by where it is when it stops or is touched. The foul lines and foul poles count as fair.
- **Fan interference:** if a fan reaches into the field of play and touches the ball, the umpire places runners where he judges they would have ended up.
- **Batting order:** each team bats in a fixed order of 9 hitters. Batting out of order can lead to outs being called.
- **Substitutions:** a player who is taken out of the game can't come back in. (Youth and recreational leagues often relax this.)

## Pitching specifics

- The pitcher must have a foot on the **pitching rubber** when delivering.
- There are two legal starting positions: the **windup** (usually with the bases empty) and the **stretch/set** (with runners on, to keep them from getting big leads).
- Pitchers can try a **pickoff**, a throw to a base to catch a runner leading off too far.
- Teams use **starting pitchers**, who typically go 5–7 innings, and **relievers** from the **bullpen**. The **closer** finishes close games.
- **Designated hitter (DH):** since 2022, both MLB leagues use a DH who bats in the pitcher's place.

## Modern MLB rule changes (2023 onward)

- **Pitch clock:** pitchers have 15 seconds to start their delivery with the bases empty and 18 seconds with runners on. Violations add a ball. Batters must be ready with 8 seconds left or they're charged a strike.
- **Pickoff limit:** a pitcher can disengage (pick off or step off) only twice per plate appearance. A third failed attempt is a balk.
- **Bigger bases:** 18-inch squares instead of 15-inch. This encourages stealing and reduces collisions.
- **Shift ban:** two infielders have to be on each side of second base, all four must be on the infield dirt when the pitch is thrown, and they can't swap sides.
- **Robot umpire challenges:** starting in 2026, MLB uses an automated ball-strike (ABS) system in which batters, pitchers, and catchers can challenge a limited number of ball/strike calls.

## Scoring and statistics basics

- **Runs (R):** the only thing that decides who wins.
- **Hits (H)** and **Errors (E):** shown on the scoreboard next to runs.
- **RBI (runs batted in):** credited to a batter whose action brings a run home.
- **Batting average:** hits ÷ at-bats. Walks, sacrifices, and hit-by-pitches don't count as at-bats. Around .300 is excellent.
- **ERA (earned run average):** earned runs a pitcher allows per 9 innings. Runs that score because of errors don't count against the pitcher. Under 3.00 is excellent.
- **Win/Loss/Save:** credited to pitchers based on when the lead was gained or protected.

## A sample sequence

Runner on first, one out. The batter hits a ground ball to the shortstop. The shortstop throws to the second baseman, who steps on second base (force out on the runner, 2 outs) and throws to first ahead of the batter (force out, 3 outs). That's a 6-4-3 double play, and the inning is over.

If you'd like, I can go further into strategy next: why teams bunt, when to intentionally walk a batter, how pitchers set up hitters with different pitch types, or how lineups are built.

# Index: Predictors and Response variables for our model
## Response- RBI *(Runs Batted In)*:
An RBI, or **run batted in**, is a stat credited to a batter when something they did at the plate lets a run score. It measures how much a hitter drives in teammates, and themselves on a home run.

**What earns an RBI:**
- A hit that scores a runner. A single with a runner on third that scores him is 1 RBI.
- A home run, which counts the batter's own run plus every runner on base. A solo homer is 1 RBI and a grand slam is 4.
- A sacrifice fly or sacrifice bunt that scores a runner.
- A ground-ball out that scores a runner from third.
- A walk, hit-by-pitch, or catcher's interference with the bases loaded, which forces in a run.

**What doesn't earn an RBI:**
- A run that scores because of a fielder's error, as long as the run wouldn't have scored without it.
- A run that scores while the batter grounds into a double play.
- A run that scores on a wild pitch, passed ball, balk, or stolen base, since those happen independently of the batter.

**Example:** bases loaded, and the batter hits a double that scores two runners while the third stops at third base. That's 2 RBIs.

RBIs used to be one of the three "Triple Crown" stats, along with batting average and home runs. Many analysts now think they say as much about a hitter's teammates as about the hitter, because you can only drive in runners who are already on base. A great hitter in a weak lineup gets fewer chances.

## Predictors:
- **Age:** age of the player
- **WAR** *(Wins Above Replacement)*: estimates how many more wins a player adds to his team than a readily available minor-league-level "replacement" player would.
- **G**: Games played
- **PA** *(Plate Appearance)*: any completed turn a batter takes at the plate, whatever the outcome: hits, outs, walks, hit-by-pitches, and sacrifices all count.
- **AB** *(At-Bat)*: a plate appearance that doesn’t end in a walk, hit-by-pitch, sacrifice, or catcher’s interference, so it counts only the times a batter got a fair chance to get a hit.
- **R**: Runs made (times player has crossed home plate)
- **H**: Hits- when a batter puts the ball in fair play and safely reaches base (single, double, triple, or home run), without the help of a fielding error or a fielder’s choice that puts out another runner.
- **X2B**: Doubles- hits that result in the runner reaching second base
- **X3B**: Triples- hits that result in the runner reaching third base
- **HR**: Home Run- hits that land outside the field of play, in fair territory
- **BB** *(Base-on-balls; also known as* ***walks****)*: Plate Appearance that ends in the batter reaching first base as a result of 4 balls
- **SO**: times struck-out
- **BA** *(Batting Average)*: hits divided by at-bats, which is the share of a batter’s at-bats that end in a hit. For example, .300 means 3 hits in every 10 at-bats.
- **OBP** *(On-base percentage)*: how often a batter reaches base by a hit, walk, or hit-by-pitch: (H + BB + HBP) ÷ (AB + BB + HBP + SF).
- **SLG** *(Slugging percentage)*: total bases per at-bat, where a single counts 1, a double 2, a triple 3, and a home run 4. It measures a hitter’s power, not just how often he gets hits.
- **OPS**: **O**n-base **p**lus **s**lugging.
- **GIDP**: Ground-into-double-play
- **HBP**: hit-by-pitch
- **SH/SF** *(Sacrifice hit/Sacrifice fly)*: a hit (bunt)/fly ball resulting in an out that still lets a runner tag up and score. The batter gets an RBI, and it doesn’t count as an at-bat.
- **IBB**: Intentional base-on-ball (walk)- when ~~an opponent is so good~~ a team is so dogshit that the manager has no faith that the defence can prevent the hitter from shitting all over the team, so they avoid hitting to him.
