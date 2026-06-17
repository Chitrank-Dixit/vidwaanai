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

### Verse 1 (Markende Puran 0.2961)
- **Original**: तत्र अम्लिकाने उन शत्रुओंके प्रति बड़ा क्रोध फकिया। उस समय ऋ्रोधके कारण उनका मुख काला पड़ गया
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2962)
- **Original**: ललाटमें माँहें टेडी हो गर्बी और वहाँसे तुरंत विकरालपुखा काली प्रकट हुईं, जो वुलकार और पाश लिये हुए थीं
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2963)
- **Original**: ब्रिचित्र खदयाड़ भ्रारण किये और चीतेके चर्मकों साड़ी पहने तर मुण्डोंकी मालासे विभूषित थों। उनके शरोरका यांस सूख गया था, केवल हड्डियोंका ढाँचा था, जिससे ते अत्यन्त भयंकर जान पड़ती थीं
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2964)
- **Original**: उनका पुख बहुत विशाल था, जीभ लपलपानेके कारण ये और घो डराबनों प्रतीत होती थों। उनकी आँखें धोतरको धैसी हुई और लाल थीं, बे अपनो भयंकर गर्जनासे सम्धूर्ण दिशाओंको गुँजा रहो थौं
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2965)
- **Original**: बड़े-बड़े दैत्योंका वध करती हुई वे कालिकादेलों बड़े वेगसे दैत्योंको उस झेनापर टूट पर्डों और उन स्रक्तों भक्षण करने लगी
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2966)
- **Original**: चे पार्श्रशक्षकों, अल्डुशधारों महातरतों, काली करालवक्प्ान्तहुर्दर्शदशनोज्ण्यला
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2967)
- **Original**: योद्धाओं झौर घंटासाहित रिलने ही हाथियॉकों 3, पा*-गफ्लौ0। 2, जा0-यत्वति। 3, पा0>ता रणे। 4, शालनवी टेकाकारने सहाँ एक श्लोक अभिक चाट माय हू, जो उस प्रकार हैं /छश्ने श्णिंस देते घके जाए तुगैस्तण्‌ जेल पादेने पहला बसे धुउनजयम।
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2968)
- **Original**: + चणड और पुण्डका यध 25175 क्र 7 + #24797 + 8995
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2969)
- **Original**: +- 35454 + #
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2970)
- **Original**: 5 4 # # 4444 4, 8454 # # # 4 8 + 44+/4/45444 ## ##झइ## 4 44 55554 545 5: 55: 55: £5: £ 2:22: 6 70 एक ही हाथसे पकड्कर मूँहमें डाल लेती थीं
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2971)
- **Original**: इसी प्रकार छोड़े, रथ और सारधिके साथ रंथों मैनिकॉको मुँहमें डालकर वे उन्हें बड़े भयानक रूपसे चना डालती धीं
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2972)
- **Original**: किस्ीके लाल पक्रड़ लेतीं, किसीका गला दबा देतीं, छाताके धक्केसे गिराकर मार डालतों थीं
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2973)
- **Original**: वे असुररोके छोड़े हुए छड्ढे बद़े अस्त्र-शस्त्र पुँहठसे पकड़ लेती और रोषमें भरकर उनको दाँतोंसे पास डालती
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2974)
- **Original**: कालीतगे वलवान्‌ एं दुरात्मा दैत्योंकी वड़ सारी सेना राँद डालीं, खा डाली औं? ++/नौंकों मार भगाया
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2975)
- **Original**: कोई तलवबरक्ते जाट उतारे गले, कोई खट्ताज़से पीटे गये और कितने ही अमुर दातोंके ऊग्रभागसे क्रुचले जाकर मृध्चुको प्राप्त हुए ।15
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2976)
- **Original**: इस प्रकार देवीने असुरोंक्ी उस सारी रूनाकों द्वाणरने मार गिराया। रह देख चण्ड उर अत्यन्त भयानक्त कलीदेनीझों ओर चौड्डा ।76
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2977)
- **Original**: तथा महादेत्य मण्डने भी अत्यतत भवड्भर बाणोंकी वर्षासें तथा हजारों बार चलाये हुए चक्रेंसे उन भयानक नेत्रोंबाली देबीकों आच्छादित क्र दिया
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2978)
- **Original**: ते अनेकों चक्र देवीके मुखमें समाते हुए ऐसे ऊान पड़े, मानों सूर्यके बहुतेरे मण्डल बादलौंके उदरमें प्रवेश कर रहे हों
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2979)
- **Original**: तब भयड्जूर गर्जना करनेवाली कालोने अत्यन्त रोषमें भरकर विकर अट्बह्मास क्रिया। उस समय उनके विकराल बदनके भीतर कंटिनतासे देखे जा सकनेवाले दाँतोंकी प्रभारों श्रे अत्यन उज्ज्वल दिखाया देती थीं
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2980)
- **Original**: देबीने बहुत बड़ी तलबार हाथ्रमें ले 'हं' का उच्चारण करके चण्डपर धावा किया और उसके केश पकड्ुकर ठसमी तलवारसे ठसका पस्तक्र क्राट डाला
- **Translation**: 

---

