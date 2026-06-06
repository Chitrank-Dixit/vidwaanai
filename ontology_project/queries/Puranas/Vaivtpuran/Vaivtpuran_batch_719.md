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

### Verse 1 (Vaivtpuran 543.12694)
- **Original**: अधिपति माना। लज्जासे उनका सिर झुक गया कुशल-समाचार पूछा। उन सब ब्रह्माओंको
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12695)
- **Original**: और वे भगवान्‌ विष्णुके चरणोंमें पड़ गये। तब देखकर अपनेको विष्णु-तुल्य माननेवाले चतुर्मुख
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12696)
- **Original**: भगवान्‌ने उनसे पूछा--' ब्रह्मन्‌! बोलो, इस समय ब्रह्माका घमंड चूर-चूर हो गया। इसके बाद
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12697)
- **Original**: तुमने स्वप्नकी भाँति यह क्या देखा है।' उनका श्रीहरिने विभिन्न ब्रह्माण्डोंमें रहनेवाले अन्यान्य प्रश्न सुनकर ब्रह्मा बोले--'प्रभो! भूत, वर्तमान ब्रह्माओंके भी दर्शन कराये। उन्हें देखकर चतुर्मुख
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12698)
- **Original**: और भविष्य--सारा जगत्‌ आपकी मायासे ही ब्रह्मा मृतक-तुल्य हो गये। उस समय भगवानूने
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12699)
- **Original**: उत्पन्न हुआ है।' यों कह चतुर्भुज ब्रह्मा वैकुण्ठकी कहा--'मुझ नारायणके शरीरमें जितने रोम हैं,
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12700)
- **Original**: सभामें लजाका अनुभव करते हुए चुप हो गये। उतने ही ब्रह्माण्ड और उनके उतने हो ब्रह्मा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12701)
- **Original**: तब सर्वान्तर्यामी भगवान्‌ श्रीहरिने उनके शाप- विद्यमान हैं।' यह सुनकर वे सभी आगत्तुक
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12702)
- **Original**: निवारणका उपाय किया। ब्रह्मा नारायणको प्रणाम करके शीघ्र ही अपने-
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12703)
- **Original**: (अध्याय 31-33) 8+0+म्दापथए->>> गड्ढकी उत्पत्ति तथा महिमा श्रीकृष्ण कहते हैं-प्रिये! इसी बीचमें
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12704)
- **Original**: शिवको प्रणाम किया। तदनन्तर स्वर-थन्त्र लिये भगवान्‌ शंकर वहाँ उपस्थित हुए। उनके मुखपर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12705)
- **Original**: भगवान्‌ शंकरने सुमधुर तालस्वरके साथ संगीत मुस्कराहट थी। वे सारे अज्जॉमें विभूति लगाये
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12706)
- **Original**: आरम्भ किया। प्रिये! उसमें हम दोनोंके गुणों वृषभराज नन्दिकेश्वरकी पीठपर बैठे थे। व्याप्रचर्मका
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12707)
- **Original**: तथा राससम्बन्धी सुन्दर पदोंका गान होने लगा। वस्त्र, सर्पमय यज्ञोपवीत, सिरपर सुनहरे रंगकी ः जटाका भार, ललाटमें अर्धचन्र, हाथोंमें त्रिशूल, पट्टिश तथा उत्तम खट्वाड़ धारण किये, श्रेष्ठ
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12708)
- **Original**: ; शिव शीघ्र ही वाहनसे उतरे और भक्तिभावसे मस्तक झुका कमलाकान्तकों प्रणाम करके उनके बामभागमें बैठे। फिर इन्द्र आदि समस्त देवता, मुनि, आदित्य, वसु, रुद्र, मनु, सिद्ध और चारण 2 किले 2 वहाँ पधारे। उन सबने पुरुषोत्तमकी स्तुति की।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12709)
- **Original**: 9 पटक जपआ उस समय उनके सारे अड्भ पुलकित हो रहे थे। <>/43076< फिर समस्त देवताओंने सिर झुकाकर भगवान्‌ मनको मोह लेनेवाले सामयिक राग,' कण्ठकी 1- संगीतमें घड्ज आदि स्वरों, उनके वर्णों और अड्जॉसे युक्त वह ध्वनि जो किसी विशिष्ट तालमें बैठायी हुई हो और जो मनोरञ्ञनके लिये गायी जाती हो। संगीत-शास्त्रके भारतीय आचार्योंने छः राग माने हैं; परंतु इन 717 शक्कर 1302 आर आक साफ 45-22
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12710)
- **Original**: * श्रीकृष्णजन्मखण्ड « ] कक #
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12711)
- **Original**: ################## #$ कक # 5 कक अऋऋ्ऋऋ 7 # 6 #%# ## 94% # 6
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12712)
- **Original**: 6##%## 68% ## एकतानता, एक मनोहर मान, गुरलपुके क्रमसे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12713)
- **Original**: हो गये। प्राणेश्वरि! उस समय बैकुण्ठधामको पद-भेद-विराम, अतिदीर्घ तथा मधुर
- **Translation**: 

---

