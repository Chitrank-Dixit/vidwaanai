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

### Verse 1 (Vaivtpuran 543.14254)
- **Original**: ही मेरे अभीष्ट कार्यको सम्पन्न करें। अतिशय सुख, सम्पूर्ण सिद्धियाँ, परम दुलंभ नारद! नहुषकी बात सुनकर सब मुनि समस्त ऐश्वर्य तथा जो तपस्यासे भी नहीं मिल
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.14255)
- **Original**: कौतृहलवश एक-दूसरेको देखते हुए जोर-जोरसे सकती, वह हरिभक्ति अथवा मुक्ति भी हम तुम्हें हँसने लगे। राजाको भगवान्‌ विष्णुकी मायासे दे सकते हैं। वत्स! बोलो, इस समय तुम्हें किस
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.14256)
- **Original**: वेष्टित एवं मोहित मानकर उन दीनवत्सल वस्तुकी इच्छा है? वह सब तुम्हें देकर ही हम।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.14257)
- **Original**: सप्तर्षियोंने कृपापूर्वकक राजाका वाहन बननेकी तपस्याके लिये जायँगे। जो क्षण श्रीकृष्णकी प्रतिज्ञा कः ली। उसकी शिविका मुक्ता और आराधनाके बिना व्यतीत होता है, वह लाख
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.14258)
- **Original**: माणिक्यसे सुशोभित थी। ऋषियोंने उसे कंधेपर युगोंके समान है अर्थात्‌ श्रीकृष्ण-भजनके बिना
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.14259)
- **Original**: उठा लिया और राजा नहुष सुन्दर वेष एवं रन्मय यदि एक क्षण भी व्यर्थ बीता तो समझना चाहिये
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.14260)
- **Original**: आभूषणोंसे विभूषित हो उस शिविकासे चला। कि हमारे एक लाख युग व्यर्थ बीत गये। जो
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.14261)
- **Original**: उस वाहनद्वारा अभीष्ट स्थानपर पहुँचनेमें अधिक दिन श्रीहरिके ध्यान और सेवनसे शून्य रह गया,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.14262)
- **Original**: विलम्ब होता देख राजा सप्तर्षियोंको डाँटने- *युगलक्षसम॑ यक्च क्षणं कृष्णार्चन॑ बिना । तदिन॑ दुर्दिनं यक्तद्ध्यानसेवनवर्जितम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.14263)
- **Original**: विना तत्सेषन॑ यो हि थिषयान्य च याम्छति । विषमत्ति. प्रणाशाय. चिहायामृतमीप्सितम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.14264)
- **Original**: [63 ] सं0 ब्र0 बै0 पुराण 2 (60। 32-33)
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.14265)
- **Original**: 620 * संक्षिस ब्रह्मवैवर्तपुराण * ##%#%#%#%#######% कक ########%#$%ककक कड़क 468 6
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.14266)
- **Original**: 4 के अपने गुरुका स्वर सुनकर महेन्द्रका मन प्रसन्नतासे खिल उठा। वे सूक्ष्मरूपको छोड़कर अपने ही रूपसे उनके निकट आये। उन्होंने की 20
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.14267)
- **Original**: भक्तिभावसे गुरुके चरणोंमें दण्डकी भाँति पड़कर सिरसे उन्हें प्रणाम किया और रोने लगे। उस जज समय महाभयभीत एवं रोते हुए इन्द्रको गुरुने सानन्द हृदयसे लगा लिया। फिर उनसे प्रायश्चित्तके ,
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.14268)
- **Original**: लिये सोमयाग करवाकर उन्हें रमणीय रत्रमय फटकारने लगा। शिविकाके उस मार्गपर सबसे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.14269)
- **Original**: सिंहासनपर बिठाया और पहलेसे चौगुना उत्तम आगे चलते थे दुर्वासा। उन्हें राजाकी फटकारपर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.14270)
- **Original**: ऐश्वर्य प्रदान किया। तदनन्तर सब देवता आकर क्रोध आ गया और वे शाप देते हुए बोले--' मूढ़चित्त
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.14271)
- **Original**: उनकी सेवा करने लगे। शचीने पुनः अपने पति महाणज! तुम महान्‌ अजगर होकर नीचे गिर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.14272)
- **Original**: देवराज इन्द्रको प्राप्त कर लिया और निवासमन्दिरमें पड़ो। धर्मपुत्र युधिष्ठिरके दर्शन होनेसे तुम
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.14273)
- **Original**: फूलोंकी सेजपर वह उनके साथ आननन्‍्दपूर्वक अजगरकी योनिसे छूट जाओगे। तत्पश्चात्‌ रन्नमय
- **Translation**: 

---

