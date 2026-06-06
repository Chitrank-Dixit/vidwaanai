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

### Verse 1 (Vishnu Puran 0.11361)
- **Original**: 36 तामग्रतो हरि्दष्ठा मीलिताक्षस्सुदर्शनम्‌। मुमतोच बाणमुदिश्यच्छेत्तु बाहुबन॑ रिपो:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11362)
- **Original**: 37 क्रमेण तत्तु बाहूनां बाणस्याच्युतचोदितम्‌ । छेद॑ चक्रेडसुरापास्तशस्त्रौषक्षपणादृतम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11363)
- **Original**: 38 छिज्ले बाहुबने तत्तु करस्थं मधुसूदनः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11364)
- **Original**: मुमुक्षुबणनाशाय.. विज्ञातस्त्रिपुरद्धिधा
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11365)
- **Original**: 39 समुपेत्याह गोबिन्द॑ सामपूर्बपुमापतिः । बिलोक्य बाएं दोर्दण्डच्छेदासुक्स्नाववर्षिणम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11366)
- **Original**: 40 अकिष्णुपुराण [ अ0 33 कृष्णचन्द्रके हुंकारसे रक्तिहीन हो जानेसे स्कामिकारत्तिकेय भी भागने लगे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11367)
- **Original**: इस प्रकार श्रीकृष्णचद्धद्वारा महादेकजीके निद्राभिभूत, झिवगणोंके क्षीण हो जानेपर कृष्ण, प्रद्युश्न और बलूभद्रजीके साथ युद्ध करनेके लिये वहाँ आणासुर साक्षात्‌ नन्दीश्वरद्वारा हाँके जाते हुए महान्‌ रथपर चढ़कर आया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11368)
- **Original**: उसके आते ही महावोर्यशाली बलभद्रजीने अनेकों नाण बरसाकर बाणासुरकों सेनाको छिन्न-भिन्न कर डाला; तब यह वीरघर्मसे भ्रष्ट होकर भागने लगी
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11369)
- **Original**: बाणासुरने देखा कि डसकी सेनाको बलभद्गजी बड़ों फुर्तीसि हलसे खींच-स्वींचकर मूसलसे मार रहे हैं और श्रीकृष्णचन्द्र उसे वाणोंसे जीधें डालते हैं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11370)
- **Original**: तब बाणासुरका श्रीकृष्णचनद्रके साथ घोर युद्ध छिड़ गया। बे दोनों परस्पर कबचभेदी बाण छोड़ने लगे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11371)
- **Original**: परंतु भगवान्‌ कृष्णने बाणासुरके छोड़े हुए तीखे वाणोंको अपने वाणोंसे काट डाला; और फिर बाणासुर कृष्णको तथा कृष्ण बाणासुरको बांधने छगे
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11372)
- **Original**: हे द्विज ! उस समय परस्पर चोट करनेवाले बाणासुर और कृष्ण दोनों ही विजयकी इच्छासे निरन्तर झीक्रतापूर्वक अख्न-शझख्र छोड़ने रंगे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11373)
- **Original**: अन्तमें, समस्त वाणोके छिन्न और सम्पूर्ण अख्न- शास्त्रोंके निष्फल हो जानेपर ओ्रीहरिने बाणासुर्को मार डालनेका विचार किया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11374)
- **Original**: तब दैत्यमण्डलूके जात्रु भगवान्‌ कृष्णने सैकड़ों सूर्योंके समान प्रकाशमान अपने सुदर्शनचक्रव्रे हाथमें ले लिया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11375)
- **Original**: जिस समय भगवान्‌ मधुसूदन बाणासुरको मारनेके लिये चक्र छोड़ना ही चाहते थे उसी समय दैल्योंकी विद्या (मन्ल्मयी कुलदेजी) कोटरी भगवान्‌के सामने नप्नावस्थामें उपस्थित हुई
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11376)
- **Original**: उसे देखते ही भगवानने नेत्र मूँद लिये और नाणासुरको लक्ष्य करके उस जत्रुकी भुजाओंके वनको काटनेके लिये सुदर्शनचक्र छोड़ा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11377)
- **Original**: भगवान्‌ अच्युतके द्वारा प्रेरित उस चक्रने दैत्योंकि छोड़े हुए अखसमृहको काटकर क्रमशः बाणासुरकी भुजाओंक्वे काट डाल्झा [ केवल दो भुजाएँ छेड़ दीं]
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11378)
- **Original**: तब त्रिपुरशत्रु भगयान्‌ शबद्भूर जान गये कि श्रीमधुसूदन बाणासुरके बाहुवनको काटकर अपने हाथमें सु चक्रको ठसका वध करनेके लिये फिर छोड़ना हैं। 39
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11379)
- **Original**: अतः: बाणासुरको अपने खण्डित भुजदप्योसे ल्थरेहकी धारा बहाते देख
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11380)
- **Original**: आ* 33 ] पक्रम अंश 401 श्रीशडटुर उवाच कृष्ण कृष्ण जगन्नाथ जाने ल्वां पुरुषोत्तमम्‌ । परेश॑ परमात्मानमनादिनिध्न॑ हरिम्‌
- **Translation**: 

---

