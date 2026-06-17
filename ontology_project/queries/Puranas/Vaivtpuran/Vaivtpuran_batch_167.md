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

### Verse 1 (Vaivtpuran 12.6434)
- **Original**: हो सकता है। पूर्वजन्मार्जित कर्मफलके बिना पाते हैं; जो पीताम्बरधारी, परात्पर, जगत्‌के
- **Translation**: 

---

### Verse 2 (Vaivtpuran 12.6435)
- **Original**: सिंह मक्खीको भी मारनेमें असमर्थ है और स्वामी, निषेकका खण्डन करनेमें समर्थ, निषेकको
- **Translation**: 

---

### Verse 3 (Vaivtpuran 12.6436)
- **Original**: मच्छर अपने प्राक्तन कर्मके बलसे हाथीको भी उत्पन्न करनेवाले, सर्वव्यापक, निषेकके भोगके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 12.6437)
- **Original**: मार डालनेकी शक्ति रखता है। सुख-दुःख, भय- दाता और भोगके निस्तारके कारणस्वरूप हैं तथा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 12.6438)
- **Original**: शोक, आनन्द--ये कर्मके ही फल हैं। इनमें सुख जो गरुड़पर आरूढ़ हो मुस्कराते हुए सुदर्शनचक्रको
- **Translation**: 

---

### Verse 6 (Vaivtpuran 12.6439)
- **Original**: और हर्ष उत्तम कर्मके और अन्य पापकर्मके घुमा रहे हैं-उन परमेश्वका उसने स्तवन
- **Translation**: 

---

### Verse 7 (Vaivtpuran 12.6440)
- **Original**: परिणाम हैं*। कर्मका भोग शुभ-अशुभ-रूपसे किया। विप्रवर! उसकी स्तुतिसे प्रसन्न होकर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 12.6441)
- **Original**: इहलोक अथवा परलोकमें प्राप्त होता है, परंतु भगवान्‌ने उसे बर दिया और दूसरे गजका
- **Translation**: 

---

### Verse 9 (Vaivtpuran 12.6442)
- **Original**: कर्मोपार्जनके योग्य पुण्यक्षेत्र भारत ही है। स्वयं मस्तक काटकर इसके धड़से जोड़ दिया।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 12.6443)
- **Original**: श्रीकृष्ण कर्मके फलदाता, विधिके विधाता, फिर उन ब्रह्मवेत्ताने ब्रह्मज्ञाससे उसे जीवित कर
- **Translation**: 

---

### Verse 11 (Vaivtpuran 12.6444)
- **Original**: मृत्युके भी मृत्यु, कालके काल, निषेकके *सुखं दुःखं भय॑ शोकमानन्दं कर्मण: फलम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 12.6445)
- **Original**: सुकर्मण: सुखं हर्षमितें पापकर्मण:
- **Translation**: 

---

### Verse 13 (Vaivtpuran 12.6446)
- **Original**: (गणपतिखण्ड 12। 27)
- **Translation**: 

---

### Verse 14 (Vaivtpuran 12.6447)
- **Original**: 'गैणेपत्तिखण्ड + 321 अंक ऋअ अंक अ डक कक अऊ कक अऊ अं कह क अर ऋअ अंक धक क
- **Translation**: 

---

### Verse 15 (Vaivtpuran 12.6448)
- **Original**: अ कक अ अं 445 & 88 9& 8 88 555 ## 8 # 8 95 888. निषेककर्ता, संहतकि भी संहारक, पालकके भी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 12.6449)
- **Original**: दिया। फिर क्रमश: देवियोंने तथा उपस्थित सभी पालक, परात्पर, परिपूर्णतम गोलोकनाथ हैं। हम
- **Translation**: 

---

### Verse 17 (Vaivtpuran 12.6450)
- **Original**: देवताओं, मुनियों, पर्वतों, गन्धवोँ और समस्त ब्रह्मा, विष्णु और महेश्वर जिस पुरुषकी कलाएँ
- **Translation**: 

---

### Verse 18 (Vaivtpuran 12.6451)
- **Original**: महिलाओंने यथोचितरूपसे रज्न प्रदान किये। उस हैं, महाविराट्‌ जिसका अंश है, जिसके रोम-
- **Translation**: 

---

### Verse 19 (Vaivtpuran 12.6452)
- **Original**: समय महादेवजीका हृदय अत्यन्त हर्षमग्न था। वे बिवरमें जगत्‌ भरे हैं, कोई-कोई उनके कलांश
- **Translation**: 

---

### Verse 20 (Vaivtpuran 12.6453)
- **Original**: विष्णुका स्तवन करने लगे। नारद! वहाँ मरकर हैं और कोई-कोई कलांशके भी अंश हैं और
- **Translation**: 

---

