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

### Verse 1 (Vaivtpuran 543.13034)
- **Original**: र्मणीय भूषण, सुवर्णमढ़ी सींगवाली दुर्लभ शिवने आशीर्वाद देते हुए कहा--'सुन्दरि!
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13035)
- **Original**: कामधेनु, स्नानोपयोगी द्रव्य, तीर्थजल तथा तुम्हें अनन्य प्रेमी, गुणवान्‌, अमर, ज्ञानिशिरोमणि
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13036)
- **Original**: मनोहर ताम्बूल भी क्रमश: अर्पित किये। इस
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13037)
- **Original**: + भ्रीकृष्णजन्मखण्ड * 569 ]]
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13038)
- **Original**: 2 8 । 4
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13039)
- **Original**: प्रकार षोडशोपचार चढ़ाकर पार्वतीने बारंबार प्रणाम किया। यह उनका नित्यका नियम बन गया। वे प्रतिदिन भक्तिभावसे शिवकी पूजा करके पिताके घर लौट जाया करती थीं। अप्सराओंके मुखसे इन्द्रने यह सुना कि पड़ती थी। आकाशमें ऊपर उठकर चक्कर काटती हुई वह आग पृथ्बीपर उतर आयी और चारों ओर चक्कर देकर कामदेवपर टूट पड़ी। भगवान्‌ शंकरके कोपसे कामदेव एक ही क्षणमें भस्म हो गये। यह देख सब देवता विषादमें डूब गये भगवान्‌ महेश्वर पार्वतीदेवीके प्रति अनुरक्त हैं। और पार्वतीने भी सिर नीचा कर लिया। तदनन्तर यह समाचार सुनकर इन्द्र हर्षसे नाचने लगे।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13040)
- **Original**: रति भगवान्‌ शिवके सामने बहुत विलाप करने उन्होंने बड़ी उतावलीके साथ दूत भेजकर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13041)
- **Original**: लगी। भयसे काँपते हुए समस्त देवताओंने कामदेवको बुलवाया। इन्द्रकी आज्ञासे कामदेव
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13042)
- **Original**: शिवका स्तवन किया। इसके बाद वे बार-बार अमरावतीपुरीमें गये। तब इन्द्रने उन्हें शीघ्र ही रोते हुए रतिसे बोले-'माँ! पतिके शरीरका उस स्थानपर भेजा, जहाँ शिवा और शिव
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13043)
- **Original**: थोड़ा-सा भस्म लेकर उसकी रक्षा करो और विद्यमान थे। पश्चनाण कामने अपने पाँचों
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13044)
- **Original**: भय छोड़ो । हम लोग उन्हें जीवित करायेंगे। तुम बाणोंकों साथ ले उस स्थानको प्रस्थान किया,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13045)
- **Original**: पुनः अपने प्रियतमको प्राप्त करोगी; परंतु जब जहाँ शक्तिसहित शिव विराजमान थे। वहाँ
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13046)
- **Original**: भगवान्‌ शंकरका क्रोध दूर हो जायगा और उनकी पहुँचकर मदनने देखा, भगवान्‌ शिव शिवाके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13047)
- **Original**: प्रसन्नताका समय होगा, तभी यह कार्य सम्भव साथ विद्यमान हैं। उनके मुख और नेत्र प्रसन्न
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13048)
- **Original**: हो सकेगा।' दिखायी देते हैं। वे त्रिभुवनकान्त एवं शान्त हैं।। . रतिका विलाप देखकर पार्वती मू्च्छित हो उन्हें देखकर कामदेव बाणसहित धनुष हाथमें
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13049)
- **Original**: गर्यीं और उन अतीन्द्रिय गुणातीत चन्द्रशेखरकी लिये आकाशमें खड़ा हो गया। उसने बड़े हर्षके
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13050)
- **Original**: स्तुति करने लगीं। तब भगवान्‌ शिव रोती हुई साथ अपने अमोघ एवं अनिवार्य अस्त्रका
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13051)
- **Original**: पार्वतीकों वहीं छोड़कर अपने स्थानको चले गये। शंकरपर प्रयोग किया; परंतु बह अमोघ अस्त्र
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13052)
- **Original**: फिर तो उसी क्षण पार्वतीका सारा अभिमान चूर भी परमात्मा शंकरपर व्यर्थ हो गया। जैसे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13053)
- **Original**: हो गया। गिरिराजनन्दिनीनी अपने रूप और आकाश निरलेप होता है, उसी तरह निर्लिप्त
- **Translation**: 

---

