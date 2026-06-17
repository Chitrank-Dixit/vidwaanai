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

### Verse 1 (Vaivtpuran 28.7278)
- **Original**: प्रभाशाली थे। उनका मुख प्रसन्न था, जिसपर द्वारपाल नियुक्त थे, जिन्हें परशुरामने देखा। उनकी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 28.7279)
- **Original**: मन्द मुस्कानकी अद्भुत छटा बिखर रही थी, वे आकृति बेडौल थी, दाँत और मुख बड़े विकराल
- **Translation**: 

---

### Verse 3 (Vaivtpuran 28.7280)
- **Original**: भक्तोंपर अनुग्रह करनेके लिये अधीर हो रहे थे। थे। तीन बड़े-बड़े नेत्र थे, जिनमें कुछ पीलिमा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 28.7281)
- **Original**: वे सनातन ज्योतिःस्वरूप, लोकोंके लिये अनुग्रहके और ललाई छायी हुई थी। वे जले हुए पर्वतके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 28.7282)
- **Original**: मूर्त रूप, जटाधारी, सतीकी हड्डियोंसे शोभित, समान काले और महान्‌ बल-पराक्रमसे सम्पन्न
- **Translation**: 

---

### Verse 6 (Vaivtpuran 28.7283)
- **Original**: तपस्याओंके फल देनेवाले तथा सम्पूर्ण सम्पदाओंके थे। शरीर उत्तम बाघम्बर तथा विभूतिसे विभूषित
- **Translation**: 

---

### Verse 7 (Vaivtpuran 28.7284)
- **Original**: दाता थे। उनका वर्ण शुद्ध स्फटिकके सदृश थे। त्रिशूल और पट्टिश धारण किये हुए वे दोनों
- **Translation**: 

---

### Verse 8 (Vaivtpuran 28.7285)
- **Original**: उज्ज्वल था। उनके पाँच मुख और तीन नेत्र थे। ब्रह्मतेजसे प्रज्बलित हो रहे थे। उन्हें देखकर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 28.7286)
- **Original**: बे तत्त्वमुद्राद्वारा शिष्योंको गुद्या ब्रह्मका उपदेश कर परशुरामका मन भयग्रस्त हो गया। फिर भी बे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 28.7287)
- **Original**: रहे थे। योगीन्द्र उनके स्तबनमें तथा बड़े-बड़े डरते-डरते कुछ कहनेकों उद्यत हुए। उन्होंने
- **Translation**: 

---

### Verse 11 (Vaivtpuran 28.7288)
- **Original**: सिद्ध उनकी सेवामें नियुक्त थे। श्रेष्ठ पार्षद श्वेत विनीत होकर बड़ी नम्नताके साथ उन दोनों चँंवरोंद्वारा निरन्तर उनको सेवा कर रहे थे। वे महाबली उच्छूंखलोंके सामने अपना सारा वृत्तान्त
- **Translation**: 

---

### Verse 12 (Vaivtpuran 28.7289)
- **Original**: बुढ़ापा और मृत्युका हरण करनेवाले, गुणातीत, कह सुनाया। ब्राह्मणकी ज़ात सुनकर उन दोनोंके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 28.7290)
- **Original**: स्वेछ्छामय, परिपूर्णतम परब्रह्मके ध्यानमें निमग्र मनमें दयाका संचार हो आया, तब उन श्रेष्ठ
- **Translation**: 

---

### Verse 14 (Vaivtpuran 28.7291)
- **Original**: थे, जो ज्योतीरूप सबके आदि, प्रकृतिसे परे और अनुचरोंने दूतद्वारा महात्मा शंकरकी आज्ञा लेकर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 28.7292)
- **Original**: परमानन्दमय हैं। उन श्रीकृष्णका ध्यान करते परशुरामको भीतर प्रवेश करनेका आदेश दिया।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 28.7293)
- **Original**: समय उनके शरीरमें रोमाज्ञ हो रहा था तथा वे परशुराम उनको आज्ञा पाकर श्रीहरिका स्मरण
- **Translation**: 

---

### Verse 17 (Vaivtpuran 28.7294)
- **Original**: आँखोंमें आँसू भरे उत्तम स्वस्से उनकी गुणावलीका करते हुए भवनके अंदर प्रविष्ट हुए। वहाँ उन्होंने
- **Translation**: 

---

### Verse 18 (Vaivtpuran 28.7295)
- **Original**: गान कर रहे थे और भधूतेश्वर, रुद्रगण तथा एक-एक करके सोलह दरवाजोंको देखा, जो
- **Translation**: 

---

### Verse 19 (Vaivtpuran 28.7296)
- **Original**: क्षेत्रपाल उन्हें घेरे हुए थे। उन्हें देखकर परशुरामने
- **Translation**: 

---

### Verse 20 (Vaivtpuran 28.7297)
- **Original**: 352 + संक्षिप्त ब्रह्मवैवर्तपुराण * अ्रफडऋक फंड पक कह कफ कक 58 6 दर # 48% # 44 4444 4 4 ## 4 844 44 44448 $ 84% 4485 88 8/ 888 5 # 4 4 # 5 4 4 5 5 बड़े आदरके साथ सिर झुकाकर प्रणाम किया।
- **Translation**: 

---

