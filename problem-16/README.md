Sum of digits in a very large number
====================================

In order to make sure our multiplication doesn't roll over, it's important to
track each digit as its own element in a list. This way, we can do
multiplication like back in elementary school by multiplying each list element
by 2 and carrying the carry over to the next digit. The nice thing is there is
no special handling because multiplying single digits together can only go as
high as 81 (9*9). The output is: 
<pre>
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
</pre>
or in scientific notation: 1.07150861 × 10^301