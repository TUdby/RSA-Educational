# RSA-Educational
The readme walks through RSA and the building of the example code provided.


# Basic RSA
RSA can be enhanced by something called the Chinese Remainder Theorem. We will go over 
that, but first we will go over basic RSA without it.

## The Algorithm
Assume we have a private key "Priv" and a public key "Pub" as shown below (we will 
show where they come from later). The algorithm for encrypting and decrypting is as
follows, where k is the original number and h is the encrypted number.

BASIC ALGORITHM

<img src="imgs/1. BasicAlgorithm/BasicKeys.png">

<img src="imgs/1. BasicAlgorithm/BasicAlgorithm.png">

MODULAR EXPONENTIATION

<img src="imgs/2. ModularExponentiation/BinaryExpansion.png">

<img src="imgs/2. ModularExponentiation/BinaryExponents.png">

<img src="imgs/2. ModularExponentiation/PowersTable.png">

<img src="imgs/2. ModularExponentiation/ImportantPowers1.png">

<img src="imgs/2. ModularExponentiation/ImportantPowers2.png">

<img src="imgs/2. ModularExponentiation/FinalAnswer.png">

BASIC KEYS

<img src="imgs/3. BasicKeys/KeyCreation.png">

EULERS TOTIENT

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
