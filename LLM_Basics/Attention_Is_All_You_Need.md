
# Problem in previous Neural Network

- Earlier model were sequential, no parallel processing which made training slow
- It struggled with long term dependencies, ie by the time the network reached end of sequence much of the early information is lost


# Introducing Transformer Neural Network

![alt text](./artifacts/image.png)

Transformer is still a Neural Network, but it adss a special layer called "Attention", which lets all tokens in a sequence talk to each other,  we can think Attention as a communication layer inside the network.

![alt text](./artifacts/image-1.png)

Each token interacts with each other and decides which ones are important for better learning , this allows model to capture the "Context" more efficiently.

![alt text](./artifacts/image-2.png)

The transformer includes an "Encodeer" and a "Decoder" block

![alt text](./artifacts/image-3.png)

Each block has an "Attention" layer and a "MLP / feed forward" layer

![alt text](./artifacts/image-4.png)

Attention layer is where all tokens interact, while in MLP layer the tokens privately refines its representation

Lets take an Example " Jake Learned AI even though it was difficult ." 

Now in Attention layer "it" looks at all other words to figure out what it refers to,  and it learns that "Jake" is the most relvant token,  simililary other tokens also look at each other.

The outputs are upated representation for each token, borrowing information from tokens that are most relevant.

![alt text](./artifacts/image-5.png)

Then in the "MLP" layer the token "it" refines this understanding internally and adjusts its own representation, This combination of communication in Attention and individual refinement by MLP layer is what helps Transformer build contextual understanding.

![alt text](./artifacts/image-6.png)

Ohter details like adding normalisation are just to keep training stable.

![alt text](./artifacts/image-7.png)


**Understanding the flow in transformer**

1. First the tokenizer splits the input in tokens, then these tokens are embedded which means transformed into numerical vector representation.

![alt text](./artifacts/image-8.png)

2. Now transformer has no sense of order by default, so we add Positional information to embeddings, to intriduce a sense of order among tokens. these are special patterns added to embeddings to tell the model where is the token in sequence, otherwise "Jake learned AI" would be considered same as "AI learned Jake".

![alt text](./artifacts/image-9.png)

3. At each step "Attention" mixes information across tokens and "MLP" refines each token.

![alt text](./artifacts/image-10.png)

4. At the end we have rich context aware representation.

![alt text](./artifacts/image-11.png)

5. Now depending on our task we use these final reprenstation differently, for example in text generation task the last representation could be used to predict the next word, similaryl in senditiment analysis task we can rely on first vector to represent entire sentence.

![alt text](./artifacts/image-12.png)

![alt text](./artifacts/image-13.png)


**Lets Dig into Attention Layer**

![alt text](./artifacts/image-14.png)


1. The Attention layer first creates 3 diffrent representation of each token, a Query, a Key and a Value. the query asks "what am I looking for?",  the key says "Here is what I have", and the value carries the actual content to share

![alt text](./artifacts/image-15.png)

![alt text](./artifacts/image-16.png)

2. For example in the sentece the "it" token forms a query vector implicitly asking "what concept am I referring to", the other tokens "Jake" and "AI" each provides the information they hold by key and value.

![alt text](./artifacts/image-17.png)

3. To decide which tokens are relavant we take dot product of token query and the keys of all other tokens in sequence.

![alt text](./artifacts/image-18.png)

4. It will compute higher score for "AI" then for "Jake", showing that "AI" is more relavent in context.

![alt text](./artifacts/image-19.png)

5. Next we normalise these scores often using a "softmax" function to turn them into attention weights

![alt text](./artifacts/image-20.png)

![alt text](./artifacts/image-21.png)

6. These weights acts like focus levels, some tokens get very strong attention while some very little

![alt text](./artifacts/image-22.png)

7. Finally each token gathers information by taking a weighted sum of all the values vectors

![alt text](./artifacts/image-23.png)

8. This process gives a new context aware representation, Mathematically the "Attention is all you need" paper expresses this in matrix form.

![alt text](./artifacts/image-24.png)

9. Instead of looping tokens one by one, the models stacks all query, keys and values into matrices and performs the doct product and softmax function simultaneously

![alt text](./artifacts/image-25.png)

10. Each token communicates with every other token in a set of matrix operation

11. At the very beginning of training, all the parameters are random, therefore all the representations are meaningless, but as training progesses, the parameters that produce queries, keys and values are optimised and overtime the attention layer learns meaningful patterns

![alt text](./artifacts/image-26.png)

12. Ohter details like Masked and Milti head just modfies how attention is calculated 

![alt text](./artifacts/image-27.png)

13. Tranformer can be used for diffent tasks like text generation, translation, summarization and it even extends to ./artifacts/images/audio detection and code generation.

In short a Transformer allows tokens to communicate