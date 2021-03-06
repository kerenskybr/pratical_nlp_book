## :snake: Code from Pratical NLP book

![alt text](https://github.com/kerenskybr/pratical_nlp_book/blob/main/cover.jpg)

## Chapter 1

![alt text](https://github.com/kerenskybr/pratical_nlp_book/blob/main/chapter_1/img/levels.png)
![alt text](https://github.com/kerenskybr/pratical_nlp_book/blob/main/chapter_1/img/sintactic_structure.png)

A linguagem humana é composta por quatro blocos principais: fonemas, morfemas e lexemas, sintaxe e contexto.

**Fonemas:**
Fonemas são as menores unidades de som em uma linguagem. Podem ou nao ter algum significado 
Por exemplo, a palavra “fixo”é pronunciada da seguinte forma:
- fixo
/f/ /i/ /k/ /s/ /o/
Repare que ela tem 4 letras, mas 5 fonemas
- que
/qu/ /e/
A palavra que tem 3 letras e 2 fonemas.

**Morfema:**
É a unidade lingustica minima portadora de significado que nao se pode dividir em unidedas mais pequenas sem passa ao nivel fonológico
Exemplo:
`comer – comia – comem – comilão`: com é o morfema lexical da palavra comer

**Lexemas:**
Lexemas sao a forma estrutural variativa dos morfemas relacionados um ao outro pelo significado. Por exemplo:
As palavras menino, menina, meninos e meninas fazem parte de um mesmo lexema.
As palavras `lindo, linda, lindos, lindas, lindinha e lindíssima` integram o mesmo lexema adjetivo.

**Sintaxe:**
Sao um conjunto de regras que controem o sentido gramatical das palavras e frase de uma linguagem, bem como a relação lógica das frases entre si.

**Contexto:**
É como varias partes de uma linguagem se juntam e convergem em um particular significado. Uma frase pode mudar de significado conforme a situação.

## Chapter 2

Code examples: `html parsing, image parsing (OCR), sentence segmentation and tokenization, spell check and stemming/lemmatization`

![alt text](https://github.com/kerenskybr/pratical_nlp_book/blob/main/chapter_2/img/preprocessing_technics.png)
![alt text](https://github.com/kerenskybr/pratical_nlp_book/blob/main/chapter_2/img/adv_preprocessing.png)
![alt text](https://github.com/kerenskybr/pratical_nlp_book/blob/main/chapter_2/img/specific_tokenization.png)
![alt text](https://github.com/kerenskybr/pratical_nlp_book/blob/main/chapter_2/img/stemming_and_lemmatization.png)

### Data Augmentation Technics:

**Synonym replacement**
Randomly choose “k” words in a sentence that are not stop words. Replace these words with their synonyms. For synonyms, we can use Synsets in Wordnet [3, 4].

**Back translation**
Say we have a sentence, S1, in English. We use a machine-translation library like Google Translate to translate it into some other language—say, German. Let the corresponding sentence in German be S2. Now, we’ll use the machine-translation library again to translate back to English. Let the output sentence be S3.

**TF-IDF–based word replacement**
Back translation can lose certain words that are crucial to the sentence. In [5], the authors use TF-IDF, a concept we’ll introduce in Chapter 3, to handle this.

**Bigram flipping**
Divide the sentence into bigrams. Take one bigram at random and flip it. For example: “I am going to the supermarket.” Here, we take the bigram “going to” and replace it with the flipped one: “to going.”

**Replacing entities**
Replace entities like person name, location, organization, etc., with other entities in the same category. That is, replace person name with another person name, city with another city, etc. For example, in “I live in California,” replace “California” with “London.”

**Adding noise to data**
In many NLP applications, the incoming data contains spelling mistakes. This is primarily due to characteristics of the platform where the data is being generated (for example, Twitter). In such cases, we can add a bit of noise to data to train robust models. For example, randomly choose a word in a sentence and replace it with another word that’s closer in spelling to the first word. Another source of noise is the “fat finger” problem [6] on mobile keyboards. Simulate a QWERTY keyboard error by replacing a few characters with their neighboring characters on the QWERTY keyboard.

**Advanced techniques**
There are other advanced techniques and systems that can augment text data. Some of the notable ones are:

**Snorkel**
This is a system for building training data automatically, without manual labeling. Using Snorkel, a large training dataset can be “created”—without manual labeling—using heuristics and creating synthetic data by transforming existing data and creating new data samples. This approach was shown to work well at Google in the recent past [9].

**Easy Data Augmentation (EDA) and NLPAug**
These two libraries are used to create synthetic samples for NLP. They provide implementation of various data augmentation techniques, including some techniques that we discussed previously.

**Active learning**
This is a specialized paradigm of ML where the learning algorithm can interactively query a data point and get its label. It is used in scenarios where there is an abundance of unlabeled data but manually labeling is expensive. In such cases, the question becomes: for which data points should we ask for labels to maximize learning while keeping the labeling cost low?

## Chapter 3

comming soon