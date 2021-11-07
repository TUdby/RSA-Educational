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

 -1. Choose two different prime numbers.
 -2. Multiply them together to get our number n, then use them to also find what is called phi of n (we will explain this in more detail later).
 -3. Choose an exponent e that is relatively prime to phi of n.
 -4. Find the inverse of e mod phi of n, this is our decryption exponent d (this is done using an algorithm called the Extended Euclidean Algorithm, we will go over this later).
 -5. Our keys are composed of e, d, and n.

<img src="imgs/3. BasicKeys/KeyCreation.png">

While this is the process for creating the keys, it is not yet enough to understand what is going on or how to code it. In the next few sections we will cover:

 - what the phi function is
 - why e is 'undone' by d mod n
 - how the extended euclidean algorithm works and how it gives us our inverse

After this, we will understand basic RSA and will look at some code. But before we move on to those sections, we need to under

## 4. Eulers Totient (The Phi Function)

The Phi function is also called Eulers Totient. I bring that up so you will recognize 
it by either name, but here I will call it the Phi function. 

<img src="imgs/4. EulersTotient/SemiPrime.png">

<img src="imgs/4. EulersTotient/Prime.png">

<img src="imgs/4. EulersTotient/PrimeFactorizationExample.png">

<img src="imgs/4. EulersTotient/PrimeFactorizationGeneral.png">

<img src="imgs/4. EulersTotient/PhiFunction.png">

<img src="imgs/4. EulersTotient/DerivingSemiPrime.png">

<img src="imgs/4. EulersTotient/DerivingPrime.png">

PROVING BASIC KEYS

<img src="imgs/5. ProvingBasicKeys/EulersTheorem.png">

<img src="imgs/5. ProvingBasicKeys/DivisibleByPhi.png">

<img src="imgs/5. ProvingBasicKeys/MultipleOfPhi.png">

<img src="imgs/5. ProvingBasicKeys/ProvingTheKeysUndo.png">

EUCLIDEAN ALGORITHM

<img src="imgs/6. Euclidean Algorithm/DivisionEquation.png">

<img src="imgs/6. Euclidean Algorithm/DivisionEquationExample.png">

<img src="imgs/6. Euclidean Algorithm/SeriesOfDivisions.png">

<img src="imgs/6. Euclidean Algorithm/RewrittenEquation.png">

<img src="imgs/6. Euclidean Algorithm/EuclideanExample.png">

EXTENDED EUCLIDEAN

<img src="imgs/7. ExtendedEuclidean/GCDEquation.png">

<img src="imgs/7. ExtendedEuclidean/PropertyOfGCDEquation.png">

<img src="imgs/7. ExtendedEuclidean/PropertyOfGCDEquation2.png">

<img src="imgs/7. ExtendedEuclidean/InverseProperty.png">

<img src="imgs/7. ExtendedEuclidean/EuclideanExample.png">

<img src="imgs/7. ExtendedEuclidean/ExtensionExample.png">

<img src="imgs/7. ExtendedEuclidean/AlteredForm.png">

<img src="imgs/7. ExtendedEuclidean/ExampleFirstPart.png">

<img src="imgs/7. ExtendedEuclidean/FirstPartProcess.PNG">

<img src="imgs/7. ExtendedEuclidean/NewSeries1.png">

<img src="imgs/7. ExtendedEuclidean/SecondPartProcess.png">

<img src="imgs/7. ExtendedEuclidean/FinalSeries.png">

<img src="imgs/7. ExtendedEuclidean/ThirdPartProcess.PNG">

<img src="imgs/7. ExtendedEuclidean/ImportantParts.png">

<img src="imgs/7. ExtendedEuclidean/FirstLinearTransformation.png">

<img src="imgs/7. ExtendedEuclidean/AllTransformations.png">

<img src="imgs/7. ExtendedEuclidean/AlteredForm.png">

<img src="imgs/7. ExtendedEuclidean/GeneralTransformations.png">

<img src="imgs/7. ExtendedEuclidean/GCDEquationExample.png">

<img src="imgs/7. ExtendedEuclidean/DotProductForm.PNG">

CHINESE REMAINDER THEOREM

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
