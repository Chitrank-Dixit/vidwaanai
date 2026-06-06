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

### Verse 1 (Vaivtpuran 53.4954)
- **Original**: हुआ एक पात्र हो, जिसकी गहराई चार अंगुलकौ विस्तार एक करोड़ योजन है तथा लंबाई उससे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 53.4955)
- **Original**: हो। उसमें एक-एक माशे सोनेके बने हुए चार-
- **Translation**: 

---

### Verse 3 (Vaivtpuran 53.4956)
- **Original**: * प्रकृतिखण्ड « 263 666###£#8##&## 5 4 #8 4 44% 4 # 45 $ 5 5 # 5555 55 ऋ अर क्क 5 5 5 ऋ कक ऊशरक्क कककक 85 शर कक डक डक चार अंगुल लंबे चार कौलोंसे छेद कर दिये
- **Translation**: 

---

### Verse 4 (Vaivtpuran 53.4957)
- **Original**: बर्षसे सत्रह लाख अट्टाईस हजार बताया है। जायेँ। फिर उस पात्रको जलके ऊपर रख दिया
- **Translation**: 

---

### Verse 5 (Vaivtpuran 53.4958)
- **Original**: इसी तरह त्रेताका कालमान बारह लाख जाय। उन छिद्रोंसे पानी आकर जितनी देरमें वह
- **Translation**: 

---

### Verse 6 (Vaivtpuran 53.4959)
- **Original**: छियानबे हजार मानव-वर्ष है। द्वापका आठ पात्र भर दे, उतने समयकों एक दण्ड कहते
- **Translation**: 

---

### Verse 7 (Vaivtpuran 53.4960)
- **Original**: लाख चौसठ हजार तथा कलियुगका चार लाख हैं। दो दण्डका एक मुहूर्त और चार मुहूर्तोंका
- **Translation**: 

---

### Verse 8 (Vaivtpuran 53.4961)
- **Original**: बत्तीस हजार मानव-वर्ष है। एक प्रहर होता है। आठ प्रहरोंसे एक दिन-। जैसे सात वार, सोलह तिथियाँ, दिन-रात, शातकी पूर्ति होती है। पंद्रह दिन-रातको एक [दो पक्ष, बारह मास और वर्ष चक्रवत्‌ घूमते पक्ष कहते हैं। दो पक्षोंका एक मास और बारह
- **Translation**: 

---

### Verse 9 (Vaivtpuran 53.4962)
- **Original**: रहते हैं, उसी प्रकार चारों युगोंका चक्र भी सदा मासका एक वर्ष होता है। मनुष्योंके एक मासमें
- **Translation**: 

---

### Verse 10 (Vaivtpuran 53.4963)
- **Original**: ही चलता रहता है। राजेन्द्र! जैसे युग परिवर्तित जितना समय व्यतीत होता है, वह पितरोंका एक
- **Translation**: 

---

### Verse 11 (Vaivtpuran 53.4964)
- **Original**: होते हैं, उसी प्रकार मन्वन्तर भी। इकहत्तर दिव्य दिन-रात है। कृष्णपक्षमें उनका दिन कहा गया
- **Translation**: 

---

### Verse 12 (Vaivtpuran 53.4965)
- **Original**: युगोंका एक मन्वन्तर होता है। इसी क्रमसे चौदह है और शुक्लपक्षमें रात्रि। मनुष्योंके एक वर्षमें मनु भ्रमण करते रहते हैं। देवताओंके एक दिन-रातकी पूर्ति होती है। नरेश्वर! मैंने भगवान्‌ शंकरके मुखसे धर्मात्मा उत्तरायणमें उनका दिन होता है और दक्षिणायनमें
- **Translation**: 

---

### Verse 13 (Vaivtpuran 53.4966)
- **Original**: मनुओंका जो आख्यान सुना है, वह बता रहा रात्रि। नरेश्वर! मनुष्य आदिकी अवस्था युग एवं
- **Translation**: 

---

### Verse 14 (Vaivtpuran 53.4967)
- **Original**: हूँ। तुम मुझसे सुनो। आदिमनु ब्रह्माजीके पुत्र कर्मके अनुरूप होती है। अब प्रकृति, प्राकृत
- **Translation**: 

---

### Verse 15 (Vaivtpuran 53.4968)
- **Original**: हैं। इसलिये उन्हें स्वायम्भुव मनु कहा गया है। पदार्थ एवं ब्रह्मा आदिको आयुका परिमाण सुनों।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 53.4969)
- **Original**: उनकी पत्नी पतिव्रता शतरूपा हैं। स्वायम्भुव मनु सत्ययुग, त्रेता, द्वापप और कलियुग-इन चारोंको
- **Translation**: 

---

### Verse 17 (Vaivtpuran 53.4970)
- **Original**: धर्मात्माओंमें वरिष्ठ और मनुओंमें गरिष्ठ हैं। वे एक चतुर्युग कहते हैं। इनकी काल-संख्या बारह
- **Translation**: 

---

### Verse 18 (Vaivtpuran 53.4971)
- **Original**: तुम्हारे प्रपितामह लगते हैं। उन्होंने भगवान्‌ हजार दिव्य वर्ष है। सावधान होकर सुनो,
- **Translation**: 

---

### Verse 19 (Vaivtpuran 53.4972)
- **Original**: शंकरका शिष्यत्व ग्रहण किया है। वे विष्णुव्रतका सत्ययुग आदिका कालमान क्रमश: चार, तोन, पालन करनेवाले जीवन्मुक्त एवं महाज्ञानी थे। दो और एक दिव्य वर्ष है। उनकी संध्या और
- **Translation**: 

---

### Verse 20 (Vaivtpuran 53.4973)
- **Original**: उन्होंने भगवान्‌ शंकरकी आज्ञासे भगवान्‌ विष्णुकी संध्यांशकाल दो हजार दिव्य वर्षोके बताये गये
- **Translation**: 

---

