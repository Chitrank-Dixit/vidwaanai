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

### Verse 1 (Mahabharat 941.8411)
- **Original**: है और सुख-दुःख अनित्य। इसी प्रकार जीवात्मा नित्य है और प्रगवान्‌ व्यासने इस पवित्र संहिताको प्रकट करके अपने पुत्र
- **Translation**: 

---

### Verse 2 (Mahabharat 941.8411)
- **Original**: है और सुख-दुःख अनित्य। इसी प्रकार जीवात्मा नित्य है और प्रगवान्‌ व्यासने इस पवित्र संहिताको प्रकट करके अपने पुत्र
- **Translation**: 

---

### Verse 3 (Mahabharat 941.8412)
- **Original**: उसके बयनका हेतु अनित्य $।' यह महाभासतका सारभूत शुकदेवजीको पढ़ाया था, वे महाभारतके सारभूत उपदेशका
- **Translation**: 

---

### Verse 4 (Mahabharat 941.8412)
- **Original**: उसके बयनका हेतु अनित्य $।' यह महाभासतका सारभूत शुकदेवजीको पढ़ाया था, वे महाभारतके सारभूत उपदेशका
- **Translation**: 

---

### Verse 5 (Mahabharat 941.8413)
- **Original**: उपदेश भारत-साविज्ीके नामसे प्रसिद्ध है। जो प्रतिदिन सबेरे इस प्रकार वर्णन कस हैं-.'मनुष्य इस जगतंमें हजारों
- **Translation**: 

---

### Verse 6 (Mahabharat 941.8413)
- **Original**: उपदेश भारत-साविज्ीके नामसे प्रसिद्ध है। जो प्रतिदिन सबेरे इस प्रकार वर्णन कस हैं-.'मनुष्य इस जगतंमें हजारों
- **Translation**: 

---

### Verse 7 (Mahabharat 941.8414)
- **Original**: उठकर इसका पाठ कख्ता है, वह सम्पूर्ण महाभाखके माता-पिताओं तथा सैकड़ों स्ली-पुत्रोंके संयोग-वियोगका
- **Translation**: 

---

### Verse 8 (Mahabharat 941.8414)
- **Original**: उठकर इसका पाठ कख्ता है, वह सम्पूर्ण महाभाखके माता-पिताओं तथा सैकड़ों स्ली-पुत्रोंके संयोग-वियोगका
- **Translation**: 

---

### Verse 9 (Mahabharat 941.8415)
- **Original**: अध्ययनका फल पाकर पखलह्य परमात्माक्ो प्राप्त कर लेता अनुभव कर चुके हैं, करते हैं और करते रंगे *। अज्ञानी
- **Translation**: 

---

### Verse 10 (Mahabharat 941.8415)
- **Original**: अध्ययनका फल पाकर पखलह्य परमात्माक्ो प्राप्त कर लेता अनुभव कर चुके हैं, करते हैं और करते रंगे *। अज्ञानी
- **Translation**: 

---

### Verse 11 (Mahabharat 941.8416)
- **Original**: है » । जैसे समुद्र और हिमालय पव॑त दोनों ही रत्रोंकी निधि माने पुरुषको प्रतिदिन ह॒र्षके हजारों ओर भयके सैकड़ों अवसर
- **Translation**: 

---

### Verse 12 (Mahabharat 941.8416)
- **Original**: है » । जैसे समुद्र और हिमालय पव॑त दोनों ही रत्रोंकी निधि माने पुरुषको प्रतिदिन ह॒र्षके हजारों ओर भयके सैकड़ों अवसर
- **Translation**: 

---

### Verse 13 (Mahabharat 941.8417)
- **Original**: गये हैं, उसी प्रकार महाभारत भी नाना प्रकारके उपदेशमय प्राप्त होते है; किंतु विद्वार पुसुयके मनपर इनका कोई प्रभाव
- **Translation**: 

---

### Verse 14 (Mahabharat 941.8417)
- **Original**: गये हैं, उसी प्रकार महाभारत भी नाना प्रकारके उपदेशमय प्राप्त होते है; किंतु विद्वार पुसुयके मनपर इनका कोई प्रभाव
- **Translation**: 

---

### Verse 15 (Mahabharat 941.8418)
- **Original**: रक्रोंका भंडार कहलाता है। जो विद्वान औ्ेकृष्णैपायनके द्वार नहीं पड़ता ।। मैं देगों हथ ऊपर उठाकर पुकार-पुकारकर
- **Translation**: 

---

### Verse 16 (Mahabharat 941.8418)
- **Original**: रक्रोंका भंडार कहलाता है। जो विद्वान औ्ेकृष्णैपायनके द्वार नहीं पड़ता ।। मैं देगों हथ ऊपर उठाकर पुकार-पुकारकर
- **Translation**: 

---

### Verse 17 (Mahabharat 941.8419)
- **Original**: प्रसिद्ध किये गये इस महाभारतरूप पम्नम बेदको सुनाता है उसे कह रहा हैं, पर मेरी बात कोई नहीं सुनता। धर्मसे मोक्ष तो
- **Translation**: 

---

### Verse 18 (Mahabharat 941.8419)
- **Original**: प्रसिद्ध किये गये इस महाभारतरूप पम्नम बेदको सुनाता है उसे कह रहा हैं, पर मेरी बात कोई नहीं सुनता। धर्मसे मोक्ष तो
- **Translation**: 

---

### Verse 19 (Mahabharat 941.8420)
- **Original**: अर्थकी प्राप्ति छेती है। जो एकाग्रचित्त होकर इस भास- सिद्ध होता ही है, अर्थ और काम भी सिद्ध होते हैं तो भी लोग
- **Translation**: 

---

### Verse 20 (Mahabharat 941.8420)
- **Original**: अर्थकी प्राप्ति छेती है। जो एकाग्रचित्त होकर इस भास- सिद्ध होता ही है, अर्थ और काम भी सिद्ध होते हैं तो भी लोग
- **Translation**: 

---

