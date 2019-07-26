# Counter.most_common -> 找列表中出现次数最多的元素
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
word_count = Counter(words)
most_common_words = word_count.most_common(3)
print(most_common_words)        # [('eyes', 8), ('the', 5), ('look', 4)]

for word, times in li:
        print(word, times)
