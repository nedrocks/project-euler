Finding the max product in a grid
=================================
The first time I saw this problem I did a word search and came up with the
correct answer. However, I'm positive this wasn't the intended solution so I
wrote a dynamic programming solution which runs pretty quickly. The obvious 
optimization would be if instead of testing the products I tested sums:

<pre>
lambda *args: 0 if 0 in args else sum(args) if 1 not in args else sum(args) - 1
</pre>

This would require keeping track of the current set of numbers which have the
greatest sum and then print their product.
<br/><br/>
Running with the given implementation:

<pre>
time PYTHONPATH=. python -m problem-11.max_adjacent
70600674

real    0m0.080s
user    0m0.038s
sys 0m0.017s
</pre>

