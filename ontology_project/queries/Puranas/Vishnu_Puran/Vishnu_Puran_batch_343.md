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

### Verse 1 (Vishnu Puran 0.6841)
- **Original**: तदम्मसा च॑ संस्पृष्टेप्रस्थिभस्मससु एते चर ख्वर्गमारो क्ष्यन्ति
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6842)
- **Original**: _ भगवहिष्णुपादाडुछ्टनिर्गतस्थ हि जलस्वैतन्पाहात्प्यम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6843)
- **Original**: यन्न केखछमभि- सनब्धिपूर्वक॑ स्त्रानाहुपभोगेषृूपकारकमनभि- संहितमप्यपेतप्राणस्पास्थिचर्मस््रायुकेशाहुपस्पृष्टं झरीरजमपि पतित॑ सद्यइुझरीरिणं स्वर्ग नयतीत्युक्त: प्रणम्य भगयते5श्वमादाय पिता- इसी समय सगरने अश्वमेध-यज्ञ आरम्भ किया
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6844)
- **Original**: उसमें उसके पुत्रोंद्रारा सुरक्षित घोड़ेको कोई व्यक्ति चुराकर पृथिवीमें घुस गया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6845)
- **Original**: तब उस घोड़ेके खुरोकि चिह्लॉंका अनुसरण करते हुए उनके पुत्रोमिंसे अत्येकने एक-एक योजन पुथिव्री खोद डाली
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6846)
- **Original**: तथा पातालमें पहुँचकर उन राजकुमारोंने अपने धोड़ेको फिरता हुआ देखा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6847)
- **Original**: पासहीमें मेघावरणहीन शरत्कालके सूर्यके समान अपने तेजसे सम्पूर्ण दिश्ञाओंको प्रकाशित करते हुए घोड़ेक्प्ें चुरानेयाले परमर्थि कपिल्फो सिर झ॒काये बैठे देखा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6848)
- **Original**: तब तो ये दुरात्मा अपने अस्ब-धाख्रोंको उठाकर 'यही हमारा अपकारी और यज्षमें त्रिश्न अलनेबाला है, इस घोड़ेको चुरानेबालेको मारो, मारो' ऐसा चिल्स्ते हुए डनकी ओर दौड़े
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6849)
- **Original**: तब भगवान्‌ कपिलदेवके कुछ आँख बदलकर देखते ही वे सब अपने हो दारीरसे उत्पन्न हुए अग्रिमें जलकर नष्ट हो गये
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6850)
- **Original**: महाराज सगरको जब मासूम हुआ कि घोड़ेका अनुसरण करनेवाले उसके समस्त पुत्र महर्षि कपिलके तेजसे दग्ध हो गये हैं तो उन्होंने असमझसके पुत्र अंशुमानको घोड़ा ले आनेके लिये नियुक्त किया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6851)
- **Original**: वह सगर-पुत्रोंद्रार ख़ोदे हुए मार्गसे कपिलजीके पास पहुँचा और भक्तिविरप्न होकर उनकी स्तुति की
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6852)
- **Original**: तब भगवान्‌ फपिल्ये उससे कहा, “बेटा ! जा, इस घोड़ेको ले जाकर अपने दादाको दे और तेरी जो इच्छा हो वही बर माँग ले । तेरा पौत्र गक़ाजीको स्वर्गसे पृथिवोपर छायेगा”
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6853)
- **Original**: इसपर अंशुमानने यही कहा कि मुझे ऐसा वर दीजिये जो ज्ह्मदण्डसे आहत होकर मरे हुए मेरे अस्वर्ग्ग पितृगणको स्वर्गकी प्राप्ति करानेवाल्त हो
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6854)
- **Original**: यह सुनकर भगवानने कहा, “मैं तुझसे पहले ही कह चुका हूँ कि तेय पौत्र गड़जीको स्वर्गसे पृथिवीपर छायेगा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6855)
- **Original**: उनके जलूसे इनकी अस्थियॉकी भस्मका स्पर्श होते ही ये सब स्वर्गको चले जायैँगे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6856)
- **Original**: भगवान्‌ विष्णुके चरणनखसे निकले हुए उस जलका ऐसा माहात्म्य है कि वह कामनापुर्वक केवल खानादि कार्योमें ही उपयोगी हो--सो नहीं, अपितु, बिगा कामताके मृतक पुष्षक्े अस्थि, चर्म, स्नायु अथवा केदा आदिका स्पर्श हो जानेसे या उसके दारीरका कोई अंग गिरनेसे भी वह देहधारीको तुरंत स्वर्गमें ले जाता है।”' भगवान्‌ कपिलके ऐसा कहनेपर वह उन्हें प्रणाम कर घोड़ेको छेकर
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6857)
- **Original**: आअ»्ड ] सतुर्थ अंदा 247 मरहेयज्ञमाजगाम
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6858)
- **Original**: सगरोः5्ष्यश्वमासाआझ ते अज्ञै समापयामरास
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6859)
- **Original**: सागर चात्मजप्रीत्या पुत्र॒त्वे कल्पितवान्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6860)
- **Original**: तस्यांशुमतो दिलीप: पुत्रो3भवत्‌
- **Translation**: 

---

