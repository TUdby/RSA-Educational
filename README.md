# RSA-Educational
The readme walks through RSA and the building of the example code provided.




## 1. The Basic Algorithm
RSA can be enhanced by something called the Chinese Remainder Theorem. We will go over 
that, but first we will go over basic RSA without it.

Assume we have a private key "Priv" and a public key "Pub" as shown below (we will 
show where they come from later). The algorithm for encrypting and decrypting is as
follows, where k is the original number and h is the encrypted number.

<img src="imgs/1. BasicAlgorithm/BasicKeys.png">

The public key is the ordered pair of a number e and a number n. The number e is the encryption exponent, and n is our modulo number. Likewise, the private key is the pair
of d and n, where d is the decryption exponent. With these keys, the algorithm is
shown below.

<img src="imgs/1. BasicAlgorithm/BasicAlgorithm.png">

A number k is encrypted by raising it to the power of e and reducing mod n to get the 
encrypted number h. Then decryption is simply h to the power of d reduced mod n. The 
following code snippet is a naive implementation this algorithm.

CODE SNIPPET MUST GO HERE

## 2. Modular Exponentiation

The problem with that implementation is that, even for very small exponents, the number
k taken to e and the number h taken to d will both be far too large for the computer to
handle efficiently. So to really implement the basic RSA algorithm we need to look at
another algorithm called modular exponentiation.

To begin, every number can be broken into what is called its binary expansion. This is
the sum of powers of two that add up to make the number (this process is used to
translate decimal numbers into binary). Take 67 as an example:

<img src="imgs/2. ModularExponentiation/BinaryExpansion.png">

Knowing our exponent rules, a number to an exponent times that same number to another
exponent is that number to the sum of the exponents. This fact can also be used to 
break a number to an exponent into pieces. For example, take 5 to the power of 67.

<img src="imgs/2. ModularExponentiation/BinaryExponents.png">

Notice that we used this fact to break the exponent into its binary expansion.

Now say we wanted to take 5 to the power of 67 and reduce it mod 29. 5 is 5 to the first
power. If we square it we get five squared. When this is reduced mod 21 we find that 5 
squared is congruent to 4 mod 29. If we squared 4, this is the same as squareing 5 
squared, which is 5 to the fourth. Squared again and we get 5 to the eighth. Continuing
on we get 5 to the power of a number that is itself a power of two. Using this process, 
we fill in the following table. See how this process is able to calculate very large 
exponents through only a little multiplication? (Infact, we will never deal with any 
number larger than the modulo number minus one sqaured.)

<img src="imgs/2. ModularExponentiation/PowersTable.png">

Using this table we see that:

<img src="imgs/2. ModularExponentiation/ImportantPowers1.png">

We also know that:

<img src="imgs/2. ModularExponentiation/ImportantPowers2.png">

Plugging in our values we see that:

<img src="imgs/2. ModularExponentiation/FinalAnswer.png">

This whole algorithm is called modular exponentiation. Here is a snippet of code where
we implement this algorithm. 

SNIPPET

And now we simply tweek the basic algorithm by introducing this function call.

SNIPPET

## 3. Basic Keys

Now we need to set up the keys for basic RSA. The process is shown in the image below.
The steps are this.

 1. Choose two different prime numbers.
 2. Multiply them together to get our number n, then use them to also find what is called phi of n (we will explain this in more detail later).
 3. Choose an exponent e that is relatively prime to phi of n.
 4. Find the inverse of e mod phi of n, this is our decryption exponent d (this is done using an algorithm called the Extended Euclidean Algorithm, we will go over this later).
 5. Our keys are composed of e, d, and n.

<img src="imgs/3. BasicKeys/KeyCreation.png">

While this is the process for creating the keys, it is not yet enough to understand what is going on or how to code it. In the next few sections we will cover:

 - what the phi function is
 - why e is 'undone' by d mod n
 - how the extended euclidean algorithm works and how it gives us our inverse

After this, we will understand basic RSA and will look at some code. But before we move
on to those sections, we need to understand what the "trapdoor" is with RSA. By
trapdoor, we mean the information that someone can encrypt without knowing, but must 
know in order to decrypt. Thus, while we know the trapdoor because we are the ones who 
created it, hackers need to search an obscenely large amount of time to find it. If 
found, the trapdoor will let people into our encrypted messages.

The trapdoor in RSA is the relationship between our primes, p and q, and the semiprime
created by multiplying them together (n). It turns out that traditional computers and 
algorithms struggle immensely in breaking a large semiprime into its primes.

Notice that p and q are used to create phi of n. In turn, phi of n is used to create the 
decryption exponent d. The way we use the primes to do this is not something that can be 
extrapolated if we only know the semiprime. The encryption exponent uses the semiprime 
to encrypt, but unless it is found out how to break the semiprime into its primes, the 
decryption algorithm will not be found. This is the trapdoor of RSA.

## 4. Eulers Totient (The Phi Function)

The Phi function is also called Eulers Totient. I bring that up so you will recognize 
it by either name, but here I will call it the Phi function. The phi function confuses 
some people because it appears to come in different forms. We saw that phi of our 
semiprime was:

<img src="imgs/4. EulersTotient/SemiPrime.png">

But later, when we cover the Chinese Remainder Theorem, we will use the fact that phi of 
a prime number is:

<img src="imgs/4. EulersTotient/Prime.png">

So what is the phi function and why does it seem to have different forms? These 
“different forms” turn out to all be specific results from the same general form. The
phi function is defined to answer the following question: if I input a number n, how
many numbers smaller than n are relatively prime to n?

Before we see the general function, remember that every number has a unique set of prime 
factors. A certain unique prime factor may be multiplied more than once in the creation 
of the number. To give an example of what I mean, take the number twelve:

<img src="imgs/4. EulersTotient/PrimeFactorizationExample.png">

See that the prime factors of 12 are 3, 2, and 2. But two shows up twice so we can write 
two to the power of 2. The unique prime factors are 3 and 2, and two shows up multiple 
times as is shown by its exponent. This final form can be generalized to the prime 
factorization of any number, and an be written as

<img src="imgs/4. EulersTotient/PrimeFactorizationGeneral.png">

Where each p is a unique prime factor and each a is the amount the respective prime 
factor shows up. Using this definition of the prime factorization of a natural number, 
the general form of the phi function is as follows (m is used to mean the amount of 
unique prime factors).

<img src="imgs/4. EulersTotient/PhiFunction.png">

Where this formula comes from is beyond our scope here. The reason I bring it up here is 
so that we can derive the specific forms for semiprimes and for primes. Here is for 
semiprimes:

<img src="imgs/4. EulersTotient/DerivingSemiPrime.png">

And here is for primes:

<img src="imgs/4. EulersTotient/DerivingPrime.png">

We have already used the semiprime form, and will later use the prime form. So this is 
what the function "is", by why is it important? That is the topic of the next section.

## 5. Proving that the Basic Keys Work

In the algorithm for basic RSA, we see that the decryption exponent d undoes what the 
encryption exponent e does. Also, n the section on creating the keys we said that d must 
be the inverse of e within the context of mod phi of n. Now we need to show that if d
is created in this manner, then it trully will 'undo' e.

First, Euler proved a theorem that is now called Eulers Theorem. This theorem is as 
follow.

<img src="imgs/5. ProvingBasicKeys/EulersTheorem.png">

This states that any integer raised to the power of phi of n, then reduced mod n, will 
equal 1 (the proof for this is omitted here, but can be found on youtube). To further 
set up our proof that d undoes e, look at the following. We take the definition of d, 
multiply e to both sides, then subtract the one across. 

<img src="imgs/5. ProvingBasicKeys/DivisibleByPhi.png">

This says that ed-1 is 0 mod phi of n. That statment is equivalent to the statment that 
there exists some number m where m times phi of n equals ed-1.

<img src="imgs/5. ProvingBasicKeys/MultipleOfPhi.png">

With all of this set up, here is the proof. Notice that we use the previous equality to 
swap out the exponent to be in terms of phi of n, then we take advantage of Eulers 
Theorem. This is why phi of n is central to RSA.

<img src="imgs/5. ProvingBasicKeys/ProvingTheKeysUndo.png">

## 6. The Euclidean Algorithm

We talked about the Phi function, we showed that d will undo e, now we need to actually 
compute the inverse of e mod phi of n. To do this we are going to use an algorithm known 
as the Extended Euclidean Algorithm. Before we get to the extended part, lets first look 
at just the basic Euclidean Algorithm.

The Euclidean Algorithm is meant to find the Greatest Common Divisor (gcd) between two 
numbers. If the gcd is 1, the two numbers are called relatively prime (also called 
coprime). The process starts by dividing the larger number  by the smaller number and 
finding the remainder.

When dividing two numbers and finding a remainder, the process can be put in an 
equation. The equation states that if you have a dividend being divided by a divisor, 
then the dividend can be can be expressed as the divisor times the quotient, plus the 
remainder.

<img src="imgs/6. Euclidean Algorithm/DivisionEquation.png">

For example, if we divide 1158 by 873, we get a quotient of 1 with a remainder of 285. 
This can be written as:

<img src="imgs/6. Euclidean Algorithm/DivisionEquationExample.png">

Now say we had two numbers, a and b, where a is the larger of the two, and we wanted to 
find their GCD. First, we set up the equation as we saw before. Then we set up another 
division equation. This time we use the divisor of the previous equation as our 
dividend, and the previous remainder as the new divisor, then we find the new quotient 
and remainder. We repeat this process until we find a remainder of zero. The GCD is the 
last non-zero remainder, 𝑟_𝑛.

<img src="imgs/6. Euclidean Algorithm/SeriesOfDivisions.png">

To see why the last non-zero remainder is the gcd, let’s first show that it is, in fact, 
a divisor. Notice that the last equation in the diagram (on the previous slide) shows 
that 𝑟_𝑛 divides 𝑟_(𝑛−1). Using this, look at the second to last equation. The right 
side is made up of a multiple of 𝑟_𝑛 and a multiple of 𝑟_(𝑛−1) added together. Because 
𝑟_𝑛 divides both of these, it therefore divides the whole right side of the equation, 
which means it also divides the left side of the equation, which is just 𝑟_(𝑛−2). This 
exact line of reasoning can be repeated for the next equation and then the next, 
continuing until we find that 𝑟_𝑛 must divide a and b. Therefore, it is a common 
divisor.

But is it the greatest common divisor? Say we have another divisor, d. Looking at the 
first equation, say we subtract 𝑏(𝑞_1) across to the other side. The equation we get 
is:

<img src="imgs/6. Euclidean Algorithm/RewrittenEquation.png">

Because d divides both a and b (because we assumed it was another common divisor), it 
must divide the left side and therefore also the right side, which is just 𝑟_1. If it 
divides 𝑟_1, then it must be true that 𝑑 ≤ 𝑟_1. We can use this result to do the exact 
same process on the next equation to conclude that 𝑑 ≤ 𝑟_2. Continuing this down to the 
end, we find that 𝑑 ≤ 𝑟_𝑛. Therefore, the last remainder is not only a divisor, but is 
larger than or equal to any other arbitrary divisor. This shows it is the GCD.

Here is a quick example of using the Euclidean Algorithm to find that gcd⁡(1158, 873)=3

<img src="imgs/6. Euclidean Algorithm/EuclideanExample.png">

## 7. The Extended Euclidean Algorithm

That was a thorough enough treatment on the basic Euclidean Algorithm, now for the 
extension. Say d is the gcd of a and b. There exists an r and an s such that:

<img src="imgs/7. ExtendedEuclidean/GCDEquation.png">

The extension is about finding this equation (or rather, the extension is what found the 
existence of this equation, and once the importance of this equation was shown the 
extension became the method of finding this equation when necessary). To understand the 
importance of this, say we reduced both sides mod a. The left side is a divisor of a and 
is therefore smaller than a, it doesn’t reduce any further. But what happens to the 
right side? Obviously it reduces to d as that is what the equation says it equals, but 
is there any more information that can be gotten from that?

Consider the following. Because d is a divisor of a, it must be smaller so it reduces to itself. Then, because ra is a multiple of a, it reduces to zero.

<img src="imgs/7. ExtendedEuclidean/PropertyOfGCDEquation.png">

This shows that s is a number that when multiplied by b and reduced mod a becomes the 
GCD. By symmetric reasoning, r will multiply by a and reduce mod b to become the GCD as 
well. What if the GCD is 1? First, let's state the property of r and s that we just 
found a little more explicitly.

<img src="imgs/7. ExtendedEuclidean/PropertyOfGCDEquation2.png">

If the GCD is 1 then this means:

<img src="imgs/7. ExtendedEuclidean/InverseProperty.png">

So if the GCD is 1, then r and s are the inverses of a mod b and b mod a! See that this 
inverse only exists if the GCD is 1, meaning a and b must be relatively prime. This is 
why we needed gcd⁡(𝑒, 𝜑(𝑛))=1, that way we can find the decryption exponent d, the 
inverse of e mod phi of n.

So the equation 𝑑=𝑟𝑎+𝑠𝑏 is very important; it is how we find inverses between coprime 
numbers in modular arithmetic. The Extension of the Euclidean Algorithm is how we find 
this equation for any numbers a and b. So how does it work?

Take the basic Euclidean algorithm example done on the left. Cut off the last equation 
(after the line), reverse the order of the equations, then isolate the remainders on the 
left-hand side. You should get what you see on the right.

<img src="imgs/7. ExtendedEuclidean/EuclideanExample.png">
<img src="imgs/7. ExtendedEuclidean/ExtensionExample.png">

Further altering the series of equations we got in the previous slide, on the right-hand 
side explicitly give a coefficient of 1 in parenthesis for all numbers that don’t have 
coefficients. For the numbers that do have coefficients, move the negative into the 
coefficient. On the left I have the specific outcome for our example, on the right, I 
have a more general form. Now I want to make some observations.

<img src="imgs/7. ExtendedEuclidean/AlteredForm.png">

The left-hand side of the top equation is the isolated gcd. The right hand side of the 
bottom equation is a multiple of _a_ plus a multiple of _b_. If we can find some way to 
"connect" these two together, we will have our equation. Now notice that every remainder 
on the left-hand side shows up in the equation of the next remainder. This could allow 
us to plug in the equation of a remainder into the equation of the next remainder, which 
is exactly what we will do.

Looking at the example equations we set up, look at the first two.

<img src="imgs/7. ExtendedEuclidean/ExampleFirstPart.png">

Now take the equation for 15 (the second equation) and plug it into 15 in the first 
equation. Then we simplify, but I will do it in a specific way to preserve the form and 
also make explicit a pattern that we will use to make an algorithm using matrices..

<img src="imgs/7. ExtendedEuclidean/FirstPartProcess.PNG">

Now looking at our original series of equations replace the first two that we took out
with the single equation that we just derived.

<img src="imgs/7. ExtendedEuclidean/NewSeries1.png">

Now take the second equation and plug the remainder 18 into the 18 of the first equation
and reduce (this is simply repeating the process we did before).

<img src="imgs/7. ExtendedEuclidean/SecondPartProcess.png">

Again, replace the first two equations with the new one.

<img src="imgs/7. ExtendedEuclidean/FinalSeries.png">

And repeat the process.

<img src="imgs/7. ExtendedEuclidean/ThirdPartProcess.PNG">

Now see that the last equation is the exact one we are looking for! The extension to 
Euclid's algorithm is to collapse the equations together to get one single equation, 
that’s it.

Hopefully you saw my little notes that said to rememver the specific equations that 
showed up in the process, now we are going to use them to create matrices. First, lets 
layout those forms in order.

<img src="imgs/7. ExtendedEuclidean/ImportantParts.png">

Look at the two parenthesis. Let’s say the first parenthesis holds the first index of a 
vector and the second parenthesis holds the second index. The second equation then shows 
a transformation on the vector, and the third equation shows the new vector. A linear 
transformation on a vector can be symbolized as matrix vector multiplication.

What is the transformation that turns our first equation into that third equation? 
Notice that our first parenthesis (our vectors first index) has one times the second 
index of the initial vector, so the first row of our matrix is \[0  1]. The second 
parenthesis (second index) is the second index multiplied by -15 plus the first index. 
So our second row is \[1  -15]. We now have enough to write the following equation.

<img src="imgs/7. ExtendedEuclidean/FirstLinearTransformation.png">

Now looking at the third equation (represented by our new vector) and the fourth 
equation (the next transformation to be represented by a matrix), we see the same 
pattern. The first index of the new vector is just the second index of the previous 
vector. The new second index is the old second index multiplied by some number (in this 
case -3) plus the old first index. This pattern will continue to the end so here is all 
the matrices to save time.

<img src="imgs/7. ExtendedEuclidean/AllTransformations.png">

But where did -1, -3, -15, and -1 come from? Look at the equations we showed a little 
bit ago.

<img src="imgs/7. ExtendedEuclidean/AlteredForm.png">

See how -1, -3, -15, and -1 are just −𝑞_1, −𝑞_2, −𝑞_3, and −𝑞_4? The whole matrix equation can be generalized as seen below.

<img src="imgs/7. ExtendedEuclidean/GeneralTransformations.png">

Now look back at the final equation that the extended algorithm gave us in our example.

<img src="imgs/7. ExtendedEuclidean/GCDEquationExample.png">

Notice that this can be written as the following dot product of the vector of _r_ and 
_s_ and a vector containing 1158 and 873 (example on left, general on right). This is 
neat just to see the final connection, but seeing as how we are really just looking for
_r_ and _s_, our computation can stop after what was seen in the previous slide.

<img src="imgs/7. ExtendedEuclidean/DotProductForm.PNG">

Now we are ready to put this into code. Take the following snippet:

SNIPPET

explanation


## 8. The Chinese Remainder Theorem

<img src="imgs/8. ChineseRemainderTheorem/InitialQuestion.png">



<img src="imgs/8. ChineseRemainderTheorem/QuestionExample.png">

<img src="imgs/8. ChineseRemainderTheorem/ExampleProcess1.png">

<img src="imgs/8. ChineseRemainderTheorem/ExampleProcess2.png">

<img src="imgs/8. ChineseRemainderTheorem/ExampleProcess3.png">

<img src="imgs/8. ChineseRemainderTheorem/ExampleAnswer.png">

<img src="imgs/8. ChineseRemainderTheorem/SlightGeneralQuestion.png">

<img src="imgs/8. ChineseRemainderTheorem/SlightGeneralProcess1.png">

<img src="imgs/8. ChineseRemainderTheorem/SlightGeneralProcess2.png">

<img src="imgs/8. ChineseRemainderTheorem/SlightGeneralProcess3.png">

<img src="imgs/8. ChineseRemainderTheorem/SlightGeneralAnswer.png">

<img src="imgs/8. ChineseRemainderTheorem/InitialQuestion.png">

<img src="imgs/8. ChineseRemainderTheorem/GeneralAnswer.png">

<img src="imgs/8. ChineseRemainderTheorem/PrimeInverses.png">

<img src="imgs/8. ChineseRemainderTheorem/BreakAndBuildProcess.png">

<img src="imgs/8. ChineseRemainderTheorem/Delta.png">

<img src="imgs/8. ChineseRemainderTheorem/DeltaInverse.png">

<img src="imgs/8. ChineseRemainderTheorem/DeltaAndInverseIdentity.png">

<img src="imgs/8. ChineseRemainderTheorem/Integers.png">

<img src="imgs/8. ChineseRemainderTheorem/DeltasMapping.png">

<img src="imgs/8. ChineseRemainderTheorem/MultiplicationRule.png">

<img src="imgs/8. ChineseRemainderTheorem/ExponentWithCRT.png">

RSA WITH CRT

<img src="imgs/9. RSAwithCRT/EncryptionFunction.png">

<img src="imgs/5. ProvingBasicKeys/EulersTheorem.png">

<img src="imgs/4. EulersTotient/Prime.png">

<img src="imgs/9. RSAwithCRT/e1.png">

<img src="imgs/9. RSAwithCRT/ReducingExponent.png">

<img src="imgs/9. RSAwithCRT/EncryptionFunctionReducedExponent.png">

<img src="imgs/9. RSAwithCRT/EncryptionAlgorithm.png">

<img src="imgs/9. RSAwithCRT/DecryptionExponents.png">

<img src="imgs/9. RSAwithCRT/DecryptionFunction.png">

<img src="imgs/9. RSAwithCRT/DecryptionAlgorithm.png">

<img src="imgs/9. RSAwithCRT/KeyCreation.png">

<img src="imgs/9. RSAwithCRT/Algorithm.png">
