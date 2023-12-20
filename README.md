# Prompt_for_portfolio
Using Large Language Model, MASK Language Model, BERT, FLAN-T5.

## Application
Suppose the user enters "I am a 70-year-old man with a sum of 1 million, how should I invest?", and I have a prompt system for investment suggestions, which will adjust it to the best value based on the user's input. Prompt suitable for chatgpt, so that chatgpt can generate appropriate replies.

## The used two LLMs description of paper
1. Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. (2018). Bert: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805. https://doi.org/10.48550/arXiv.1810.04805
   
2. Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Yunxuan Li, Xuezhi Wang, Mostafa Dehghani, Siddhartha Brahma, Albert Webson, Shixiang Shane Gu, Zhuyun Dai, Mirac Suzgun, Xinyun Chen, Aakanksha Chowdhery, Alex Castro-Ros, Marie Pellat, Kevin Robinson, Dasha Valter, Sharan Narang, Gaurav Mishra, Adams Yu, Vincent Zhao, Yanping Huang, Andrew Dai, Hongkun Yu, Slav Petrov, Ed H. Chi, Jeff Dean, Jacob Devlin, Adam Roberts, Denny Zhou, Quoc V. Le, Jason Wei. (2022). Scaling instruction-finetuned language models. arXiv preprint arXiv:2210.11416. https://doi.org/10.48550/arXiv.2210.11416

## Used two LLMs from hugging face
1. https://huggingface.co/bert-base-uncased
2. https://huggingface.co/google/flan-t5-xxl

## Often used to estimate investors’ risk-return levels
| 風險屬性	 | 風險水平 | 投資取向 |
| -------- | -------- | -------- |
| 保守型 | 7 - 10     | 代表您不願意接受任何投資風險, 您適合的金融產品偏向報酬來自利息收入的產品，縱使利率水準未必跟得上通貨膨脹的幅度。|
| 安穩型	 | 11 –15 | 代表您可以接受低投資風險,希望預期報酬率可以優於中期存款利率,以期投資本金不因通貨膨脹而貶值。 |
| 穩健型	 | 16 –22 | 代表您可以接受中等的投資風險,希望預期報酬率可以優於長期存款利率;以期投資本金不因通貨膨脹而貶值,您可以接受高一點程度的波動。 |
| 成長型	 | 23 –30 | 代表您可以接受高度的投資風險,短、中及長期的波動性均高,希望預期報酬率可以大幅超過通貨膨脹率且適合具波動性的投資品;了解風險及報酬是相對應的，您適合投資的產品是具高報酬且高風險的。 |
| 積極型	 | 31 –35 | 代表您可以接受非常高度的投資風險,短、中及長期的波動性均高,也希望預期報酬極度豐厚,您適合波動性極大的投資產品;預期波動性極高，你可以接受極大的資本損失。 |



