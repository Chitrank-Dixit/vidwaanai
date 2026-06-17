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

### Verse 1 (Mahabharat 0.4591)
- **Original**: भात्यकि और वृषसेनमें युद्ध छिड़ा हुआ था। सात्यकिने तीन की । तब तो भीमसेनने दूसरा धनुष हाथमें लिया और उसकी
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4591)
- **Original**: भात्यकि और वृषसेनमें युद्ध छिड़ा हुआ था। सात्यकिने तीन की । तब तो भीमसेनने दूसरा धनुष हाथमें लिया और उसकी
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4592)
- **Original**: णोंसे वृषसेनके सारधिको मारकर एक भालेसे उसका भरकर उन्होंने उसको दस बराणोंसे बींध डाला । इतना ही नहीं, तमामकर एक बाणसे ध्वजा काट दी और तीन सायकोसे भीमने कर्णपर भी सत्तर तीखे बाणोंका प्रहार किया वृषसेनकी छातीमें घाव किया। उस प्रहारसे वृषसेनका सारा झरीर सुन्न हो गया। एक क्षणतक बेहोश रहनेके बाद वह उठा धर लत्सा-- आउट. -> ने दा ह छः 37
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4592)
- **Original**: णोंसे वृषसेनके सारधिको मारकर एक भालेसे उसका भरकर उन्होंने उसको दस बराणोंसे बींध डाला । इतना ही नहीं, तमामकर एक बाणसे ध्वजा काट दी और तीन सायकोसे भीमने कर्णपर भी सत्तर तीखे बाणोंका प्रहार किया वृषसेनकी छातीमें घाव किया। उस प्रहारसे वृषसेनका सारा झरीर सुन्न हो गया। एक क्षणतक बेहोश रहनेके बाद वह उठा धर लत्सा-- आउट. -> ने दा ह छः 37
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4593)
- **Original**: था कि सात्यकिने दस बाणोंसे उसकी डाल-सलबारके 51 486 ट््यक 8 - कर दिये 2 66.0)
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4593)
- **Original**: था कि सात्यकिने दस बाणोंसे उसकी डाल-सलबारके 51 486 ट््यक 8 - कर दिये 2 66.0)
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4594)
- **Original**: ! 0 सका कक रा] आवक लग 5-5.
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4594)
- **Original**: ! 0 सका कक रा] आवक लग 5-5.
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4595)
- **Original**: 585. :< ; ध्स् द् आफ नर है )
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4595)
- **Original**: 585. :< ; ध्स् द् आफ नर है )
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4596)
- **Original**: थ् ई ई। 4 रे ड़ डे
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4596)
- **Original**: थ् ई ई। 4 रे ड़ डे
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4597)
- **Original**: डरे संक्षिप्त महाभारत [ कर्णपर्व तदनन्तर, कर्णको यृष्टशुप्रने दस; द्रौपदीके पुत्रोने तिहत्तर,
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4597)
- **Original**: डरे संक्षिप्त महाभारत [ कर्णपर्व तदनन्तर, कर्णको यृष्टशुप्रने दस; द्रौपदीके पुत्रोने तिहत्तर,
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4598)
- **Original**: बाणोंकी बौछाससे उन महान्‌ धनुर्धरोंका मानमर्दन करता हुआ सात्यकिने सात, भीमसेनने चौंसठ, सहदेवने सात, नकुछने
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4598)
- **Original**: बाणोंकी बौछाससे उन महान्‌ धनुर्धरोंका मानमर्दन करता हुआ सात्यकिने सात, भीमसेनने चौंसठ, सहदेवने सात, नकुछने
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4599)
- **Original**: कर्ण हाथियोंकी सेनामें बेरोक-टोक घुस गया। फिर तीस, झतानीकने सात, झिखण्डीने दस, धर्मराजने सौ तथा
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4599)
- **Original**: कर्ण हाथियोंकी सेनामें बेरोक-टोक घुस गया। फिर तीस, झतानीकने सात, झिखण्डीने दस, धर्मराजने सौ तथा
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4600)
- **Original**: चेदिवीरोंक तीस रथियोंका सफाया करके उसने राजा अन्य बीरोने भी बहुत-सें बाण मारे। सब ल्परेगोने सूतपुत्र॒को
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4600)
- **Original**: चेदिवीरोंक तीस रथियोंका सफाया करके उसने राजा अन्य बीरोने भी बहुत-सें बाण मारे। सब ल्परेगोने सूतपुत्र॒को
- **Translation**: 

---

