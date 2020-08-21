# lever: A Command-line To-do Manager

## Introduction

lever is a command-line to-do manager that treats daily schedules as series of projects and corresponding "working cycles".

Command `lever` enters a REPL mode that allows you to manage projects and cycles in a way that's similar to managing files and directories using `ls`, `rm`. You can find syntax explanation by entering `help` in the REPL.

Command `lever pull` prints out a simple report listing your current projects and cycles (as if you're getting instructions from a git remote).

(It's still a stupid program in development)

## Coming Soon

+ `lever push`: users can enter their daily summaries
+ `lever stat`: statistics
+ `lever add/ls/rm`: access lever's main functions without calling the REPL

## Q/A

### Why bother writing a new program?

For some reasons, I found traditional to-dos a bit useless for me:

1. I tend to just forget personal long-term schedules
2. short-term goals are easily delayed over and over again

I think the problem might be that traditional to-dos are not that closely related to time and the internal drives are just not strong enough to make me stick to the plan. So I tried to make a system that is time-centered and "works like a lever" -- like a physical start button for users to push in order to enhance internal drive subconsciously (inspired by a scene in *the Avengers* when Ironman was trapped in a huge propeller and Captain America had to pull the lever).
