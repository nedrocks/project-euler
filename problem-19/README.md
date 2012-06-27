Months starting in Sunday for a century
=======================================

This is a very naive solution, but it works for any known start point.

I bet there is a better formula, or at least some recursion, based on cycles --
if a year starts on a monday and it is not a leap year it will always contain
the same number of months starting with a Sunday. The reverse is true as well.
Also, the output of what the start of the next year could be generated. Thus,
using the sundays.py script with slight modifications, I can generate this
map:

<pre>
{
(True,0): (2,2),
(True,1): (1,3),
(True,2): (2,4),
(True,3): (2,5),
(True,4): (2,6),
(True,5): (1,0),
(True,6): (2,1),
(False,0): (2,1),
(False,1): (2,2),
(False,2): (1,3),
(False,3): (3,4),
(False,4): (1,5),
(False,5): (2,6),
(False,6): (1,0),
}
</pre>

This maps the key (is_leap_year, day_of_week) to 
(number_of_months_starting_with_sunday, starting_day_of_next_year). Mondays
equal 0 in this example.

Doing a quick view of the pattern, starting with 1901, I see that it repeats
every 34th year. Thus, this could be easily solved with doing some addition
and lookups.