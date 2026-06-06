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

### Verse 1 (Vaivtpuran 53.4994)
- **Original**: जाती है, तब वे पुनः सृष्टिका कार्य प्रारम्भ करते स्वायम्भुव मनुके समान ही महान धर्मिष्ठ एवं
- **Translation**: 

---

### Verse 2 (Vaivtpuran 53.4995)
- **Original**: हैं। ब्रह्माकी रात्रिमें जो लोकोंका संहार होता दानी रहे हैं। दो अन्य मनु राजा प्रियत्नरतके पुत्र
- **Translation**: 

---

### Verse 3 (Vaivtpuran 53.4996)
- **Original**: है, उसे 'श्लुद्र प्रलय” कहते हैं। उसमें देवता, तथा धर्मात्माओमें श्रेष्ठ हैं। उनके नाम हैं--तापस
- **Translation**: 

---

### Verse 4 (Vaivtpuran 53.4997)
- **Original**: मनु और मनुष्य आदि दग्ध हो जाते हैं। इस और उत्तम। दोनों ही वैष्णव हैं तथा क्रमश:
- **Translation**: 

---

### Verse 5 (Vaivtpuran 53.4998)
- **Original**: प्रकार जब त्रह्माके तीस दिन-रात व्यतीत हो तीसरे और चौथे मनुके पदपर प्रतिष्ठित हैं। वे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 53.4999)
- **Original**: जाते हैं, तब उनका एक मास पूरा होता है। दोनों भी भगवान्‌ शंकरके शिष्य हैं तथा वैसे ही बारह महीनोंका उनका एक वर्ष होता श्रीकृष्णकी भक्तिमें तत्पर रहते हैं। धर्मात्माओंमें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 53.5000)
- **Original**: है। इस प्रकार त्रह्माके पंद्रह वर्ष व्यतीत होनेपर श्रेष्ठ रैवत पाँचवें मनु हैं। चाक्षुपषको छठा मनु
- **Translation**: 

---

### Verse 8 (Vaivtpuran 53.5001)
- **Original**: एक प्रलय होता है, जिसे वेदॉमें 'दैनन्दिन प्रलय' जानना चाहिये। वे भी विष्णुभक्तिमें तत्पर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 53.5002)
- **Original**: कहा गया है। प्राचीन वेदज्ञोंने उसीको 'मोहरात्रि' रहनेवाले हैं। सूर्यपुत्र श्राद्धदेव जो विष्णुके भक्त
- **Translation**: 

---

### Verse 10 (Vaivtpuran 53.5003)
- **Original**: की संज्ञा दी है। उसमें चन्द्रमा, सूर्य आदि; हैं, सातवें मनु कहे गये हैं (इन्हींको वैवस्वत
- **Translation**: 

---

### Verse 11 (Vaivtpuran 53.5004)
- **Original**: दिक्पाल, आदित्य, बसु, रुद्र मनु, इन्द्र, मानव, मनु कहते हैं)। सूर्यके दूसरे वैष्णव पुत्र सावर्णि
- **Translation**: 

---

### Verse 12 (Vaivtpuran 53.5005)
- **Original**: ऋषि, मुनि, गन्धर्व तथा राक्षस आदि; मार्कण्डेय, आठवें मनु हैं। विष्णुत्रतपरायण दक्षसावर्णि नवें
- **Translation**: 

---

### Verse 13 (Vaivtpuran 53.5006)
- **Original**: लोमश और पेचक आदि चिरजीवी; राजा मनु हैं। ब्रह्मज्ञानविशारद ब्रह्मसावर्णि दसवें मनु
- **Translation**: 

---

### Verse 14 (Vaivtpuran 53.5007)
- **Original**: इन्द्रद्युप्न, अकूपार नामक कच्छप तथा नाडीजंघ हैं। ग्यारहवें मनुका नाम धर्मसावर्णि है। वे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 53.5008)
- **Original**: नामक बक--ये सब-के-सब नष्ट हो जाते हैं। धर्मिष्ट, वरिष्ठ तथा सदा ही वैष्णवोंके व्रतका
- **Translation**: 

---

### Verse 16 (Vaivtpuran 53.5009)
- **Original**: ब्रह्मलोकके नीचेके सब लोक तथा नागोंके स्थान पालन करनेवाले हैं। ज्ञानी रुद्रसावर्णि बारहवें
- **Translation**: 

---

### Verse 17 (Vaivtpuran 53.5010)
- **Original**: भी विनाशको प्राप्त हो जाते हैं। ऐसे समयमें
- **Translation**: 

---

### Verse 18 (Vaivtpuran 55.5162)
- **Original**: के प्रकृतिखण्ड + 271 8 ।।2।।2
- **Translation**: 

---

### Verse 19 (Vaivtpuran 55.5163)
- **Original**: ]।।।।4444।।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 55.5164)
- **Original**: 4। 40 9334444534-53344&>&&2##नन नम %% कक ### 55% 'फूल चढ़ावे। पुनः ध्यानके पश्चात्‌ सोलह उपचार (4 ) अर्घ्य अर्पित करे। आसन, बसन, पाद्य, अर्घ्य, गन्ध,
- **Translation**: 

---

