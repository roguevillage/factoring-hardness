`factoring hardness` Mini-Lesson
================================

Overview
--------

This mini-lesson is designed for 6th-12th grade students with exposure to integer factorization but otherwise varying backgrounds in math and computer science. It is written in the [5E](http://enhancinged.wgbh.org/research/eeeee.html) model.

Engage
------

(Board) `Cryptography` (from Greek: `secret writing`): protects data online

(Discussion) What are some examples of information that you or your parents would want to keep secret online? (Passwords, full name, address, credit card number, etc.) 

* Cryptography relies on there being problems that are "hard" to solve--even for computers!
* `Factoring` is one of those hard problems. Let's explore why!

Explore
-------

(Board) `Algorithm` (from `Al-Khwarizmi`, a Persian mathematician): general steps to solve a problem

(Activity) Construct an `algorithm` for factoring some number N. (Can be in English, math, or code. If you're stuck, consider an example.)

(Discussion) Students' results.

* Candidate (English):
for all the numbers between 1 and N:
    if that number divides N:
       add it to the list of factors

* Candidate (Code):
for i in range(1, N):
    if N%i == 0:
       factors.append(i)

(Guiding Questions)
* How can we tell if a number divides N? (If the remainder is 0. Introduce the `modulus` operator: we let N `modulo` i be the remainder when i divides N.)
* Do we need to try `all` the numbers between 1 and N? Why or why not? (No: each small factor will have a complimentary big factor and vice versa, where we define "small" and "big" in relation to the factor pivot point, the square root of N.)
* How do we know if something is `hard`? (Answers vary, today we will focus on time.)

(Experiment) Test how `hard` factoring is by seeing how much time it takes our algorithm to factor numbers with varying digits. (See factor.py.) Pick 5 different N's with 1-17 digits. 

(Guiding Questions)
* What do you think will happen when the numbers get really big?
* How big will they get before that happens?
* Why is factoring hard?

* Everyone enter 5 results into the class Excel spreadsheet (alt: data table on board)
* Graph digits (x) to time (y), apply best-fit curve.

Explain
-------

(Board) Graph.

(Discussion) 
* What do you notice about this curve? (It gets steep fast--called `exponential`.)
* Why do you think it gets harder to factor the bigger the number gets? (More factors to try.)
* Does the time it takes have anything to do with the factors themselves? Why or why not? (Yes: the fewer, bigger factors the longer it takes.)

Elaborate
---------

* Algorithms for factoring not much better than what we did
* We don't know whether an efficient algorithm for factoring exists--determining the hardness of the problems generally is a big "open" (unsolved) problem in computer science
* Quantum computers could make factoring easy, but it's still in early stages (at time of writing, can factor ~3-digit number in ~45 minutes). 

Extend
------

* How much harder is it to factor a number with 2 big `prime` factors? How do computer scientists use factoring to hide, or `encrypt` information? 
