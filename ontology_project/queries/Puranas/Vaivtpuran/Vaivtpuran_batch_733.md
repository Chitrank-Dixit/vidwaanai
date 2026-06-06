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

### Verse 1 (Vaivtpuran 543.12974)
- **Original**: ही देवराज इन्द्र, काल, मृत्यु तथा यम हैं। वे वस्त्रके स्थानमें व्याप्रचर्म धारण किये,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12975)
- **Original**: मृत्युझ्य होनेके कारण मृत्युकी भी मृत्यु, कालके हड्डियोंकी माला पहने तथा अज्जोंमें विभूति रमाये
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12976)
- **Original**: भी काल तथा यमके भी यम हैं। वेद, बेदकर्ता बड़ी शोभा पाते थे। दिगम्बर वेष, पाँच मुख
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12977)
- **Original**: तथा बेद-बेदाड्रोंके पारज्जगत विद्वान भी आप ही
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12978)
- **Original**: + भ्रीकृष्णजन्मखण्ड « 567 5कऊ% 66444 444 8# 8 #% 44% # 8 # #% # ऋ $# 4 # # 88 8 8 5 # # ## #% # # 4 ऋ 4 ऋ कक # # ## 44 कक कक कक हैं। आप ही विद्वानोंक जनक, विद्वान्‌ तथा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12979)
- **Original**: पाठ करे तो पुत्र पाता है। भार्याहीनको सुशीला दिद्वानोंके गुरु हैं। आप ही मन्त्र, जप, तप और
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12980)
- **Original**: तथा परम मनोहारिणी भार्या प्राप्त होती है। वह उनके फलदाता हैं। आप ही वाक्‌ और आप
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12981)
- **Original**: चिरकालसे खोयी हुई वस्तुकों सहसा तथा ही वाणीकी अधिष्ठात्री देवी हैं। आप ही उसके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12982)
- **Original**: अवश्य पा लेता है। राज्यप्रष्ट पुरुष भगवान्‌ स्रष्टा और गुरु हैं। अहो! सरस्वतीका बीज अद्भुत
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12983)
- **Original**: शंकरके प्रसादसे पुनः राज्यको प्राप्त कर लेता है। यहाँ कौन आपकी स्तुति कर सकता है?! है। कारागार, श्मशान और शत्रु-संकटमें पड़नेपर ऐसा कहकर गिरिराज हिमालय उनके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12984)
- **Original**: तथा अत्यन्त जलसे भरे गम्भीर जलाशयमें नाव चरणकमलोंकों धारण करके खड़े रहे। भगवान्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12985)
- **Original**: टूट जानेपर, विष खा लेनेपर, महाभयंकर शिव वृषभपर बैठे हुए शैलराजको प्रबोध देते
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12986)
- **Original**: संग्रामके बीच फैंस जानेपर तथा हिंसक जन्तुओंसे रहे। जो मनुष्य तीनों संध्याओंके समय इस परम
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12987)
- **Original**: घिर जानेपर इस स्तुतिका पाठ करके मनुष्य पुण्यमय स्तोत्रका पाठ करता है, वह भवसागरमें
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12988)
- **Original**: भगवान्‌ शंकरकी कृपासे समस्त भयोंसे मुक्त हो रहकर भी समस्त पापों तथा भयोंसे मुक्त हो
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12989)
- **Original**: जाता है। जाता है। पुत्रहीन मनुष्य यदि एक मासतक इसका (अध्याय 37-38) “39290... गिरिराज हिमवान्‌द्वारा गणोंसहित शिवका सत्कार, मेनाको शिवके अलौकिक सौन्दर्यके दर्शन, पार्वतीद्वारा शिवकी परिक्रमा, शिवका उन्हें आशीर्वाद, शिवाद्वारा शिवका षोडशोपचार-पूजन, शंकरद्वारा कामदेवका दहन तथा पार्वतीको तपस्याद्वारा शिवकी प्राप्ति भगवान्‌ श्रीकृष्ण कहते हैं--प्रिये! इस
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12990)
- **Original**: छोड़कर नूतन यौवन धारण करते थे और प्रकार स्तुति करके गिरिराज हिमवान्‌ नगरसे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12991)
- **Original**: अत्यन्त सुन्दर रमणीय रूप हो युवतियोंके चित्त दूर निवास करनेवाले भगवान्‌ शंकरसे कुछ ही
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12992)
- **Original**: चुरा रहे थे। वे कामातुरा कामिनियोंकों कामदेवके दूरीपर उनकी आज्ञा ले स्वयं भी ठहर गये।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12993)
- **Original**: समान जान पड़ते थे। सतियोंको औरस पुत्रके उन्होंने भक्तिपूर्वक भगवान्‌कों मधुपर्क आदि
- **Translation**: 

---

