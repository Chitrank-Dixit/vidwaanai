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

### Verse 1 (Vaivtpuran 543.12954)
- **Original**: ऋषि--सब उनके सामने खड़े थे। हिमालयने मेरे ही लिये आये हैं। यही जानकर उन्होंने
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12955)
- **Original**: इन सबको मस्तक झुकाकर भगवान्‌ शिवको विविध दिव्य बस्त्रों तथा दिव्य रत्नालंकारों
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12956)
- **Original**: प्रणाम किया और पृथ्वीपर माथा टेक दण्डकी एवं मालाओंके द्वारा अपने सम्पूर्ण अद्भोंको
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12957)
- **Original**: भाँति पड़कर दोनों हाथ जोड़ लिये। इसके बाद सुसज्जित किया। तत्पश्चात्‌ अपने अनुपम रूपको
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12958)
- **Original**: बड़ी भक्ति-भावनासे शिवके चरणकमल पकड़कर देखकर पार्बतीने मन-ही-मन शंकरजीका ध्यान
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12959)
- **Original**: पर्वतराजने नमस्कार किया और नेन्रोंसे आँसू किया। विशेषतः स्वामीके चरणकमलोंका वे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12960)
- **Original**: बहाते पुलकित-शरीर हो धर्मके दिये हुए स्तोत्रसे चिन्तन करने लगीं। उस समय शिवको छोड़कर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12961)
- **Original**: परमेश्वर शिवकी स्तुति आरम्भ की। पिता, माता, बन्धु-बान्धव, साध्वी वर्ग तथा
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12962)
- **Original**: । हिमालय बोले--भगवन्‌! आप ही सृष्टिकर्ता सहोदर भाई किसीको भी उन्होंने अपने मनमें
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12963)
- **Original**: ब्रह्मा हैं। आप ही जगत्पालक विष्णु हैं। आप स्थान नहीं दिया। ही सबका संहार करनेवाले अनन्त हैं और आप इधर गिरिराज हिमालयने वहाँ जाकर
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12964)
- **Original**: ही कल्याणदाता शिव हैं। आप गुणातीत ईश्वर, भगवान्‌ चन्द्रशेखरके दर्शन किये। वे गड्भाजीके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12965)
- **Original**: सनातन ज्योतिःस्वरूप हैं। प्रकृति और उसके रमणीय तटसे ऊपरको आ रहे थे। उनके मुखपर
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12966)
- **Original**: ईश्वर हैं। प्राकृत पदार्थरूप होते हुए भी प्रकृतिसे मन्द मुस्कानको प्रभा फैल रहो थी। वे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12967)
- **Original**: परे हैं। भक्तोंके ध्यान करनेके लिये आप अनेक संस्कारयुक्त माला धारण किये मेरे नामका जप
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12968)
- **Original**: रूप धारण करते हैं। जिन रूपोंमें जिसकी प्रीति कर रहे थे। उनके सिरपर सुनहरी प्रभासे युक्त
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12969)
- **Original**: है, उसके लिये आप वे ही रूप धारण करते जटाराशि विराजमान थी। वे वृषभकी पीठपर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12970)
- **Original**: हैं। आप ही सृष्टिके जन्मदाता सूर्य हैं। समस्त बैठकर हाथमें त्रिशूल लिये सब प्रकारके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12971)
- **Original**: तेजोंके आधार हैं। आप ही शीतल किरणोंसे आभूषणोंसे सुशोभित थे। सर्पका ही यज्ञोपवीत
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12972)
- **Original**: सदा शस्योंका पालन करनेवाले सोम हैं। आप पहने सर्पमय आभूषणोंसे विभूषित थे। उनकी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12973)
- **Original**: ही वायु, वरुण और सर्वदाहक अग्नि हैं। आप अद्जभकान्ति शुद्ध स्फटिकके समान उज्बल थी,
- **Translation**: 

---

