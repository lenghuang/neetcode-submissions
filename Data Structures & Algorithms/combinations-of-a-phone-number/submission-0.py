'''

For 3,4, i have these options

3 - [d,e,f]
4 - [g,h,i]

dg, dh, di
eg, eh, ei
fg, fh, fi

i've suggested an O(n^2) type thing, this doesn't seem right, would there be duplicates?

3 - [d,e,f]
4 - [g,h,i]
5 - [j,k,l]

dgj, dgk, dgl
dhj, dhk, dhl
dij, dik, dil
...
and so and and so forth
return 3^3 choices?

how can this be faster?

maybe like a tree?

   d
 / | \
g  h  i
|
[all options from 5]

feels like im duplicating the options at each step

maybe i need to build it up

build up the, [d,e,f]
then build. [dg, dh, di, eg, eh, ei, fg, gh, gi]
then build 

hm still the same amount of operations

i feel like you have to generate all of them no matter what..

let me try the first way

-----


for each letter in the possibilities of the first one (d,e,f)
    for each letter in the possibilites of the seond (g,h,i)
       ....

ah. i see the problem. i can't really write O(n) possible for loops.

-----

i need to kinda just like recurse through these 

-----


recurse('') = ''
recurse(acc, n) = recurse(acc + 3) + recurse(acc + 4) + recurse(acc + 5)

for whatever number I'm "adding"

I want to go through all those numbers

and then recurse on all of them

recurse("", "34")
= recurse("d", "4"), recurse("e", "4"), recurse("f", "4")
= recurse("dg", ""), recurse("dh", ""), recurse("di", ""), ... etc etc recurse("e", "4"), recurse("f", "4")

so recurse(acc, thing ur iterating on):
    take the first thing ur iterating on 
    get the letters
    call recurse again on each of those, but this time, append to acc, and do one less letter

maybe storing too many strings but we'll consider that an optimiziation


'''

class Solution:

    def __init__(self):
        self.mapping = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        res = []
        # recurse
        def recurse(digits, acc):
            if len(digits) <= 0:
                print("appending", acc)
                res.append(acc)
                return
            print("digits", digits)
            x = digits[0]
            letters = self.mapping[x]
            for c in letters:
                rest = digits[1:]
                combo = acc + c
                print("rest", rest, "combo", combo)
                recurse(rest, combo)
        # call it
        recurse(digits, "")
        return res
            
