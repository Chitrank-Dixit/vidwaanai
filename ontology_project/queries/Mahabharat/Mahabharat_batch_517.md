# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Mahabharat 0.5161)
- **Original**: उद्योग और बल सभी कुछ था; इनके सहारे वे अपने धनुषसे
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5161)
- **Original**: उद्योग और बल सभी कुछ था; इनके सहारे वे अपने धनुषसे
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5162)
- **Original**: तेज किये हुए बाणोंकी वर्षा करके कर्णके मर्मस्थानोंको छेदने छूगे। फिर उन्होंने उसकी छातीमें यमदण्डके समान नौ बाण मारे। इस प्रकार चोट-पर-चोट खाकर कर्ण
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5162)
- **Original**: तेज किये हुए बाणोंकी वर्षा करके कर्णके मर्मस्थानोंको छेदने छूगे। फिर उन्होंने उसकी छातीमें यमदण्डके समान नौ बाण मारे। इस प्रकार चोट-पर-चोट खाकर कर्ण
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5163)
- **Original**: अत्यक्त आहत हो गया, उसकी मुट्ठी खुल गयी, घनुष
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5163)
- **Original**: अत्यक्त आहत हो गया, उसकी मुट्ठी खुल गयी, घनुष
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5164)
- **Original**: और तरकस गिर पड़े और वह रथ्षपर ही गिरकर बेहोझ । हो गया। अर्जुन श्रेष्ठ थे और श्रेष्ठ पुरुषोंके ब्रतका पालन
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5164)
- **Original**: और तरकस गिर पड़े और वह रथ्षपर ही गिरकर बेहोझ । हो गया। अर्जुन श्रेष्ठ थे और श्रेष्ठ पुरुषोंके ब्रतका पालन
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5165)
- **Original**: करते थे; उन्होंने जब कर्णको संकटमें पड़ा देखा तो उस समय उसे मारनेका विचार छोड़ दिया। यह देख भगवान्‌
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5165)
- **Original**: करते थे; उन्होंने जब कर्णको संकटमें पड़ा देखा तो उस समय उसे मारनेका विचार छोड़ दिया। यह देख भगवान्‌
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5166)
- **Original**: $े आपके अनुसार उसके जायें पहियेको निगलने लछूगी। रथ डगमग हुआ और एक पहिया जमीनमें बैंस गया। इस प्रकार जब पहिया फैसा, परशुरामजीका दिया श्रीकृष्ण सहसा बोल उठे--'पाण्डुलन्दन ! यह लापरवाही
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5166)
- **Original**: $े आपके अनुसार उसके जायें पहियेको निगलने लछूगी। रथ डगमग हुआ और एक पहिया जमीनमें बैंस गया। इस प्रकार जब पहिया फैसा, परशुरामजीका दिया श्रीकृष्ण सहसा बोल उठे--'पाण्डुलन्दन ! यह लापरवाही
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5167)
- **Original**: हुआ अख्र भूल गया और घोर सर्पपुख बाण भी कट कैसी ? बुद्धिमान्‌ पुरुष संकटमें पड़े हुए शत्रुको मारकर
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5167)
- **Original**: हुआ अख्र भूल गया और घोर सर्पपुख बाण भी कट कैसी ? बुद्धिमान्‌ पुरुष संकटमें पड़े हुए शत्रुको मारकर
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5168)
- **Original**: गया, तब कर्ण बहुत घबराया। बह एक साथ इते धर्ष और वक्ष प्राप्त करते हैं। तुम भी इसका नाझ करनेके
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5168)
- **Original**: गया, तब कर्ण बहुत घबराया। बह एक साथ इते धर्ष और वक्ष प्राप्त करते हैं। तुम भी इसका नाझ करनेके
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5169)
- **Original**: संकटोंको न सह सकतनेके कारण विषादमें डूब गया और लिये शीघ्रता करो; यदि यह पहलेहीके समान शक्तिझाली हो
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5169)
- **Original**: संकटोंको न सह सकतनेके कारण विषादमें डूब गया और लिये शीघ्रता करो; यदि यह पहलेहीके समान शक्तिझाली हो
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5170)
- **Original**: हाथ हिला-हिलाकर धर्मकी निन्‍दा करने लगा--'धर्मवेत्त जाद्ग़ा तो फिर तुमपर आक्रमण करेगा।' तब अर्जुनने
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5170)
- **Original**: हाथ हिला-हिलाकर धर्मकी निन्‍दा करने लगा--'धर्मवेत्त जाद्ग़ा तो फिर तुमपर आक्रमण करेगा।' तब अर्जुनने
- **Translation**: 

---

