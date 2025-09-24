### 1. If you only had 200 labeled replies, how would you improve the model without collecting thousands more?
I’d use a pretrained model like DistilBERT or RoBERTa so it can learn from patterns already trained on large text data. To get more variety, I’d generate paraphrased versions of the same replies or use semi-supervised learning with some unlabeled data.

---

### 2. How would you ensure your reply classifier doesn’t produce biased or unsafe outputs in production?
I’d test the model on different kinds of replies to check for unfair or strange behavior. I’d also set up monitoring so low-confidence or unusual predictions can be flagged for review instead of being sent directly.

---

### 3. Suppose you want to generate personalized cold email openers using an LLM. What prompt design strategies would you use to keep outputs relevant and non-generic?
I’d include details about the recipient (like their role, company, or interest) in the prompt so the text feels personal. I’d also give the model a few good examples and tell it to keep the opener short and professional.