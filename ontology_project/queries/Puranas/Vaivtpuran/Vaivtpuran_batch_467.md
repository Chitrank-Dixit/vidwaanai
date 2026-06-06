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

### Verse 1 (Vaivtpuran 23.3954)
- **Original**: सर्वस्वरूपे विप्राणां मन्त्रसरा परात्पे। सुखदे मोक्षदे देवि प्रसन्ना भव सुन्दरि
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.3955)
- **Original**: विप्रपापेध्यदाहाय ज्वलदग्रिशिखोपमे । क्रह्मतेज:प्रदे देवि प्रसत्ना भव सुन्दरि
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.3956)
- **Original**: कायेन मनसा वाचा यत्पापं कुरुते ट्विज:। तत्‌ ते स्मरणपात्रेण भस्मीभूत॑ भविष्यति
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.3957)
- **Original**: (प्रकृतिखण्ड 23 । 79-84)
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.3958)
- **Original**: 176 + संक्षिप्त श्रह्म॑जैंवर्तपुराण « 648 6 448 6/084:8856:82+0 6 8 9 ]480 4448 ]]05]0 090 854]52]99]] 2 097:5:2]84446। एक वर्ष व्यतीत हो जानेके पश्चात्‌ सत्यपराक्रमी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.3959)
- **Original**: सभी योनियाँ प्राणीको अपने कर्मके अनुसार प्राप्त सत्यवान्‌ अपने पिताकी आज्ञाके अनुसार हर्षपूर्वक
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.3960)
- **Original**: होती हैं। इसमें कुछ भी संशय नहीं है। 'फल और ईंधन लानेके लिये अरण्यमें गये। उनके इस प्रकार सावित्रीसे कहकर यमराज मौन पीछे-पीछे साध्वी सावित्री भी गयी। दैवबश
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.3961)
- **Original**: हो गये। सत्यवान्‌ वृक्षसे गिरे और उनके प्राण प्रयाण कर भगवान्‌ नारायण कहते हैं--मुने ! पतिव्रता गये। मुने ! यमराजने उनके अन्जुछ्च-सदृश जीवात्माको
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.3962)
- **Original**: सावित्रीने यमराजकी बात सुनकर परम भक्तिके सूक्ष्म शरीरके साथ बाँधकर यमपुरीके लिये
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.3963)
- **Original**: साथ उनका स्तवन किया; फिर वह उनसे पूछने प्रस्थान किया। तब साध्वी सावित्री भी उनके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.3964)
- **Original**: लगी। पीछे लग गयी। संयमनीपुरीके स्वामी साधुश्रेष्ठ
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.3965)
- **Original**: . सावित्रीने पूछा--भगवन्‌! कौन कार्य है, यमराजने सुन्दरी सावित्रीको पीछे-पोछे आतो
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.3966)
- **Original**: किस कर्मके प्रभावसे क्‍या होता है, कैसे फलमें देख मधुर वाणीमें कहा। कौन कर्म हेतु है, कौन देह है और कौन देही धर्मराजने कहा--अहो सावित्री! तुम इस
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.3967)
- **Original**: है अथवा संसारमें प्राणी किसकी प्रेरणासे कर्म मानव-देहसे कहाँ जा रही हो? यदि पतिदेवके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.3968)
- **Original**: करता है? ज्ञान, बुद्धि, शरीरधारियोंके प्राण, साथ जानेकी तुम्हारी इच्छा है तो पहले इस [इन्द्रियाँ तथा उनके लक्षण एबं देवता, भोक्ता, शरीरका त्याग कर दो। मर्त्यलोकका प्राणी इस
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.3969)
- **Original**: भोजयिता, भोज, निष्कृति तथा जीव और पाक्थभौतिक शरीरको लेकर मेरे लोकमें नहीं जा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.3970)
- **Original**: परमात्मा-ये सब कौन और क्या हैं? इन सबका सकता। नश्वर व्यक्ति नश्वर लोकमें ही जानेका
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.3971)
- **Original**: परिचय देनेकी कृपा कीजिये। अधिकारी है। साध्वि! तुम्हारा पति सत्यवान्‌ु
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.3972)
- **Original**: धर्मराज बोले--साध्वी सावित्री! कर्म दो भारतवर्षमें आया था। उसकी आयु अब पूर्ण
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.3973)
- **Original**: प्रकारके हैं-शुभ और अशुभ। वेदोक्त कर्म शुभ हो चुकी, अतएव अपने किये हुए कर्मका फल
- **Translation**: 

---

