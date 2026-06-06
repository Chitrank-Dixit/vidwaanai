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

### Verse 1 (Vishnu Puran 0.11781)
- **Original**: हे ट्विजोत्तम ! उस चरणको मृगाकार देख उस य्याधने उसे दुरहोसे खड़े-खड़े उसी तोमरसे बींघ डाला
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11782)
- **Original**: किंतु वहाँ पहुँचनेपर उसने एक चतुर्भुजधारी मनुष्य देखा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11783)
- **Original**: यह देखते ही वह चरणोंमें गिस्कर बरारम्बार उनसे कहने लगा--“ प्रसन्न होइये, प्रसन्न होइये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11784)
- **Original**: पैने बिना जाने ही मृगकी आशक़्से यह अपराध किया है, कृपया क्षमा कीजिये । मैं अपने पापसे दग्ध हो रहा हूँ, आप मेरी रक्षा कीजिये"
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11785)
- **Original**: श्रीपराशरजी बोले--तब भगवानने उससे कहा--“लुब्यक ! तू तनिक भी न डर; मेरी कृपासे तू अभी देवताओंके स्थान स्वर्गलोकको चलता जा
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11786)
- **Original**: इन भगवद्वाक्योंके समाप्त होते हो कहाँ एक विमान आया, उसपर चढ़कर वह व्याध भगवान्‌की कृपासे उसी समय #% महाभारतमें यह प्रसंग आया हैं कि---एक बार महर्षि दुर्वासा ओकृष्णचन्द्रजोके यहाँ आये और भगवानसे सत्कार पाकर उन्होंने कह्ा कि आप मेरा जूँठछा जल अपने सारे शरीरमें लगाइये । भगवानने वैसा ही किया, परंतु 'ब्राह्मणका जूँठ पैरसे नहीं छूना चाहिये' ऐसा सोचकर परमें नहीं छगाया । इसपर दुर्वासाने शाप दिया कि आपके पैरमें कभी छेट हो जआायगा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11787)
- **Original**: अ* 38 ] पश्षम अंझ ड9्5 गते तस्मिन्स भगवान्संयोज्यात्मानमात्मनि । ब्रह्ममूतेउव्ययेडचिन्तये. वासुदेवमयेउमले
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11788)
- **Original**: 74 अजन्मन्यमरे विष्णावप्रमेये5सिल्लात्मनि । स्वर्गको चला गया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11789)
- **Original**: उसके चले जानेपर भगवान्‌ ,, अमर, अजन्मा, अमर, अप्रमेय, अखिलात्पा और ब्रह्मस्वरूप विष्णुभगवानमें लीन कर त्रिगुणात्मक गतिको पार करके इस मनुष्य-झरीरको छोड़ तत्याज मानुष देहमतीत्य त्रिविधां गतिम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11790)
- **Original**: अश्यया--क औ हक इति श्रीविष्णुपुराणे पञ्ममेंडशें सप्तत्रिशोउध्यायः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11791)
- **Original**: जज औ एप अड़तीसवाँ अध्याय यादबवॉका अन्त्येप्टि-संस्कार परीक्षितका राज्याभिषेक तथा पाण्डवोंका स्वर्गारोहण औपराचर उवाच अर्जुनोईपि तदान्विष्य रामकृष्णकलेवरे । संस्कार लम्भयामास तथान्येषामनुक्रमात्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11792)
- **Original**: 9 अष्टौ महिष्य: कथिता रुक्मिणीप्रमुखास्तु या: । उपगुहा हरेंदेंहे॑विविशुस्ता हुताइनम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11793)
- **Original**: 2 रेवती चापि रामस्य देहमाहिलिष्य सत्तमा
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11794)
- **Original**: विवेज्ञ ज्वलित वह्निं तत्सड्राह्नादशीतलम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11795)
- **Original**: 3 उप्रसेनस्तु _तच्छूत्वा तथैवानकदुन्दुभिः । देवबकी रोहिणी चैत्र विविशुर्जातवेदसम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11796)
- **Original**: 4 ततोडर्जुनः प्रेतकार्य कृत्वा तेषां यथाविधि । निश्चक्राम जन॑ सर्व गृहीत्वा वज़्मेव च
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11797)
- **Original**: 5 द्वारवत्या विनिष्क्रान्ता: कृष्णपल्य: सहस्नशः । बज्र जनं च कौन्तेय: पालयज्छनकैर्ययो
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11798)
- **Original**: 6 सभा सुधर्मा कृष्णेन मर्त्यलोके समुन्झिते । स्वर्ग जगाम मैत्रेय पारिजातश्ष पादप:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11799)
- **Original**: 7 यस्समिन्दिने हरिययातो दिवं॑ सन्त्यज्य मेदिनीम्‌ । तस्मिन्नेवावतीर्णाठय कालकायो बली कलि:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11800)
- **Original**: 8 प्लावयामास तां शून्यां द्वारकां च महोदधिः । वासुदेबगृहं त्वेके न प्लावयति सागर:
- **Translation**: 

---

